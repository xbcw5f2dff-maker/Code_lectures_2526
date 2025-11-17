class LinkedList:                                    #de linkedlist klasse (het skelet)
    def __init__(self):                              
        self.__head = None                           #eerste node MAAR verwijst enkel naar de 1ste node: self.__head ──► [A]──►[B]──►[C]
        self.__tail = None                           #laatste node MAAR "idem"
        self.__size = 0                              #hoeveel nodes er zijn (bij begin is de lijst leeg)                          

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:                         #als de lijst leeg is return dan None
            return None
        else:                                        #anders zit de 1ste node in self.__head => return dit
            return self.__head.element
    
    # Return the last element in the list            #exact zelfde als getfirst(self) maar dan met tail
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element               #self.__tail is enkel de pijl, self.__tail.element is het element waarnaar die pijl wijst 

    # Add an element to the beginning of the list  
    def addFirst(self, e):                                               #in begin: self.__head ──► [A]──►[B]──►[C]──►None
        newNode = Node(e) # Create a new node                            #hier maak je een nieuwe node: newNode ──► [X]──►None
        newNode.next = self.__head # link the new node with the head     #newnode.next = self.__head betekent dat newnode verwijst naar de oude head dus bv X wijst naar A 
        self.__head = newNode # head points to the new node              #dan zeg je dat self.__head (de pijl) wees naar A en nu wil je dat de pijl van self.__head naar X wijst zodat je krijgt: newNode ──► [X]──►[A]──►[B]──►[C] 
        self.__size += 1 # Increase list size                            

        if self.__tail == None: # the new node is the only node in list 
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):                                                            
        newNode = Node(e) # Create a new node for e                            #maak de nieuwe node aan 
    
        if self.__tail == None:                                                #als de lijst leeg is (tail verwijst naar niets):
            self.__head = self.__tail = newNode # The only node in list        #dan: head en tail moeten naar de nieuwe node verwijzen
        
        else:                                                                  #als de lijst niet leeg was bv: tail verwijst naar C en we willen D toevoegen
            self.__tail.next = newNode # Link the new with the last node       #de huidige laatste node C verwijst nu naar D
            self.__tail = self.__tail.next # tail now points to the last node  #we zettende tail nu op D
                                                                               #zie het als: self.__tail.next => naarwaar verwijst de node op de tail en self.__tail => verwijst naar de node op de tail zelf 
        self.__size += 1 # Increase size                                       

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle                                #je wil bv invoegen op index 2, current start op 1 ste element en current wordt current next, zo gaat dit doot tot current net voor de index staat waar je het wilt invoegen
            current = self.__head                                   #dan sla je de  index (currentnext) waar je het wilt invoegen op in temp 
            for i in range(1, index):                               #dan zeg je dat de node die je wilt invoegen op de plaats van die index komt die je opgeslagen hebt 
                current = current.next                              #uiteindelijk zeg je dat je temp nu laat verwijzen naar de volgende locatie 
            temp = current.next                                     #zie word doc voor betere uitleg
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element o 
    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    # Return the element from this list at the specified index 
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class, dit maakt een node aan; 1 blokje in een linkedlist en bestaat uit element en next 
class Node:
    def __init__(self, e):         #de constructor; elke keer als je schrijft n = Node(5) dan voert python deze __init__ uit, argument e = de waarde die wordt opgeslagen in de node 
        self.element = e           #we bewaren de waarde in de node dus in dit geval element = 5 en next = None 
        self.next = None           #in het begin weet de node niet wie de volgende is dus daarom next = None, later verandert dit; node1.next = node2 dan krijgen we node1 => node 2 => None 

#zorgt ervoor dat je kan schrijven: for x in mijLinkedlist: print(x), bestaat omdat python de lijst moet kunnen doorlopen, daarvoor moet de klasse een iterator teruggeven die telkens het volgende element neemt 
class LinkedListIterator:          #klasse die isntaat voor het overlopen vd nodes in een linkedlist 
    def __init__(self, head): 
        self.current = head        #we bewaren een pointer naar de node waar we ons nu bevinden 
        
    def __next__(self):            #functie die wordt opgeroepen om telkens het volgende element te geven in de loop
        if self.current == None:   #dit betekent dat we voorbij het einde vd linkedlist zijn, er bestaat geen volgende node 
            raise StopIteration    #dus dan moet het stoppen 
        else:                      #als we niet op het einde zijn:
            element = self.current.element #dan halen we de waarde op vd node waar we ons nu bevinden 
            self.current = self.current.next #erna schuiven we naar de volgende node
            return element    
        
