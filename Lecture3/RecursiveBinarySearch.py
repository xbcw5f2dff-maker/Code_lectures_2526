#hoofdfunctie, deze wordt als laatste opgesteld als mantel eromheen, deze roept gwn de hulpfunctie (recursive function) op met juiste start waarden 
def recursiveBinarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return recursiveBinarySearchHelper(lst, key, low, high)

#recursieve functie, deze wordt eerst opgesteld 
def recursiveBinarySearchHelper(lst, key, low, high):
    if low > high:  # The list has been exhausted without a match, stopconditie 
        return -low - 1
#als low < high dan volgende uitvoeren;
    mid = (low + high) // 2 
    if key < lst[mid]:
        return recursiveBinarySearchHelper(lst, key, low, mid - 1) #als je doelwaarde < waarde midden dan roep je opnieuw de functie aan waarbij high nu midden - 1 is 
    elif key == lst[mid]:
        return mid
    else:
        return recursiveBinarySearchHelper(lst, key, mid + 1, high) #zelfde uitleg 

def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursiveBinarySearch(lst, 3))
    print(recursiveBinarySearch(lst, 4))

main()
