# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *

#" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"" --all but the numerics below
PUNCTUATION_NUMERICS_SPACE = " " + string.punctuation + "0123456789"
PUNCTUATION_ONLY = string.punctuation

#-----------------------------------------------------------------------
#
# Problem Set 6

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

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
        self.word = word.lower()
        #print "Word Trigger " + self.word
        
    def isWordIn(self, text):
        textList = []
        """returns True if whole word present in text, False otherwise.
           not case-sensitive - text is a string.
        """
        #print "text " + text
        text = text.lower()
        #print "text lower case " + text
        for punctuationMark in PUNCTUATION_ONLY:
            text = text.replace(punctuationMark, " ")
        #print "text with punctuation replaced by spaces " + text
        textList = text.split(" ")
        #for text in textList:
            #print " text word " + text
        #print "word " + self.word.lower()
        return self.word.lower() in textList

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
# TitleTrigger inherits from WordTrigger that inherits from Trigger
    def evaluate(self, story):
        return self.isWordIn(story.title)

# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
# SubjectTrigger inherits from WordTrigger that inherits from Trigger
    def evaluate(self, story):
        return self.isWordIn(story.subject)

# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
# SummaryTrigger inherits from WordTrigger that inherits from Trigger
    def evaluate(self, story):
        #print "summary trigger "
        #print self.isWordIn(story.summary)
        return self.isWordIn(story.summary)

# Composite Triggers
# Problems 6-8
# TODO: NotTrigger
class NotTrigger(Trigger):
    triggerNewsItem = 0
    def __init__(self, trigNewsItem):
        self.triggerNewsItem = trigNewsItem

    def evaluate(self, newsItem):
        return not self.triggerNewsItem.evaluate(newsItem)

# TODO: AndTrigger
class AndTrigger(Trigger):
    triggerNewsItem1 = 0
    triggerNewsItem2 = 0
    def __init__(self, trigNewsItem1, trigNewsItem2):
        self.triggerNewsItem1 = trigNewsItem1
        self.triggerNewsItem2 = trigNewsItem2

    def evaluate(self, newsItem):
        return self.triggerNewsItem1.evaluate(newsItem) and self.triggerNewsItem2.evaluate(newsItem)

# TODO: OrTrigger
class OrTrigger(Trigger):
    triggerNewsItem1 = 0
    triggerNewsItem2 = 0
    def __init__(self, trigNewsItem1, trigNewsItem2):
        self.triggerNewsItem1 = trigNewsItem1
        self.triggerNewsItem2 = trigNewsItem2

    def evaluate(self, newsItem):
        #print "or trigger 1"
        #print self.triggerNewsItem1.evaluate(newsItem)
        #print "or trigger 2"
        #print self.triggerNewsItem2.evaluate(newsItem)
        return self.triggerNewsItem1.evaluate(newsItem) or self.triggerNewsItem2.evaluate(newsItem)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger -- given phrase, fires if given phrase is in any of the
# story's title, subject or summary
class PhraseTrigger(Trigger):
    phrase = ""

    def __init__(self, phrase):
        self.phrase = phrase
        #print "phrase " + phrase

    def evaluate(self, story):
        titleTrigger = False
        subjectTrigger = False
        summaryTrigger = False
        if (len(story.title) != 0):
            #print "phrase " + self.phrase + " story title " + story.title
            if (self.phrase in story.title):
                titleTrigger = True
        if (len(story.subject) != 0):
            #print "phrase " + self.phrase + " story subject " + story.subject
            if (self.phrase in story.subject):
                subjectTrigger = True
        if (len(story.summary) != 0):
            #print "phrase " + self.phrase + " story summary " + story.summary
            if (self.phrase in story.summary):
                summaryTrigger = True
        return titleTrigger or subjectTrigger or summaryTrigger

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances and a triggerList.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    trigStoryList = []
    for story in stories:
        for trigger in triggerlist:
            if (trigger.evaluate(story)):
                trigStoryList.append(story)
    return trigStoryList

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns: None
    """
    # TODO: Problem 11
    ''' trigger types:
    title trigger - one word parameter
    subject trigger - one word parameter
    summary trigger - one word parameter
    not trigger - trigger name parameter
    and trigger - 2 trigger name parameters
    or trigger - 2 trigger name parameters
    phrase trigger - a phrase string parameter
    '''
    if (triggerType == "TITLE"):
        #print "Title Trigger " + " param " + params[0]
        trigger = TitleTrigger(params[0])
    elif (triggerType == "SUBJECT"):
        #print "Subject Trigger " + " param " + params[0]
        trigger = SubjectTrigger(params[0])
    elif (triggerType == "SUMMARY"):
        #print "Summary Trigger " + " param " + params[0]
        trigger = SummaryTrigger(params[0])
    elif (triggerType == "NOT"):
        #print "Not Trigger "
        if (params[0] in triggerMap):
            trigger = NotTrigger(triggerMap[params[0]])
        else:
            trigger = NotTrigger(params[0])
    elif (triggerType == "AND"):
        if (params[0] in triggerMap) and (params[1] in triggerMap):
        #print "And Trigger " + " param 0 " + params[0] + " param 1 " + params[1]
            trigger = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
        elif (params[0] not in triggerMap) and (params[1] in triggerMap):
            trigger = AndTrigger(params[0], triggerMap[params[1]])
        elif (params[0] in triggerMap) and (params[1] not in triggerMap):
            trigger = AndTrigger(triggerMap[params[0]], params[1])
        else:
            trigger = AndTrigger(params[0], params[1])
    elif (triggerType == "OR"):
        #print "Or Trigger " + " param 0 " + params[0] + " param 1 " + params[1]
        if (params[0] in triggerMap) and (params[1] in triggerMap):
            trigger = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        elif (params[0] not in triggerMap) and (params[1] in triggerMap):
            trigger = OrTrigger(params[0], triggerMap[params[1]])
        elif (params[0] in triggerMap) and (params[1] not in triggerMap):
            trigger = OrTrigger(triggerMap[params[0]], params[1])
        else:
            trigger = OrTrigger(params[0], params[1])
    elif (triggerType == "PHRASE"):
        paramsStr = ' '.join(params) #puts list of chars in str
        #print "Phrase Trigger " + " param " + paramsStr
        trigger = PhraseTrigger(paramsStr)
    triggerMap[name] = trigger
    return trigger

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        #triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # from here is about drawing
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_summary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()
'''
#Trigger 1:
    pt = PhraseTrigger("Neil deGrasse Tyson")
#Trigger 2:
    ot = OrTrigger(SummaryTrigger("Mars"), SummaryTrigger("Venus"))
    trigList = [pt, ot]
#Story with title:
    story = NewsStory(" ", "Planetarium Popular","Strangely, children enjoy learning","Astrophysicist Neil deGrasse Tyson brings in new visitors to NYC museum", " ")
    storyList = [story]
    filteredStories = filterStories(storyList, trigList)
    lenFilteredStory = len(filteredStories)
    if (len(filteredStories) != 0):
        print filteredStories[0].title
        print filteredStories[0].subject
        print filteredStories[0].summary
'''
