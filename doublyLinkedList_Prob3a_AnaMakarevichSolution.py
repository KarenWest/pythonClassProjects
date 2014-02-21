def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.myName() > newFrob.myName():
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)            
        else:
            if newFrob.myName() > atMe.getBefore().myName():
                newFrob.setBefore(atMe.getBefore())
                atMe.getBefore().setAfter(newFrob)
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)            
            else:
                insert(atMe.getBefore(), newFrob)        
    else:
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            if newFrob.myName() < atMe.getAfter().myName():
                newFrob.setAfter(atMe.getAfter())
                atMe.getAfter().setBefore(newFrob)
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
            else:
                insert(atMe.getAfter(), newFrob)

#Here are some test cases for this Problem:
##eric = Frob('eric')
##andrew = Frob('andrew')
##ruth = Frob('ruth')
##fred = Frob('fred')
##martha = Frob('martha')
##boris = Frob('boris')
##newf = Frob('martha')
##insert(eric, andrew)
##insert(eric, martha)
##insert(eric, boris)
##print "before eric: " + str(eric.getBefore().myName()) + "(expected: Boris)"
##print "after eric: " + str(eric.getAfter().myName()) + "(expected: Martha)"
##print "before boris: " + str(boris.getBefore().myName()) + "(expected: Andrew)"
##print "after boris: " + str(boris.getAfter().myName()) + "(expected: Eric)"
##print "after andrew: " + str(andrew.getAfter().myName()) + "(expected: Boris)"
##insert(eric, fred)
##print "after eric: " + str(eric.getAfter().myName()) + "(expected: Fred)"
##print "before fred: " + str(fred.getBefore().myName()) + "(expected: Eric)"
##print "after fred: " + str(fred.getAfter().myName()) + "(expected: Martha)"