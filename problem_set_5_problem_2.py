import string

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    best_score = None
    best_shift = None
    for shift in range(26):
        shifted_text = applyShift(text, shift).split(' ')
        score = 0
        for word in shifted_text:
            if isWord(wordList, word):
                score += 1
        if score > best_score:
            best_score = score
            best_shift = shift
    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    text = getStoryString()
    wordList = loadWords()
    best_shift = findBestShift(wordList, text)
    return applyShift(text, best_shift)
    '''
    Jack Florey is a mythical character created on the spur of a moment to help cove
    r an insufficiently planned hack. He has been registered for classes at MIT twic
    e before, but has reportedly never passed a class. It has been the tradition of 
    the residents of East Campus to become Jack Florey for a few nights each year to
     educate incoming students in the ways, means, and ethics of hacking.
    '''