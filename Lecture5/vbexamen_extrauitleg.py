import csv
from asyncio import current_task   # 👉 dit wordt nergens gebruikt; mag eigenlijk weg


class Node:
    def __init__(self, task_name: str, duration: int, priority: int):
        # Eén taak in de linked list:
        # - task_name: naam van de taak
        # - duration: duur in minuten
        # - priority: 1 = hoogste prioriteit, grotere cijfers = lagere prioriteit
        # - next: verwijzing naar de volgende Node in de lijst
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None   # in het begin wijst de node naar niets


class LinkedList:
    def __init__(self):
        # __head: eerste node in de lijst
        # __tail: laatste node in de lijst
        # __size: aantal nodes in de lijst
        self.__head = None
        self.__tail = None
        self.__size = 0

    # --------------------------------------------------
    # 1) Taak toevoegen aan het einde van de lijst
    # --------------------------------------------------
    def add_task(self, task_name: str, duration: int, priority: int):
        # Maak een nieuwe Node voor deze taak
        newNode = Node(task_name, duration, priority)

        # Als de lijst leeg is → head én tail worden deze nieuwe node
        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            # Lijst is niet leeg: de huidige tail moet naar de nieuwe node wijzen
            self.__tail.next = newNode
            # Tail verschuiven naar de nieuwe node
            self.__tail = self.__tail.next

        # Grootte bijhouden
        self.__size += 1

    # --------------------------------------------------
    # 2) Taak verwijderen op basis van task_name
    # --------------------------------------------------
    def remove_task(self, task_name: str):
        # Als de lijst leeg is → niets te doen
        if self.__head is None:
            return None

        # Speciaal geval: de eerste node (head) is degene die we willen verwijderen
        if self.__head.task_name == task_name:
            removed = self.__head                  # bewaar de te verwijderen node
            self.__head = self.__head.next         # head schuift op naar de volgende node
            self.__size -= 1

            # Als de lijst hierdoor leeg wordt, moet tail ook None worden
            if self.__head is None:
                self.__tail = None

            return removed.task_name               # naam van verwijderde taak teruggeven

        # Algemeen geval: we zoeken verder in de lijst
        previous = self.__head          # node vóór current
        current = self.__head.next      # node die we aan het controleren zijn

        while current is not None:
            if current.task_name == task_name:
                # Sla current over: previous.next wijst nu naar de node na current
                previous.next = current.next
                self.__size -= 1

                # Als we de laatste node verwijderen → tail aanpassen
                if current == self.__tail:
                    self.__tail = previous

                return current.task_name

            # één stap verder in de lijst
            previous = current
            current = current.next

        # Niet gevonden
        return None

    # --------------------------------------------------
    # 3) Alle taken tonen als één string
    # --------------------------------------------------
    def display_tasks(self):
        # We bouwen een string zoals:
        # [Task1 (prio 1, dur 10), Task2 (prio 2, dur 5)]
        result = "["
        current = self.__head

        while current is not None:
            # taak-info toevoegen
            result += (
                current.task_name
                + " (prio " + str(current.priority)
                + ", dur " + str(current.duration)
                + ")"
            )

            # naar volgende node
            current = current.next

            # Als er nog een node komt → komma, anders sluiten we de haak
            if current is not None:
                result += ", "
            else:
                result += "]"

        return result

    # --------------------------------------------------
    # 4) Taak zoeken op naam
    # --------------------------------------------------
    def find_task(self, task_name: str):
        # Doorloop de lijst en zoek naar een node met dezelfde task_name
        current = self.__head
        while current is not None:
            if current.task_name == task_name:
                # Details als tuple teruggeven
                return (current.task_name, current.duration, current.priority)
            current = current.next
        return None   # niet gevonden

    # --------------------------------------------------
    # 5) Totale duur van alle taken
    # --------------------------------------------------
    def calculate_total_duration(self):
        current = self.__head
        duration = 0

        # Som van alle durations van alle nodes
        while current is not None:
            duration += current.duration
            current = current.next

        return duration

    # --------------------------------------------------
    # 6) Taken inladen uit een CSV-bestand
    #    verwacht per rij: task_name,duration,priority
    # --------------------------------------------------
    def read_tasks_from_CSV(self, filepath):
        # Open CSV-bestand in leesmodus
        with open(filepath, "r") as file:
            reader = csv.reader(file)

            # Eerste rij overslaan als dat bv. een header is
            next(reader)

            # Elke rij is een list, bv ["Task A","10","1"]
            for row in reader:
                # Als het geen 3 kolommen zijn → overslaan
                if len(row) != 3:
                    continue
                task_name = row[0]
                duration = int(row[1])
                priority = int(row[2])

                # Voeg taak toe aan de linked list
                self.add_task(task_name, duration, priority)

    # --------------------------------------------------
    # 7) (EERSTE versie) Reorder by priority met Python-lijst
    #    → LET OP: later overschrijf je deze methode met de helper-versie
    # --------------------------------------------------
    def reorder_tasks_by_priority(self):
        # 1. Alle nodes in een gewone Python-lijst steken
        tasks = []
        current = self.__head
        while current is not None:
            tasks.append((current.task_name, current.duration, current.priority))
            current = current.next

        # 2. Sorteren op priority (x[2])
        tasks.sort(key=lambda x: x[2])

        # 3. Linked list leegmaken
        self.__head = None
        self.__tail = None
        self.__size = 0

        # 4. Gesorteerd terug toevoegen
        for name, duration, priority in tasks:
            self.add_task(name, duration, priority)

    # --------------------------------------------------
    # 8) (EERSTE versie) Reorder by (priority, duration) met Python-lijst
    #    → LET OP: ook deze wordt later overschreven door helper-versie
    # --------------------------------------------------
    def reorder_tasks_by_priority_duration(self):
        tasks = []
        current = self.__head
        while current is not None:
            tasks.append((current.task_name, current.duration, current.priority))
            current = current.next

        # Sorteren op (priority, duration)
        tasks.sort(key=lambda x: (x[2], x[1]))

        self.__head = None
        self.__tail = None
        self.__size = 0

        for name, duration, priority in tasks:
            self.add_task(name, duration, priority)

    # --------------------------------------------------
    # 9) Extra: optimalisatie-functie
    # --------------------------------------------------
    def optimize_tasks(self):
        # Sorteer op (priority, duration)
        self.reorder_tasks_by_priority_duration()

        print("Optimized Task Order:")
        print(self.display_tasks())

        print("Total duration:", self.calculate_total_duration())

    # ==================================================
    # Vanaf hier: implementatie MET helperfuncties,
    # zoals de opgave vraagt
    # ==================================================

    # --------------------------------------------------
    # 10) Helper: gesorteerd invoegen op priority
    # --------------------------------------------------
    def sorted_insert_by_priority(self, head, node):
        """
        Voegt één node gesorteerd in op prioriteit (lage priority = eerst).
        Geeft de (mogelijk nieuwe) head terug.
        """

        # Geval 1: lege lijst of node moet helemaal vooraan
        if head is None or node.priority < head.priority:
            node.next = head         # node wijst naar oude head
            return node              # node wordt de nieuwe head

        # Geval 2: in het midden of einde invoegen
        current = head

        # Loop zolang de volgende node bestaat én een priority heeft
        # die kleiner of gelijk is dan die van node
        while current.next is not None and current.next.priority <= node.priority:
            current = current.next

        # current staat nu op de node vóór het invoegpunt
        node.next = current.next     # node wijst naar de node na current
        current.next = node          # current wijst nu naar node

        return head

    # --------------------------------------------------
    # 11) Hoofd-functie: reorder op priority (met helper)
    #     (OVERSCHRIJFT de eerdere simpele versie!)
    # --------------------------------------------------
    def reorder_tasks_by_priority(self):
        """
        Maakt een nieuwe gesorteerde linked list op basis van priority.
        Gebruik de helperfunctie sorted_insert_by_priority().
        """

        new_head = None
        current = self.__head

        # Elke node losmaken uit de oude lijst en gesorteerd invoegen
        # in new_head
        while current is not None:
            next_node = current.next   # volgende node onthouden
            current.next = None        # huidige node losmaken

            new_head = self.sorted_insert_by_priority(new_head, current)

            current = next_node        # verder gaan met de volgende

        # vervang oude lijst door de gesorteerde lijst
        self.__head = new_head

    # --------------------------------------------------
    # 12) Helper: gesorteerd invoegen op (priority, duration)
    # --------------------------------------------------
    def sorted_insert_by_priority_duration(self, head, node):
        """
        Voegt één node gesorteerd in op:
            1) priority (laag = eerst)
            2) duration (laag = eerst bij gelijke priority)
        Geeft de (mogelijk nieuwe) head terug.
        """

        # Geval 1: lege lijst OF node moet helemaal vooraan
        if (head is None or
                node.priority < head.priority or
                (node.priority == head.priority and node.duration < head.duration)):
            node.next = head          # node wijst naar oude head
            return node               # node wordt nieuwe head

        # Geval 2: in het midden of einde
        current = head

        # Loop tot we een plek vinden waar node vóór current.next moet komen
        while current.next is not None:
            next_node = current.next

            # Stop als node een hogere voorrang heeft dan next_node
            if (node.priority < next_node.priority or
                    (node.priority == next_node.priority and node.duration < next_node.duration)):
                break

            current = current.next

        # Invoegen tussen current en current.next
        node.next = current.next
        current.next = node

        return head

    # --------------------------------------------------
    # 13) Hoofd-functie: reorder op (priority, duration) met helper
    #     (OVERSCHRIJFT de eerdere simpele versie!)
    # --------------------------------------------------
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
            next_node = current.next    # volgende node onthouden
            current.next = None         # huidige node losmaken van oude lijst

            # Gesorteerd invoegen in nieuwe lijst
            new_head = self.sorted_insert_by_priority_duration(new_head, current)

            current = next_node         # ga door naar volgende node

        # Oude head vervangen door de nieuwe gesorteerde lijst
        self.__head = new_head
