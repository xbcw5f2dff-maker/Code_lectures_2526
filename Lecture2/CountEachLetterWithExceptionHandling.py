def main():
    while True: #oneindige while lus => blijft herhalen tot we zelf break zeggen 
        try:
            filename = input("Enter a filename: ").strip()
            inputFile = open(filename, "r") # Open the file
            break #dus als het bestand openen lukt dan stopt de while lus 
        except IOError: #als het mislukt om te openen dan springt het naar except 
            print("File " + filename + " does not exist. Try again") #dit wordt geprint en daarna wordt terug gesprongen naar begin van de while true dus opnieuw vragen voor bestand naam

    counts = 26 * [0] # Create and initialize counts
    for line in inputFile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i])
              + (" time" if counts[i] == 1 else " times"))

    inputFile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main()

