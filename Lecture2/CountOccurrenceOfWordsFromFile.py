def main():
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    inputFile = open(filename, "r") # Open the file

    wordCounts = {} # Create an empty dictionary to count words
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close() 
    
    pairs = list(wordCounts.items()) # Get pairs from the dictionary, wordcounts.items() geeft de (key, value)-paren als tuples, list() om lijst vn te maken vande paren tuples 

    items = [[x, y] for (y, x) in pairs] # Reverse pairs in the list, want het begint met woord en dan aantal en lijsten worden gesorteerd obv 1ste element vh paar, en we willen op aantal sorteren ipv op woord
    #resultaat; [aantal, woord] lijstenwat
    items.sort() # Sort pairs in items

    for i in range(len(items) - 1, 0, -1): #start bij laatste index (de grootste) eindig net boven 0
        print(items[i][1] + "\t" + str(items[i][0])) #items[i][1] => woord, items[i][0] => aantal en backslash t is tab
                                                     #items[i][0] => 1ste element vd lijst => aantal
                                                     #items[i][1] => 2 de element vd lijst => woord 
# Count each word in the line
def processLine(line, wordCounts): 
    line = replacePunctuations(line) # Replace punctuations with space
    words = line.split() # Get words from each line, splitst woorden op spaties => resultaat is lijst van worden => .split() geeft ALTIJD lijst terug
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1 #als woord al bestaat => teller + 1
        else:
            wordCounts[word] = 1 #anders => eerste keer gezien => teller = 1

# Replace punctuations in the line with space
def replacePunctuations(line): #elke letter ch controleren als het een leesteken is vervangen door spatie 
    for ch in line:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            line = line.replace(ch, " ")

    return line

main()
