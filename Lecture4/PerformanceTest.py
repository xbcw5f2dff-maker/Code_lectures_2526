import time
#Deze code meet hoelang het duurt om een heel simpele lus (for-lus) uit te voeren voor verschillende groottes van n.
def getTime(n):
    startTime = time.time()    #tijd noteren wnr we starten
    k = 0                      #variabele die we telkens optellen
    for i in range(n):         #we doen dit n keer 
        k = k + 5 #simpele bewerking zodat er iets gebeurt, je wilt gwn weten hoelang het duurt om een bewerking n keer uit te voeren, kon bv evengoed k+1 zijn; een kleine bewerking die de computer verplicht om iets te doen 
    endTime = time.time()      #tijd na afloop noteren                                     
    print("Execution time for n =", n, "is",
        endTime - startTime, "seconds")

def main():
    getTime(10000)
    getTime(100000)
    getTime(1000000)
    getTime(10000000)

main()
