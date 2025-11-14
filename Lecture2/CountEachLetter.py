def main():
    filename = input("Enter a filename: ").strip() #.strip() verwijdert spaties of enters aan begin/einde 
    inputFile = open(filename, "r") # Open the file dat gebruiker heeft ingevoerd 

    counts = 26 * [0] # Create and initialize counts dit maakt een lijst van 26 nullen; [0, 0, 0, ..., 0] elke positite stelt letter voor; index 0 => letter 'a',...
    for line in inputFile: #leest lijn per lijn 
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts) # A en a zullen als 2 verschillende letters gezien worden dus .lower() om allemaal kleine letters te maken, er wordt dan geteld hvl keer elke letter voorkomt en de lijst met nullen wordt dan aangepast daarom counts ook argument 
    
    # Display results staat eig beter vanonder en def countletters hier 
    for i in range(len(counts)):
        if counts[i] != 0: #als waarde in de lijst niet 0 is dan;
            print(chr(ord('a') + i) + " appears " + str(counts[i]) # om van index trg naar letter te gaan ch(ord('a') + i) bv; i = 0 → ord('a') + 0 → 97 → chr(97) = 'a'
              + (" time" if counts[i] == 1 else " times"))                                                                    #of; i = 1 → chr(98) = 'b'

    inputFile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha(): # Test if ch is a letter
            counts[ord(ch) - ord('a')] += 1  #ord(ch) geeft ascii nummer vh karakter bv ord('a') = 97 , ord('c') = 99 
                                             #ord(ch) - ord('a') geeft de juiste index voor de counts bv ch = 'a' => 97 - 97 = 0 (index 0 in de lijst) dus dan verhoog je de teller op de juiste index ; += 1 
main() # Call the main function
