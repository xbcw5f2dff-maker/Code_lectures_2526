import csv
from asyncio import current_task


class Node:
    def __init__(self, task_name: str, duration: int, priority: int):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add_task(self, task_name: str, duration: int, priority: int):
        newNode = Node(task_name, duration, priority)
        if self.__tail == None:
            self.__head = self.__tail = newNode

        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next

        self.__size += 1

    def remove_task(self, task_name: str):
        if self.__head is None:
            return None


        if self.__head.task_name == task_name:
            removed = self.__head
            self.__head = self.__head.next
            self.__size -= 1

            # Als lijst hierdoor leeg wordt
            if self.__head is None:
                self.__tail = None

            return removed.task_name

            # Algemeen geval: zoeken in de lijst
        previous = self.__head
        current = self.__head.next

        while current is not None:
            if current.task_name == task_name:

                previous.next = current.next
                self.__size -= 1

                # Als we de laatste node verwijderen → tail aanpassen
                if current == self.__tail:
                    self.__tail = previous

                return current.task_name

            previous = current
            current = current.next
        return None

    def display_tasks(self):
        result = "["
        current = self.__head

        while current is not None:
            result += (
                    current.task_name
                    + " (prio " + str(current.priority)
                    + ", dur " + str(current.duration)
                    + ")"
            )

            current = current.next

            if current is not None:
                result += ", "
            else:
                result += "]"

        return result

    def find_task(self, task_name: str):
        current = self.__head
        while current is not None:
            if current.task_name == task_name:
                return (current.task_name, current.duration, current.priority)
            current = current.next
        return None

    def calculate_total_duration(self):
        current = self.__head
        duration = 0
        while current is not None:
            duration += current.duration
            current = current.next
        return duration

    def read_tasks_from_CSV(self, filepath):
       with open(filepath, "r") as file:
           reader = csv.reader(file)

           next(reader)
           for row in reader:
               if len(row) != 3:
                   continue
               task_name = row[0]
               duration = int(row[1])
               priority = int(row[2])
               self.add_task(task_name, duration, priority)

    def reorder_tasks_by_priority(self):
        # 1. Alle nodes uit de linked list halen in een gewone Python-lijst
        tasks = []
        current = self.__head
        while current is not None:
            tasks.append((current.task_name, current.duration, current.priority))
            current = current.next

        # 2. Python laten sorteren op priority (index 2 in de tuple)
        tasks.sort(key=lambda x: x[2])  # x = (task_name, duration, priority)

        # 3. De linked list leegmaken
        self.__head = None
        self.__tail = None
        self.__size = 0

        # 4. Alles opnieuw in de juiste volgorde toevoegen
        for name, duration, priority in tasks:
            self.add_task(name, duration, priority)


    def reorder_tasks_by_priority_duration(self):
        tasks = []
        current = self.__head
        while current is not None:
            tasks.append((current.task_name, current.duration, current.priority))
            current = current.next

        # sorteer op (priority, duration)
        tasks.sort(key=lambda x: (x[2], x[1]))

        self.__head = None
        self.__tail = None
        self.__size = 0

        for name, duration, priority in tasks:
            self.add_task(name, duration, priority)

    def optimize_tasks(self):
        # sorteer op priority en duration
        self.reorder_tasks_by_priority_duration()

        print("Optimized Task Order:")
        print(self.display_tasks())

        print("Total duration:", self.calculate_total_duration())


    #met hulperfunctie zoals opgave vraagt
    def sorted_insert_by_priority(self, head, node):
        """
        Voegt één node gesorteerd in op prioriteit (lage priority = komt eerst).
        Geeft de (mogelijk nieuwe) head terug.
        """

        # Geval 1: lege lijst of node moet helemaal vooraan
        if head is None or node.priority < head.priority:
            node.next = head
            return node  # node is nu de nieuwe head

        # Geval 2: ergens in het midden of einde invoegen
        current = head

        # Loop door de lijst zolang de volgende node een lagere/even lage priority heeft
        while current.next is not None and current.next.priority <= node.priority:
            current = current.next

        # Nu staat current op de node vóór het invoegpunt
        node.next = current.next  # node wijst naar de node die erna moet komen
        current.next = node  # huidige node wijst nu naar onze nieuwe node

        return head

    #hoofdfunctie
    def reorder_tasks_by_priority(self):
        """
        Maakt een nieuwe gesorteerde linked list op basis van priority.
        Gebruik de helperfunctie sorted_insert_by_priority().
        """

        new_head = None
        current = self.__head

        while current is not None:
            next_node = current.next  # volgende node bewaren
            current.next = None  # node losmaken uit oude lijst

            # gesorteerd invoegen in nieuwe lijst
            new_head = self.sorted_insert_by_priority(new_head, current)

            current = next_node  # verdergaan

        self.__head = new_head  # lijst vervangen door nieuwe gesorteerde lijst

    #hulpfunctie
    def sorted_insert_by_priority_duration(self, head, node):
        """
        Voegt één node gesorteerd in op:
            1) priority (laag = eerst)
            2) duration (laag = eerst bij gelijke priority)
        Geeft de (mogelijk nieuwe) head terug.
        """

        # ---- Geval 1: Lege lijst OF node moet helemaal vooraan ----
        if (head is None or
                node.priority < head.priority or
                (node.priority == head.priority and node.duration < head.duration)):
            node.next = head
            return node  # node is nieuwe head

        # ---- Geval 2: midden of einde ----
        current = head

        # Loop tot we een plek vinden waar node moet worden ingevoegd
        while current.next is not None:

            next_node = current.next

            # stop als node vóór next_node moet komen
            if (node.priority < next_node.priority or
                    (node.priority == next_node.priority and node.duration < next_node.duration)):
                break

            current = current.next

        # Invoegen
        node.next = current.next
        current.next = node

        return head

    #hoofdfunctie
    def reorder_tasks_by_priority_duration(self):
        """
        Maakt een nieuwe linked list gesorteerd op:
            1) priority
            2) duration
        met behulp van sorted_insert_by_priority_duration()
        """

        new_head = None
        current = self.__head

        while current is not None:
            next_node = current.next  # volgende node onthouden
            current.next = None  # huidige node losmaken van oude lijst

            # Gesorteerd invoegen in nieuwe lijst
            new_head = self.sorted_insert_by_priority_duration(new_head, current)

            current = next_node  # ga door naar volgende node

        self.__head = new_head  # vervang oude lijst door gesorteerde lijst









