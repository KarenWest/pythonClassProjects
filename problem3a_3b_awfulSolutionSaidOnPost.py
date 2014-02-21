def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    ptr = atMe
    debug = False
    while True:
        if newFrob.myName() < ptr.myName():
            if ptr.getBefore() is None:
                # Put newFrob at head
                if debug:
                    print "put newFrob at head"
                ptr.setBefore(newFrob)
                newFrob.setAfter(ptr)
                newFrob.setBefore(None)
                break
            elif newFrob.myName() >= ptr.getBefore().myName():
                # Insert inbetween
                if debug:
                    print "put inbetween going left"
                bbefore = ptr.getBefore()
                aafter = ptr
                newFrob.setAfter(aafter)
                newFrob.setBefore(bbefore)
                aafter.setBefore(newFrob)
                bbefore.setAfter(newFrob)
                break
            else:
                if debug:
                    print "increment left"
                ptr = ptr.getBefore()
        else:
            if ptr.getAfter() is None:
                # Put at end
                if debug:
                    print "Put at end"
                ptr.setAfter(newFrob)
                newFrob.setBefore(ptr)
                newFrob.setAfter(None)
                break
            elif newFrob.myName() <= ptr.getAfter().myName():
                # Insert in between
                if debug:
                    print "Put inbetween going right"
                bbefore = ptr
                aafter = ptr.getAfter()
                newFrob.setAfter(aafter)
                newFrob.setBefore(bbefore)
                aafter.setBefore(newFrob)
                bbefore.setAfter(newFrob)
                break
            else:
                if debug:
                    print "increment right"
                ptr = ptr.getAfter()
         
    
def printList(frob):
    while frob.getBefore() is not None:
        #print '1'
        frob = frob.getBefore()
    while frob.getAfter() is not None:
       # print '2'
        print frob.myName() + ' -> ' ,
        frob = frob.getAfter()
    print frob.myName()
    
    # print "printing addresses"
    # while frob.getBefore() is not None:
    # #print '1'
        # frob = frob.getBefore()
    
    # while frob.getAfter() is not None:
       # # print '2'
        # print frob,
        # frob = frob.getAfter()   
    # print frob        
    
    # while frob.getBefore() is not None:
        # print frob,
        # frob = frob.getBefore()
    # print frob
     
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here    
    if start.getBefore() is None:
        #print start.myName()
        return start
    else:
        #print start.myName()
        return findFront(start.getBefore())