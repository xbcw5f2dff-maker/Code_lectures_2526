def mergeSort(list):
    if len(list) > 1: # als lengte lijst 1 is dan is ze al gesorteerd 
        # Merge sort the first half
        firstHalf = list[ : len(list) // 2] #lijst in 2 delen en eerste deel nemen
        mergeSort(firstHalf)                #mergesort toepassen op eerste deel => deze lijst op zijn beurt ook weer in 2 delen gesplitst, en dan weer mergesort op 1 ste en 2 de helft totdat de lengte vd lijsten 1 is (want dan is ze al gesorteerd)

        # Merge sort the second half
        secondHalf = list[len(list) // 2 : ] #lijst in 2 deleen en tweede deel nemen 
        mergeSort(secondHalf)                #mergesort toepassen op tweede deel => idem

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, list)

# Merge two sorted lists */
def merge(list1, list2, temp): #list1 => linkerdeel (al gesorteerd), list2 => rechterdeel (al gesorteerd), temp => originele lijst waarin alles wordt samengevoegd 
    current1 = 0  # Current index in list1 => gwn bijhouden waar we zitten in welke lijst gwn bijhouden waar we zitten in welke lijst 
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2): #zolang er elementen zijn in zowel lijst 1 als lijst 2: 
        if list1[current1] < list2[current2]: #is element op die index uit lijst 1 < element op die index lijst 2:
            temp[current3] = list1[current1]  #dan ga je element uit lijst 1 toevoegen aan nieuwe lijst 
            current1 += 1 #index schuift 1
            current3 += 1 #index schuift 1
        else: #als element op die index lijst 2 kleinder is dan:                dus eig gwn kleinste vd 2 in nieuwe lijst zetten of ja in de originele lijst
            temp[current3] = list2[current2] 
            current2 += 1 #index schuift 1 
            current3 += 1 #index schuift 1  

    while current1 < len(list1): #als lijst 2 leeg is dan gooi je de rest van lijst 1 in originele lijst
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2): #als lijst 1 leeg is dan gooi je rest van lijst 2 in originele lijst 
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(list)
    for v in list:
        print(v, end = " ")

main()
 
