'''
A Frob is an object that has a name, and two connections or links: a "before"
and an "after" link that are intended to point to other instances of objects.

We can use Frobs to form a data structure called a doubly linked list. In a
doubly linked list, each element has the property that if element A has a
"before" link to element B, then element B has an "after" link to element A.
We want to create a doubly linked collection of Frob instances with the property
that all Frobs with names that are alphabetically before a specific Frob's name
appear ordered along the "before" link, and all Frobs with names that are
alphabetically after a specific Frob's name appear ordered along the "after"
link. Here is an example:

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

Note that if a Frob is inserted with the same name as a pre-existing Frob, both
names should be inserted in the final data structure (the exact ordering of the
two identical Frobs does not matter). So in the above example, if we were to
next execute the line insert(eric, Frob('martha')), we would expect the doubly
linked list to have the elements in the following order:
andrew - eric - fred - martha - martha - ruth.

Provide a definition for an insert function that will create an ordered doubly
linked list. This function is defined outside of the class Frob, and takes two
arguments: a Frob that is currently part of a doubly linked list, and a new Frob.
The new Frob will not initially have any "before" or "after" links to other Frobs.
The function should mutate the list to place the new Frob in the correct location,
with the resulting doubly linked list having appropriate "before" and "after" links.
'''

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe
    is a part of.    
    """
    #atMe is a list already in alphabetical order
    nameList = []
    sortedNameList = []
    atMeName = atMe.myName()
    newFrobName = newFrob.myName()
#    print "atMeName " + atMeName + " new Frob Name " + newFrobName
    nameList.append(atMeName)
    nameList.append(newFrobName)
    sortedNameList = sorted(nameList)
#    print ""
#    print "sorted name list [0] " + sortedNameList[0]
#    print "sorted name list [1] " + sortedNameList[1]
#    print ""

    if (sortedNameList[0] == atMeName): #insert newFrob AFTER atMe, but check next Frob to see whether it comes after that too
#        print "insert new frob AFTER atME but check next Frob first"
        saveAfterLink = atMe.getAfter() #points to next Frob structure
        saveBeforeLink = atMe.getBefore() #points to previous Frob structure
        if (saveAfterLink == None) and (saveBeforeLink == None): #atMe is only frob in linked list-frob goes after it
#            print "atMe was the only frob in doubly linked list--putting new frob AFTER it"
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(None)  
        elif (saveAfterLink != None):
#            print "there is an after link for atMe"
            nextFrobStructLink = saveAfterLink.getAfter()
            nextFrobStructName = saveAfterLink.myName()
            nameList = []
            nameList.append(nextFrobStructName)
            nameList.append(newFrobName)
            sortedNameList = sorted(nameList)
            if (sortedNameList[0] == newFrobName): #insert new Frob immediately after atMe
#                print "new frob is immediately after atMe"
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
                newFrob.setAfter(saveAfterLink)
                saveAfterLink.setBefore(newFrob)
            else: #keep looking through each link until you find where it fits in the linked list
#                print "new frob does NOT come immediately after atMe - look further up links"
                stillLooking = True
                saveAfterLink = nextFrobStructLink
                while (stillLooking == True):
#                    print "still looking for where this new frob belongs in list"
                    nextnextFrobStructLink = saveAfterLink.getAfter() #point to next Frob structure
                    if (nextnextFrobStructLink != None): #more frobs follow this next frob
#                        print "more frobs follow this next frob"
                        saveAfterLink = nextnextFrobStructLink
                        nextnextFrobStructName = nextnextFrobStructLink.myName()
                        nameList = []
                        nameList.append(nextnextFrobStructName)
                        nameList.append(newFrobName)
                        sortedNameList = sorted(nameList)
                        if (sortedNameList[0] == newFrobName):
#                            print "frob belongs here before this next frob we checked"
                            saveBeforeLink = nextnextFrobStructLink.getBefore()
                            nextnextFrobStructLink.setBefore(newFrob)
                            newFrob.setAfter(nextnextFrobStructLink)
                            newFrob.setBefore(saveBeforeLink)
                            saveBeforeLink.setAfter(newFrob)
                            stillLooking = False
                    else: #no more frobs after this next frob
#                            print "frob belongs here before this next frob which is the LAST frob" 
                            saveBeforeLink = nextnextFrobStructLink.getBefore()
                            nextnextFrobStructLink.setBefore(newFrob)
                            newFrob.setAfter(nextnextFrobStructLink)
                            newFrob.setBefore(saveBeforeLink)
                            saveBeforeLink.setAfter(newFrob)
                            stillLooking = False
        else: #atMe has no after link but does have before link - put new frob here
#            print "new frob is immediately after atMe and atMe was last frob"
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(None)            
    else: #insert new Frob BEFORE atMe, but check next previous Frob to see whether it comes before that Frob too
#        print "insert new frob BEFORE atMe, but check next previous frob's first"
        saveAfterLink = atMe.getAfter() #points to next Frob structure
        saveBeforeLink = atMe.getBefore() #points to previous Frob structure
        if (saveAfterLink == None) and (saveBeforeLink == None): #atMe is only frob in linked list-frob goes after it
#            print "atMe is the only frob in doubly linked list--putting new frob BEFORE it"
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(None)  
        elif (saveBeforeLink != None):
#            print "there is a before link for atMe--check ones before this, if any"
            prevFrobStructLink = saveBeforeLink.getBefore()
            prevFrobStructName = saveBeforeLink.myName()
            nameList = []
            nameList.append(prevFrobStructName)
            nameList.append(newFrobName)
            sortedNameList = sorted(nameList)
            if (sortedNameList[0] != newFrobName): #insert new Frob immediately before atMe
#                print "insert new frob immediately before atMe"
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
                newFrob.setBefore(saveBeforeLink)
                saveBeforeLink.setAfter(newFrob)
            else: #keep looking through each link until you find where it fits in the linked list
#                print "look at before links before this atMe"
                stillLooking = True
                saveBeforeLink = prevFrobStructLink
                while (stillLooking == True):
#                    print "still looking at before links"
                    nextprevFrobStructLink = saveBeforeLink.getBefore() #point to next prev Frob structure
                    if (nextprevFrobStructLink != None): #there are more prev frob structs before this one
#                        print "previous frob before link has a frob"
                        saveBeforeLink = nextprevFrobStructLink
                        nextprevFrobStructName = nextprevFrobStructLink.myName()
                        nameList = []
                        nameList.append(nextprevFrobStructName)
                        nameList.append(newFrobName)
                        sortedNameList = sorted(nameList)
                        if (sortedNameList[0] != newFrobName):
#                            print "found where new frob belongs in before links"
                            saveAfterLink = nextprevFrobStructLink.getAfter()
                            nextprevFrobStructLink.setAfter(newFrob)
                            newFrob.setBefore(nextprevFrobStructLink)
                            newFrob.setAfter(saveAfterLink)
                            saveAfterLink.setAfter(newFrob)
                            stillLooking = False
                    else: #there are no more prev frob structs before this one
#                            print "found where new frob belongs and no more before links"
                            saveAfterLink = nextprevFrobStructLink.getAfter()
                            nextprevFrobStructLink.setAfter(newFrob)
                            newFrob.setBefore(nextprevFrobStructLink)
                            newFrob.setAfter(saveAfterLink)
                            saveAfterLink.setAfter(newFrob)
                            stillLooking = False
        else: #atMe has no before link but does have after link - put new frob before it
#            print "new frob is immediately before atMe and atMe was first frob"
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(None)            
 
def printDoubleList(anyFrob):
    stillPrinting = True
    print "Starting with Frob Name: " + str(anyFrob.myName())
    savePrevFrob = anyFrob
    saveNextFrob = anyFrob
    print "Print all frobs before this frob"
    while(stillPrinting == True):
        prevFrobLink = savePrevFrob.getBefore()
        if (prevFrobLink != None):
            print "next previous frob name " + str(prevFrobLink.myName())
            savePrevFrob = prevFrobLink
        else:
            print "no more previous frobs"
            stillPrinting = False
            
    print "Print all frobs after this frob"
    stillPrinting = True
    while(stillPrinting == True):
        nextFrobLink = saveNextFrob.getAfter()
        if (nextFrobLink != None):
            print "next frob name " + str(nextFrobLink.myName())
            saveNextFrob = nextFrobLink
        else:
            print "no more after frobs"
            stillPrinting = False

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
printDoubleList(andrew)
print ""
#print "eric before frob " + eric.getBefore().myName()
#print "andrew after frob " + andrew.getAfter().myName()
insert(eric, ruth)
printDoubleList(andrew)
print ""
print "andrew after frob " + andrew.getAfter().myName()
print "eric before frob " + eric.getBefore().myName()
print "eric after frob " + eric.getAfter().myName()
print "ruth before frob " + ruth.getBefore().myName()

insert(eric, fred)
printDoubleList(andrew)
print ""
print "andrew after frob " + andrew.getAfter().myName()
print "eric before frob " + eric.getBefore().myName()
print "eric after frob " + eric.getAfter().myName()
print "fred before frob " + fred.getBefore().myName()
print "fred after frob " + fred.getAfter().myName()
print "ruth before frob " + ruth.getBefore().myName()

print ""
#insert(eric, martha)
insert(ruth, martha)
printDoubleList(andrew)
print ""
print "andrew after frob " + andrew.getAfter().myName()
print "eric before frob " + eric.getBefore().myName()
print "eric after frob " + eric.getAfter().myName()
print "fred before frob " + fred.getBefore().myName()
print "fred after frob " + fred.getAfter().myName()
print "ruth before frob " + ruth.getBefore().myName()
print "martha before frob " + martha.getBefore().myName()
print "martha after frob " + martha.getAfter().myName()

#printDoubleList(eric)
#printDoubleList(fred)
#printDoubleList(martha)
#printDoubleList(ruth)

'''
insert() - test case results:
 INCORRECT --Test Case Output (posted after final exam due date-so can look later)
 (Also, there are correct solutions to do it more efficiently).
Test: 1A

Adding to the beginning: Adding 'allison' to the list ('gabby')

Output:

    Test: insert(Frob("gabby"), Frob("allison"))
    *** Walking the linked list forward: ***
    allison
    gabby

Test: 1B

Adding to the beginning: Adding 'allison' to the list ('gabby')

Output:

    Test: insert(Frob("gabby"), Frob("allison"))
    *** Walking the linked list backward: ***
    gabby
    allison

Test: 2A

Adding to the end: Adding 'zara' to the list ('gabby')

Output:

    Test: insert(Frob("gabby"), Frob("zara"))
    *** Walking the linked list forward: ***
    gabby
    zara

Test: 2B

Adding to the end: Adding 'zara' to the list ('gabby')

Output:

    Test: insert(Frob("gabby"), Frob("zara"))
    *** Walking the linked list backward: ***
    zara
    gabby

Test: 3A

Multiple names. test_list = Frob('abby')

Output:

    Test: insert(test_list, Frob("xander"))
    Test: insert(test_list, Frob("beto"))
    *** Walking the linked list forward: ***
    abby
    beto
    xander

Test: 3B

Multiple names. test_list = Frob('abby')

Output:

    Test: insert(test_list, Frob("xander"))
    Test: insert(test_list, Frob("beto"))
    *** Walking the linked list backward: ***
    xander
    beto
    abby

Test: 4

Equal names: Adding 'alvin' to the list ('alvin')

Output:

    Test: insert(Frob("alvin"), Frob("alvin"))
    *** Walking the linked list forward: ***
    alvin
    alvin
    *** Walking the linked list backward: ***
    alvin
    alvin

Test: 5

Multiple names. test_list = Frob('allison')

Output:

    Test: insert(test_list, Frob("lyla"))
    Test: insert(test_list, Frob("christina"))
    Test: insert(test_list, Frob("ben"))
    *** Walking the linked list forward: ***
    allison
    ben
    christina
    lyla
    *** Walking the linked list backward: ***
    lyla
    christina
    ben
    allison

Test: 6

Multiple names. test_list = Frob('zsa zsa') a = sm.Frob('ashley') m = sm.Frob('marcella') v = sm.Frob('victor')

Your output:

    Test: insert(test_list, m)
    Test: insert(m, a)
    Test: insert(a, v)
    Traceback (most recent call last):
      File "submission.py", line 87, in insert
        saveBeforeLink = nextnextFrobStructLink.getBefore()
    AttributeError: 'NoneType' object has no attribute 'getBefore'

Correct output:

    Test: insert(test_list, m)
    Test: insert(m, a)
    Test: insert(a, v)
    *** Walking the linked list forward: ***
    ashley
    marcella
    victor
    zsa zsa
    *** Walking the linked list backward: ***
    zsa zsa
    victor
    marcella
    ashley

Test: 7

Multiple names. test_list = Frob('mark') c = Frob('craig')

Your output:

    Test: insert(test_list, Frob("sam"))
    Test: insert(test_list, Frob("nick"))
    Test: insert(test_list, c)
    Test: insert(c, Frob("xanthi"))
    Traceback (most recent call last):
      File "submission.py", line 87, in insert
        saveBeforeLink = nextnextFrobStructLink.getBefore()
    AttributeError: 'NoneType' object has no attribute 'getBefore'

Correct output:

    Test: insert(test_list, Frob("sam"))
    Test: insert(test_list, Frob("nick"))
    Test: insert(test_list, c)
    Test: insert(c, Frob("xanthi"))
    Test: insert(test_list, Frob("jayne"))
    Test: insert(c, Frob("martha"))
    *** Walking the linked list forward: ***
    craig
    jayne
    mark
    martha
    nick
    sam
    xanthi
    *** Walking the linked list backward: ***
    xanthi
    sam
    nick
    martha
    mark
    jayne
    craig

Test: 8

Multiple names. test_list = Frob('leonid') a = Frob('amara') j1 = Frob('jennifer') j2 = Frob('jennifer') s = Frob('scott')

Your output:

    Test: insert(test_list, s)
    Test: insert(s, j1)
    Traceback (most recent call last):
      File "submission.py", line 127, in insert
        nextprevFrobStructLink = saveBeforeLink.getBefore() #point to next prev Frob structure
    AttributeError: 'NoneType' object has no attribute 'getBefore'

Correct output:

    Test: insert(test_list, s)
    Test: insert(s, j1)
    Test: insert(s, j2)
    Test: insert(j1, a)
    *** Walking the linked list forward: ***
    amara
    jennifer
    jennifer
    leonid
    scott
    *** Walking the linked list backward: ***
    scott
    leonid
    jennifer
    jennifer
    amara

Test: 9

Multiple names. test_list = Frob('eric')

Your output:

    Test: insert(test_list, Frob("eric"))
    Test: insert(test_list, Frob("chris"))
    Test: insert(test_list, Frob("john"))
    Traceback (most recent call last):
      File "submission.py", line 68, in insert
        nextnextFrobStructLink = saveAfterLink.getAfter() #point to next Frob structure
    AttributeError: 'NoneType' object has no attribute 'getAfter'

Correct output:

    Test: insert(test_list, Frob("eric"))
    Test: insert(test_list, Frob("chris"))
    Test: insert(test_list, Frob("john"))
    Test: insert(test_list, Frob("john"))
    Test: insert(test_list, Frob("chris"))
    Test: insert(test_list, Frob("eric"))
    Test: insert(test_list, Frob("john"))
    Test: insert(test_list, Frob("chris"))
    *** Walking the linked list forward: ***
    chris
    chris
    chris
    eric
    eric
    eric
    john
    john
    john
    *** Walking the linked list backward: ***
    john
    john
    john
    eric
    eric
    eric
    chris
    chris
    chris
'''

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    beforeFrob = start.getBefore()
    if (beforeFrob == None):
        #print "returning " + start.myName()
        return start
    else:
        #print " calling recursively findfront with " + beforeFrob.myName()
        findFront(beforeFrob)

frontFrob = findFront(ruth)
print "front frob was " + frontFrob.myName()
'''
findFront() test case results posted after exam due date--also see better solutions:
 INCORRECT Hide output
Test: 1

p = Frob('percival')

Output:

    findFront(p)
    percival

Test: 2

p = Frob('percival') r = Frob('rupert') insert(p, r)

Your output:

    findFront(p)
    percival
    findFront(r)
    AttributeError: 'NoneType' object has no attribute 'myName'

Correct output:

    findFront(p)
    percival
    findFront(r)
    percival

Test: 3

s = Frob('sterling') r = Frob('rupert') insert(s, r)

Your output:

    findFront(s)
    AttributeError: 'NoneType' object has no attribute 'myName'

Correct output:

    findFront(s)
    rupert
    findFront(r)
    rupert

Test: 4

Multiple names. test_list = Frob('zsa zsa') a = sm.Frob('ashley') m = sm.Frob('marcella') v = sm.Frob('victor')

Your output:

    insert(test_list, m)
    insert(m, a)
    insert(a, v)
    findFront(v)
    AttributeError: 'NoneType' object has no attribute 'myName'

Correct output:

    insert(test_list, m)
    insert(m, a)
    insert(a, v)
    findFront(v)
    ashley
    findFront(m)
    ashley

Test: 5

Multiple names. test_list = Frob('leonid') a = Frob('amara') j1 = Frob('jennifer') j2 = Frob('jennifer') s = Frob('scott')

Your output:

    insert(test_list, s)
    insert(s, j1)
    insert(s, j2)
    insert(j1, a)
    findFront(a)
    amara
    findFront(j1)
    AttributeError: 'NoneType' object has no attribute 'myName'

Correct output:

    insert(test_list, s)
    insert(s, j1)
    insert(s, j2)
    insert(j1, a)
    findFront(a)
    amara
    findFront(j1)
    amara
    findFront(j2)
    amara
    findFront(s)
    amara
    findFront(test_list)
    amara
'''
