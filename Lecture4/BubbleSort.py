def bubbleSort(lst):
    needNextPass = True
    
    k = 1
    while k < len(lst) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(lst) - k): 
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                temp = lst[i]           #linkse getal steek ik in doosje 
                lst[i] = lst[i + 1]     #op de plaats van het linske getal zet ik nu het rechtse getal
                lst[i + 1] = temp       #op plaats van rechtse getal zet ik dan het linske getal dat in het doosje zat 
          
                needNextPass = True # Next pass still needed

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")

main()
