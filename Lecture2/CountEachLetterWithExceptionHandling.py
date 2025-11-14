def main():
    while True: #oneindige while lus => blijft herhalen tot we zelf break zeggen 
        try:
            filename = input("Enter a filename: ").strip()
            inputFile = open(filename, "r") # Open the file
            break #dus als het bestand openen lukt dan stopt de while lus 
        except IOError: #als het mislukt om te openen dan springt het naar except 
            print("File " + filename + " does not exist. Try again") #dit wordt geprint en daarna wordt terug gesprongen naar begin van de while true dus opnieuw vragen voor bestand naam

    counts = 26 * [0] # Create and initialize counts, maak een lijst van 26 nullen voor elke letter
    for line in inputFile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0: #als waarde op index i 0 is dan printen we die niet (letter komt 0 keer voor)
            print(chr(ord('a') + i) + " appears " + str(counts[i]) #ord('a') geeft de ASCII code vd letter => ord('a') = 97, 97 + i geeft de ASCII code vn letter i chr(...) zet het terug om naar letter
              + (" time" if counts[i] == 1 else " times"))

    inputFile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha(): #als character een letter is dan ;neem je de ASCII code ervan en trek je er de ASCII code van 'a' af dan krijg je de positie vd letter (index) en doe je + 1 om count te verhogen
            counts[ord(ch) - ord('a')] += 1   

main()

