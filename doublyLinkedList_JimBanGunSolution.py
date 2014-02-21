#########################################################
#
#   Definition of a Frob in a Doubly Linked List
#
#   A frob/node has a 'before' and an 'after' pointer
#
#   Frob name is case sensitive and will be ordered
#   alphabetically (e.g. frob 'andrew' > 'Andrew')   
#
#   Program by Jimmy Bangun
#   Final Exam - MITx 6.00 Fall 2012
#
#########################################################
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


#########################################################
#
#   Function to insert frobs into a Doubly Linked list
#
#########################################################
def insert(atMe, newFrob):
    
    ## Check if atMe is actually free (a new frob), if yes then swap with newFrob
    if (atMe.before == None and atMe.after == None):
        temp = atMe
        atMe = newFrob
        newFrob = temp
        
    ## newFrob is to the right of atMe
    if atMe.name < newFrob.name:

        # set pointer
        ptr = atMe

        # Check if atMe and newFrob are the first 2 frobs in the link
        if ptr.after == None and newFrob.before == None:
            newFrob.after = ptr.after
            newFrob.before = ptr
            ptr.after = newFrob

        # Link already exists
        else:

            # Move pointer to find position to insert newFrob
            while ptr.after.name < newFrob.name:
                ptr = ptr.after
                if ptr.after == None:   # pointer at the end of link
                    break
                
            # Insert newFrob by changing the frob attributes
            newFrob.after = ptr.after
            newFrob.before = ptr
            if ptr.after != None:   # newFrob not at end of link
                ptr.after.before = newFrob 
            ptr.after = newFrob  
                        
    ## newFrob is to the left of atMe
    else:

        # set pointer
        ptr = atMe

        # Check if atMe and newFrob are the first 2 frobs in the link
        if ptr.before == None and newFrob.after == None:
            newFrob.after = ptr
            newFrob.before = ptr.before
            ptr.before = newFrob

        # Link already exists
        else:

            # Move pointer to find position to insert newFrob
            while ptr.before.name > newFrob.name:
                ptr = ptr.before
                if ptr.before == None:  # pointer at the end of link
                    break

            # Insert newFrob by changing the frob attributes
            newFrob.before = ptr.before
            newFrob.after = ptr
            if ptr.before != None:  # newFrob not at end of link
                ptr.before.after = newFrob        
            ptr.before = newFrob
            
           
#########################################################
#
#   Function to find head/start of a Doubly Linked list
#
#########################################################
def findFront(start):
    
    # Initialize pointer position
    ptr = start

    # Base case (beginning of the link)
    if ptr.before == None:
        return ptr

    # Recursive case (move pointer to left and findFront)
    else:
        return findFront(ptr.before)



#########################################################
#
#   Test Case (DL link should be in alphabetical order
#   from left to right. Last before/after == None
#
#########################################################    

# Create frobs
andrew = Frob('andrew')
eric = Frob('eric')
fred = Frob('fred')
martha = Frob('martha')
ruth = Frob('ruth')
adam = Frob('adam')
estu = Frob('estu')
albert = Frob('albert')
yoyo = Frob('yoyo')

print "Print result is in the 'Before - Frob Name - After' format"
print " "

print "Start from nothing and link 2 nodes"
insert(eric, andrew)
print andrew.before, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after
print " "

print "Insert at end of link"
insert(eric, ruth)
print andrew.before, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert in middle of link to the right"
insert(eric, fred)
print andrew.before, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print fred.before.name, fred.name, fred.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert from end of link to the left"
insert(ruth, martha)
print andrew.before, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print fred.before.name, fred.name, fred.after.name
print martha.before.name, martha.name, martha.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert at start of link"
insert(andrew, adam)
print adam.before, adam.name, adam.after.name
print andrew.before.name, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print fred.before.name, fred.name, fred.after.name
print martha.before.name, martha.name, martha.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert in middle of link to the left"
insert(fred, estu)
print adam.before, adam.name, adam.after.name
print andrew.before.name, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print estu.before.name, estu.name, estu.after.name
print fred.before.name, fred.name, fred.after.name
print martha.before.name, martha.name, martha.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert from start of link to the right"
insert(adam,albert)
print adam.before, adam.name, adam.after.name
print albert.before.name, albert.name, albert.after.name
print andrew.before.name, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print estu.before.name, estu.name, estu.after.name
print fred.before.name, fred.name, fred.after.name
print martha.before.name, martha.name, martha.after.name
print ruth.before.name, ruth.name, ruth.after
print " "

print "Insert to end from start"
insert(adam, yoyo)
print adam.before, adam.name, adam.after.name
print albert.before.name, albert.name, albert.after.name
print andrew.before.name, andrew.name, andrew.after.name
print eric.before.name, eric.name, eric.after.name
print estu.before.name, estu.name, estu.after.name
print fred.before.name, fred.name, fred.after.name
print martha.before.name, martha.name, martha.after.name
print ruth.before.name, ruth.name, ruth.after.name
print yoyo.before.name, yoyo.name, yoyo.after
print " "

# Find head/start of DL from the last/right node
print findFront(yoyo).name