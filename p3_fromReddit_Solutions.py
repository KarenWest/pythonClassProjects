def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    temp = atMe
    before = None
    while temp.getBefore():
        temp = temp.getBefore()
    after = temp
    while after and newFrob.myName() > after.myName():
        before = after
        after = after.getAfter()
    newFrob.setAfter(after)
    newFrob.setBefore(before)
    if before:
        before.setAfter(newFrob)
    if after:
        after.setBefore(newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore():
        return findFront(start.getBefore())
    return start