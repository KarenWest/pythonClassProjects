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
    def word_param():
        return params
    
    def trigger_param():
        return [triggerMap[p] for p in params]
    
    def phrase_param():
        return [' '.join(params)]
    
    trigger_types = {
                     'TITLE': (TitleTrigger, word_param), 
                     'SUBJECT': (SubjectTrigger, word_param), 
                     'SUMMARY': (SummaryTrigger, word_param), 
                     'NOT': (NotTrigger, trigger_param), 
                     'AND': (AndTrigger, trigger_param), 
                     'OR': (OrTrigger, trigger_param), 
                     'PHRASE': (PhraseTrigger, phrase_param)
                     }
    
    params = trigger_types[triggerType][1]()
    triggerMap[name] = trigger_types[triggerType][0](*params)
    return triggerMap[name]