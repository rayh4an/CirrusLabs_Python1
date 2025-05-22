import string
print('Question 5\n')

def anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "".lower()))
print('Are [secure] and [rescue] anagrams?')
print(anagram("secure", "rescue"))
print('Are [day] and [night] anagrams?')
print(anagram("day", "night"))

print('\nQuestion 6\n')

def strongPassword(password):
    upperCase = any(char.isupper() for char in password)
    lowerCase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    specialChar = any(char in string.punctuation for char in password)

    return upperCase and lowerCase and digit and specialChar and len(password) >= 12

print('Is ChickenNumber9* a strong password?')
print(strongPassword("ChickenNumber9*"))
print('Is Harpy74 a strong password?')
print(strongPassword("Harpy74"))

print('\nQuestion 7\n')

def longWordFinder(sentence):
    words=sentence.split()
    longest = max(words, key=len)
    return longest

print('I went outside and saw many birds, but one bird in particular was enormous.')
print('The longest word in the sentence above is: ' + str(longWordFinder("I went outside and saw many birds, but one bird in particular was enormous.")))

print('\nQuestion 8\n')

def listFlatten(nested):
    flat= []
    for value in nested:
        if isinstance(value, list):
            flat.extend(listFlatten(value))
        else:
            flat.append(value)
    return flat

print('When this list is flattened, [1, 63, [87], [90, 22], [2], 43], it becomes ' + str(listFlatten([1, 63, [87], [90, 22], [2], 43])))