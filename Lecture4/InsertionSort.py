# The function for sorting elements in ascending order
def insertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[0..i-1] so that
        #   lst[0..i] is sorted.
        currentElement = lst[i] #element dat we willen sorteren 
        k = i - 1 #laatste element van reeds gesorteerde zone; bij i = 2 is gesorteerde zone = index 0 en 1 dus k = 1 
        while k >= 0 and lst[k] > currentElement: #zolang het element links groter is dan currentElement 
            lst[k + 1] = lst[k]                    # schuif element op index k één plaats naar rechts
            k -= 1                                 # ga met je vinger één plaats naar links
  
        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement #als k dus niet groter was dan current element dan wordt k + 1 current element en gaan we verder in de for lus naar de volgende i 
                                    #daar “valt” het element op de juiste plek in het gesorteerde stuk, je zou denken opening zit op index k want je hebt die inhoud ervan naar k + 1 gekopieerd maar je hebt hierna ook de index van k met 1 verlaagt dus daarom k + 1 = currentelement
def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    insertionSort(list)
    for v in list:
        print(v, end = " ")

main()
