print('Question 9\n')

def freqCount(text):
    freq = {}
    collection = text.lower().split()
    for word in collection:
        word = word.strip('.,!?":;')
        freq[word] = freq.get(word, 0) + 1
    return freq

paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, " \
"it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, " \
"it was the spring of hope, it was the winter of despair."
print('Paragraph: It was the best of times, it was the worst of times, it was the age of wisdom, ' \
'it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, ' \
'it was the spring of hope, it was the winter of despair.\n')
print('Frequency Counter: '+ str(freqCount(paragraph)))

print('\nQuestion 10\n')

def charCounter(text):
    counter = {}
    for char in text: 
        counter[char] = counter.get(char, 0) + 1
    return counter

print('Characters counted in [My name is Rayhaan Mohamed]: '+str(charCounter("My name is Rayhaan Mohamed")))

print('\nQuestion 11\n')

def gradebook():
    students = {
        "Sam": 82,
        "Connor": 90,
        "Arib": 77,
        "Sarah": 86,
        "Ray": 88,
        "Jobn": 95,
        "Homer": 74
    }
    return students

def queryGradebook(gradebook, name):
    return gradebook.get(name, "No results found")

discover = gradebook()
print('Ray: ' + str(queryGradebook(discover, "Ray")))
print('Deji: ' + str(queryGradebook(discover, "Deji")))