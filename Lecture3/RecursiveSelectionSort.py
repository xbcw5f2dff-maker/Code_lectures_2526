e#hoofdfunctie 
def sort(lst):
    sortHelper(lst, 0, len(lst) - 1) # Sort the entire lst (vn index O tot de laatste de lijst sorteren)

#recursieve functie 
def sortHelper(lst, low, high):
    if low < high: #als low == high dan stopt de functie (stopconditie)
        # Find the smallest number and its index in lst[low .. high]
        indexOfMin = low; #je zegt dat min op low staat 
        min = lst[low]; #je zegt dat het eerste element tot nu toe het kleinste is (min), je doet deze en vorige lijn gwn om startpunt te hebben 
        for i in range(low + 1, high + 1): #eerste laat je weg en laatste wil je er wel bij => range(a, b) gaat van a tot b-1 
            if lst[i] < min:
                min = lst[i] #je zegt oke getal op i is kleiner dat het oude min dus is nieuwe min 
                indexOfMin = i #index van dat getal i 

        # Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low] #dat getal dat nu min is verander je door getal dat op low stond 
        lst[low] = min #getal op low verander je door dat getal dat min is 

        # Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high)

def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)

main()
