from string import ascii_lowercase as lower, ascii_uppercase as upper, ascii_letters as both

 

# 1. Build a coder

def buildCoder(shift):

return dict(zip(both, (lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])))

 

# 2. Apply the coder

def applyCoder(text, coder):

return "".join([coder.get(letter, letter) for letter in text])

 

# 3. Apply a shift

def applyShift(text, shift):

return applyCoder(text, buildCoder(shift))

 

# 4. Find the best shift for given text

def findBestShift(wordList, text):

words = text.split(" ")

for shift in range(26):

coder = buildCoder(shift)

if sum(isWord(wordList, applyCoder(word, coder)) for word in words) > len(words) / 2:

return shift

return False

 

# 5. Decrypt the provided story

def decryptStory():

return applyShift(story, findBestShift(loadWords(), getStoryString()))

 

# 6. Recursively reverse a string

def reverseString(aStr):

return aStr[-1] + reverseString(aStr[:-1]) if len(aStr) > 0 else ""

 

# 7. Determine whether a word is X-ian

def x_ian(x, word):

if len(x) == 0:

return True

else:

split = word.find(x[0])

return False if split == -1 else x_ian(x[1:], word[split + 1:])

 

# 8. Add typewriter-style line breaks

def insertNewlines(text, lineLength):

split = text.find(" ", lineLength - 1)

if split == -1:

return text

else:

return text[:split] + "\n" + insertNewlines(text[split:], lineLength)
