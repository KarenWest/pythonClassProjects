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

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def evaluate(self, story):
        test_subject = self.phrase in story.getSubject()
        test_title = self.phrase in story.getTitle()
        test_summary = self.phrase in story.getSummary()
        return test_subject or test_title or test_summary

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    result = []
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                result.append(s)
                break
    return result