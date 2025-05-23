from datetime import datetime
import csv

print('Question 12\n')

def readCount(filename):
    try:
        with open(filename, 'r') as file:
            lineNum = file.readlines()
            countLine = len(lineNum)
            countWord = sum(len(line.split()) for line in lineNum)
            countChar = sum(len(line) for line in lineNum)

        return {
            "Line Count: ": countLine,
            "Word Count: ": countWord,
            "Character Count": countChar
        }
    
    except FileNotFoundError:
        return "file is unavailable"

print('Paragraph: It was the best of times, it was the worst of times, it was the age of wisdom, ' \
'it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, ' \
'it was the spring of hope, it was the winter of despair.\n')
print('Txt file analyzed: ' + str(readCount("question12.txt")))

print('\nQuestion 13\n')

def logWriter():
    with open("question13.txt", 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Script run at: {timestamp}\n")

logWriter()
print('Check the [question13.txt] file for confirmation.')

print('\nQuestion 14\n')

def csvReader(filename):
    try:
        with open(filename, 'r') as file:
            read = csv.DictReader(file)
            for row in read:
                if float(row['grades']) > 75:
                    print(row['name'])
    
    except FileNotFoundError:
        return "file is unavailable"
    
csvReader("question14.csv")