#hoofdfunctie
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1) #quicksort werkt op een deel ve lijst (subarray) dus de helperfunctie heeft grenzen nodig first=0, last=len(lst)-1

#recursieve helper
def quickSortHelper(lst, first, last):
    if last > first: #als last == first dan subdeel maar 1 element dus al gesorteerd en als last < first dan is het leeg dus ook gesorteerd , het zijn INDEXEN daarom dat dit zo werkt 
        pivotIndex = partition(lst, first, last) #dit zet pivot op de juiste plaats in het subarray en zorgt dat alles links ervan kleiner of gelijk is en alles rechts ervan groter is dan de pivot 
        quickSortHelper(lst, first, pivotIndex - 1) #sorteer alles links van de pivot 
        quickSortHelper(lst, pivotIndex + 1, last) #sorteer alles rechts van de pivot 

# Partition lst[first..last] 
def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot; dus zoals in de videosimulatie: eerste element = pivot 
    low = first + 1  # Index for forward search; low start rechts naast de pivot 
    high = last  # Index for backward search; high start op laatste plaats 

    while high > low: #zolang ze elkaar niet kruisen voer dan volgende uit;
        # Search forward from left
        while low <= high and lst[low] <= pivot: #deze while stopt als we een element vinden dat groter is dan de pivot of als we high voorbijgaan
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot: #deze while stopt als we een element vinden dat <= pivot of als we low voorbijgaan
            high -= 1

        # Swap two elements in the list
        if high > low: #wanneer we in vorige 2 whiles iets gevonden hebben dan swappen we low en high 
            lst[high], lst[low] = lst[low], lst[high]

   #wanneer low en high elkaar kruisen;
    while high > first and lst[high] >= pivot:  #high schuift naar links tot hij op een element komt dat kleiner is dan de pivpt => dit is de plek waar de pivot moet staan
        high -= 1                               #=> We willen pivot op de laatste positie links waar lst[high] < pivot
                                                #  (= laatste element in de “linker groep”).   => zie video 4min30s

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        # We hebben een echte kleinere waarde gevonden -> pivot moet naar 'high'
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        # pivot is al de kleinste, hij blijft gewoon op zijn plaats
        return first

# A test function 
def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    quickSort(lst)
    for v in lst:
        print(v, end = " ")

main()
