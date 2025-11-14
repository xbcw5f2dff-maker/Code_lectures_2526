from random import randint 

def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w")
    for i in range(10):
        outputFile.write(str(randint(0, 9)) + " ") #str(...) → maakt er een string van, want write() kan geen int schrijven, randint(0, 9) → genereert willekeurig getal van 0 t.e.m. 9, " " → spatie tussen de getallen
    outputFile.close() # Close the file , Na de lus staat er in het bestand bv.: 7 1 9 3 3 8 5 0 2 4, dan close om schrijven af te ronden 

    # Open file for reading data
    inputFile = open("Numbers.txt", "r") #bestand opnieuw openen om te lezen 
    s = inputFile.read() # Read all data to s, s wordt 1 grote string ; "7 1 9 3 3 8 5 0 2 4"
    numbers = [float(x) for x in s.split()] #string s wordt gesplitst in aparte strings en float zet elk element om naar getal [] maakt er lijst van
                #resultaat ; numbers = [7.0, 1.0, 9.0, 3.0, 3.0, 8.0, 5.0, 0.0, 2.0, 4.0]
    for number in numbers:   
        print(number, end = " ") #normaal zet print een enter op einde (nieuwe regel) maar end=" " zet een spatie in de plaats, resultaat ; 7.0 1.0 9.0 3.0 3.0 8.0 5.0 0.0 2.0 4.0 
    inputFile.close() # Close the file
    
main() # Call the main function
