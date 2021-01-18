import os
import re

IGNOREWORDCASE = False
FOLDERPATH = "/Users/aaronwright/Downloads/TextFiles"

searchString = input("Please enter a word & hit return: ")

wordList = []
for (path, directories, files) in os.walk(FOLDERPATH, topdown=True):
    for file in files:
        filepath = os.path.join(path, file)
        with open(filepath, 'r') as currentfile:
            try:          
                for num, line in enumerate(currentfile, 1): 
                    line = line.strip()
                    match = re.search(searchString, line, re.IGNORECASE) if IGNOREWORDCASE else re.search(searchString, line)
                    if match:
                        word = f"Word '{searchString}' found in file '{file}' on line {num}: {line}"
                        wordList.append(word)
            except:
                words = f"ERROR - FILE NOT SCANNED: {file}"
                wordList.append(words)
  
for word in wordList:
    print(word)
    # Create Dataframe using Pandas, and save the DataFrame Values to a CSV
    #df = pd.DataFrame(data={"Results": wordList})
    #df.to_csv("./mycsv.csv", sep=",", index=False, line_terminator='\n')