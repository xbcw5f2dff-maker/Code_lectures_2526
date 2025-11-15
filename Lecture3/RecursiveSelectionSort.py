#hoofdfunctie 
def sort(lst):
    sortHelper(lst, 0, len(lst) - 1) # Sort the entire lst (vn index O tot de laatste de lijst sorteren)

#recursieve functie 
def sortHelper(lst, low, high):
    if low < high: #als low == high dan stopt de functie (stopconditie)
        # Find the smallest number and its index in lst[low .. high]
        indexOfMin = low; #je zegt dat min op low staat 
        min = lst[low]; #je zegt dat het minimum dat je tot nu toe kent het getal op low is 
        for i in range(low + 1, high + 1): #eerste laat je weg en laatste wil je er wel bij => range(a, b) gaat van a tot b-1 
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i

        # Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low]
        lst[low] = min

        # Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high)

def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)

main()
