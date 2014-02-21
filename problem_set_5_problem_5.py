def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    index = text.find(' ', lineLength - 1)
    if index == -1:
        return text
    temp_text = text[:index + 1] + '\n'
    return temp_text + insertNewlines(text[index + 1:], lineLength)
#    --------
    def insertNewlinesRec(text, lineLength, count):
        if len(text) < lineLength:
            return text
        if count >= (lineLength - 1) and text[count] == ' ':
            return '\n' + insertNewlinesRec(text[count + 1:], lineLength, 0)
        return text[count] + insertNewlinesRec(text, lineLength, count + 1)
    return insertNewlinesRec(text, lineLength, 0)
#    --------
    if len(text) <= lineLength:
        return text
    if text[lineLength - 1] == ' ':
        temp_text = text[:lineLength - 1] + '\n'
        return temp_text + insertNewlines(text[lineLength:], lineLength)
    return text[0] + insertNewlines(text[1:], lineLength)