class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    
    def isWordIn(self, text):
        for p in string.punctuation:
            text = text.replace(p, ' ')
        text = text.lower().split()
        return self.word in text
    
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())