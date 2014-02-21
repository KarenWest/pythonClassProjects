# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


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
    Returns a list of NewsStorys.
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

import functools
def JavaMonster(self, attribs, do=(getattr,)):
    for name, func in ('set%s', setattr), ('get%s', getattr):
        for attr in attribs:
            if func in do:
                setattr(self, name % attr.title(), functools.partial(func, self, attr))

def update_self(self, loc):
    self.__dict__.update((k,v) for k, v in loc.items() if k != 'self' and not k.startswith('_'))

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        update_self(self, locals())
        self.attribs = 'guid title subject summary link'.split()
        JavaMonster(self, self.attribs)

    def __iter__(self):
        """
        Iterate the content part of NewsStory
        """
        return iter((self.title, self.subject, self.summary))

    def __repr__(self):
        return 'NewsStory(%s, %r, %r, %r, %r)' % (self.guid, self.title, self.subject, self.summary, self.link)
    
##    get_guid, get_title, get_summary, get_link = getGuid, getTitle, getSummary, getLink
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

    def __str__(self):
        if hasattr(self, 'text'):
            text = 'with text %r' %  self.text
        else:
            text = '(%s)' % ', '.join(map(str, self.triggers))
        return ('%s trigger %s ' % (self.type, text)).rstrip()

    def __repr__(self):
        if hasattr(self, 'triggers'):
            self.text = ', '.join(map(repr, self.triggers))
            return '%sTrigger(%s)' % (self.type.title(), self.text)
        else:
            return '%sTrigger(%r)' % (self.type.title(), self.text)
        

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    type = 'WORD'
    def __init__(self, word):
        self.text = self.word = word

    def isWordIn(self, text):
        return any(word == self.word.lower()
                   for word in ''.join(' ' if c in string.punctuation
                                       else c.lower() for c in text).split())

class TitleTrigger(WordTrigger):
    type = 'TITLE'
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    type = 'SUBJECT'
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    type = 'SUMMARY'
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    type = 'NOT'
    def __init__(self, *triggers):
        self.triggers = triggers
        
    def evaluate(self, story):
        return not self.triggers.evaluate(story)
    
class AndTrigger(Trigger):
    type = 'AND'
    def __init__(self, *triggers):
        self.triggers = triggers
        
    def evaluate(self, story):
        return all(trigger.evaluate(story) for trigger in self.triggers)
    
class OrTrigger(Trigger):
    type = 'OR'
    def __init__(self, *triggers):
        self.triggers = triggers
        
    def evaluate(self, story):
        return any(trigger.evaluate(story) for trigger in self.triggers)
    
class PhraseTrigger(Trigger):
    type = 'PHRASE'
    def __init__(self, text):
        self.text = text

    def evaluate(self, story):
        return any(self.text in text for text in story) # without iterator defined: (story.title, story.summary, story.subject))


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: only the stories for which a trigger in triggerlist fires.
    """
    return list(story for story in stories if any(trigger.evaluate(story) for trigger in triggerlist))


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

    Returns: made triggerMap value
    """
    if triggerType in {'AND', 'OR', 'NOT'}:
        params = [triggerMap[par] for par in params]
    elif triggerType == 'PHRASE':
        params = [' '.join(params)]
    triggerMap[name] = eval("%sTrigger(*params)" % triggerType.title())
    #print triggerMap[name]
    return triggerMap[name]
    

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    with  open(filename) as triggerfile:
        lines = [unicode(line.rstrip(), 'latin1')
                 for line in triggerfile if line.strip() and line[0] != '#']
    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:
        linesplit = line.split(" ")#, 2) if "PHRASE"  in line else line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            print makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])
    return triggers
    
import thread
import ScrolledText
SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    try:
        triggerlist = readTriggerConfig("triggers.txt")      

        # from here is about drawing
        t = "My RSS News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = ScrolledText.ScrolledText(master, font=("Helvetica",14))
        cont.pack(side=LEFT)
        cont.tag_config("title", justify='center')
        cont.tag_config('body', wrap = 'word')
        button = Button(root, text="Exit", command=root.destroy, font=("Helvetica", 18))
        button.pack(side=BOTTOM, padx=8, pady=8)
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, (80 * '-').join("\n\n"), "title")
                cont.insert(END, newstory.getSummary(), "body")
                cont.insert(END, (120 * '*').join("\n\n"), "title")
                guidShown.append(newstory.getGuid())


        while True:
            #print "Polling . . .",
            stories = [story for url in
                       # Get stories from Google's Top Stories RSS news feed
                       ("http://news.google.com/?output=rss",
                        # Get stories from Yahoo's Top Stories RSS news feed
                        "http://rss.news.yahoo.com/rss/topstories",
                        # Test Finnish source for non-Ascii characters
                       'http://yle.fi/uutiset/rss/uutiset.rss')
                       for story in process(url) ]
            
            map(get_cont, filterStories(stories, triggerlist))
            #print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()