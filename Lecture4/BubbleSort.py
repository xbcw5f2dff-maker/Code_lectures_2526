def bubbleSort(lst):
    needNextPass = True #Bij de start van de sortering weten we nog niet of de lijst gesorteerd is, we nemen dus aan dat er sws 1 pass nodig is dus True
    
    k = 1
    while k < len(lst) and needNextPass: #als k<len(lst) en needNextPass is true (in begin sws true want dat staat hierboven) dan ga je de lus binnen 
        # List may be sorted and next pass not needed
        needNextPass = False #na de controle of je de while-lus binnen gaat zet je need next pass op false => als je de for loop binnen gaat en de if loop (dus je swapt) ,dan zal het terug op Tue gezet worden en doorloop je het proces opnieuw, anders niet => lijst is al gesorteerd dus geen nood aan andere pass
        for i in range(len(lst) - k): #-k omdat die op het einde al goed staan, lijst wordt dus kleiner en kleiner: na elke pass staat het grootste element volledig vn achter, na 2de pass, staat 2de grootste op voorlaatste plaats 
            if lst[i] > lst[i + 1]: #als je getal groter is dan het volgende dan wisselen;
                # swap lst[i] with lst[i + 1]
                temp = lst[i]           #linkse getal steek ik in doosje 
                lst[i] = lst[i + 1]     #op de plaats van het linske getal zet ik nu het rechtse getal
                lst[i + 1] = temp       #op plaats van rechtse getal zet ik dan het linske getal dat in het doosje zat 
          
                needNextPass = True # Next pass still needed dus terug naar while-lus

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")

main()
