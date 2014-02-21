#======================
# Part 1
# Data structure design
#======================
import string
PUNCTUATION_ONLY = string.punctuation
# Problem 1

# TODO: NewsStory
class NewsStory(object):
    guid = ""
    title = ""
    subject = ""
    summary = ""
    link = ""
    def __init__(self, guid, title, subject, summary, link):
        """creat NewsStory with these parameters"""
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        """return self's guid from the news story"""
        return self.guid

    def getTitle(self):
        """return self's title from the news story"""
        return self.title

    def getSubject(self):
        """return self's subject from the news story"""
        return self.subject

    def getSummary(self):
        """return self's summary from the news story"""
        return self.summary

    def getLink(self):
        """return self's link from the news story"""
        return self.link

guidTest1 = "koalaGuid"
guidTest2 = "pillowsGuid"
guidTest3 = "softDrinksGuid"
guidTest4 = "softNewPinkGuid"
guidTest5 = "softFootballsGuid"
guidTest6 = "MicrosoftBadPillowsGuid"
guidTest7 = "ReutersBoringGuid"
guidTest8 = "softThingsSoftGuid"

titleTest1 = "koala title"
titleTest2 = "pillows title"
titleTest3 = "soft drinks title"
titleTest4 = "soft is new pink title"
titleTest5 = "soft footballs title"
titleTest6 = "Microsoft's announcement about bad pillows title"
titleTest7 = "Reuters report boring title"
titleTest8 = "soft things soft title"

subjectTest1 = "koala subject"
subjectTest2 = "pillows subject"
subjectTest3 = "soft drinks subject"
subjectTest4 = "soft is new pink subject"
subjectTest5 = "soft footballs subject"
subjectTest6 = "Microsoft's announcement about bad pillows subject"
subjectTest7 = "Reuters report boring subject"
subjectTest8 = "soft things soft subject"

summaryTest1 = 'Koala bears are soft and cuddly'
summaryTest2 = 'I prefer pillows that are soft.'
summaryTest3 = 'Soft drinks are great'
summaryTest4 = "Soft's the new pink!"
summaryTest5 = '"Soft!" he exclaimed as he threw the football'
summaryTest6 = 'Microsoft announced today that pillows are bad'
summaryTest7 = 'Reuters reports something really boring'
summaryTest8 = 'soft things are soft'

linkTest1 = "www.koalas.com"
linkTest2 = "www.pillows.com"
linkTest3 = "www.softDrinks.com"
linkTest4 = "www.softNewPink.com"
linkTest5 = "www.softFootballs.com"
linkTest6 = "www.MicrosoftBadPillows.com"
linkTest7 = "www.ReutersBoring.com"
linkTest8 = "www.softThingsSoft.com"

test1 = NewsStory(guidTest1, titleTest1, subjectTest1, summaryTest1, linkTest1)
test2 = NewsStory(guidTest2, titleTest2, subjectTest2, summaryTest2, linkTest2)
test3 = NewsStory(guidTest3, titleTest3, subjectTest3, summaryTest3, linkTest3)
test4 = NewsStory(guidTest4, titleTest4, subjectTest4, summaryTest4, linkTest4)
test5 = NewsStory(guidTest5, titleTest5, subjectTest5, summaryTest5, linkTest5)
test6 = NewsStory(guidTest6, titleTest6, subjectTest6, summaryTest6, linkTest6)
test7 = NewsStory(guidTest7, titleTest7, subjectTest7, summaryTest7, linkTest7)
test8 = NewsStory(guidTest8, titleTest8, subjectTest8, summaryTest8, linkTest8)

testSuiteNewsStory = [test1, test2, test3, test4, test5, test6, test7, test8]
'''
numTests = len(testSuiteNewsStory)
i = 1
print "Number of tests for NewsStory class = " + str(numTests)
for test in testSuiteNewsStory:
    print "test " + str(i) + " : "
    print ""
    print test.getGuid()
    print test.getTitle()
    print test.getSubject()
    print test.getSummary()
    print test.getLink()
    print ""
    i += 1
'''
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger): #WordTrigger is a subclass of Trigger
    word = ""
    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        textList = []
        """returns True if whole word present in text, False otherwise.
           not case-sensitive - text is a string.
        """
#        print "text " + text
        text = text.lower()
#        print "text lower case " + text
        for punctuationMark in PUNCTUATION_ONLY:
            text = text.replace(punctuationMark, " ")
#        print "text with punctuation replaced by spaces " + text
        textList = text.split(" ")
#        for text in textList:
#            print " text word " + text
#       print "word " + self.word
        return self.word in textList
    
# TODO: TitleTrigger
class TitleTrigger(WordTrigger, NewsStory):
# TitleTrigger inherits from WordTrigger that inherits from Trigger
    def __init__(self, word):
        self.word = word
        
    def evaluate(self, story):
        return self.isWordIn(self.title)

#Test WordTriggers
titleTests = [titleTest1, titleTest2, titleTest3, titleTest4, titleTest5, titleTest6, titleTest7, titleTest8]
wordList = ["soft", "koala", "pillows", "drinks", "pink", "footballs", "Microsoft", "Reuters", "Things", "Nothing"]

'''
wordTrigSoft = WordTrigger("soft")
wordTrigKoala = WordTrigger("koala")
wordTrigPillows = WordTrigger("pillows")
wordTrigDrinks = WordTrigger("drinks")
wordTrigPink = WordTrigger("pink")
wordTrigFootballs = WordTrigger("footballs")
wordTrigMicrosoft = WordTrigger("Microsoft")
wordTrigReuters = WordTrigger("Reuters")
wordTrigThings = WordTrigger("Things")
wordTrigNothing = WordTrigger("Nothing")
wordTrigList = [wordTrigSoft, wordTrigKoala, wordTrigPillows, wordTrigDrinks, wordTrigPink, wordTrigFootballs, wordTrigMicrosoft, wordTrigReuters, wordTrigThings, wordTrigNothing]
i = 0
for trigger in wordTrigList:
    for title in titleTests:
        print "is word " + wordList[i] + " in title " + title + " for WordTrigger " + trigger.word
        print trigger.isWordIn(title)
    i += 1
'''
#Test TitleTriggers--this time with NewsStory objects passed to trigger instead of a text string
titleTriggerList = []
for newsStoryTest in testSuiteNewsStory:
    titleTriggerList.append(TitleTrigger(newsStoryTest))
    print "Appended News Story title " + newsStoryTest.title + " to titleTriggersList"
    
i = 0
for trigNewsStory in titleTriggerList:
    print "is word " + wordList[i] + " in trigger for TitleTrigger " + trigNewsStory.title
    print trigNewsStory.evaluate(trigNewsStory)
    i += 1
