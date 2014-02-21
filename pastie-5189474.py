## Problem 4 [python]
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    assert(type(s1) is str)
    assert(type(s2) is str)
    result=""
    i=0
    iMax = min(len(s1), len(s2))
    while i < iMax:
          result += s1[i] + s2[i]
          i+=1
    if (len(s1) > iMax):
        result += s1[iMax:]
    elif len(s2) > iMax:
        result += s2[iMax:]
    return result



def assertThat(tst, result):
    print "Testing", tst, ":",
    try:
        res = eval(tst)
    except AssertionError:
        res = "error"
    print "Success" if res == result else ("Expected:", result, "got", res)

assertThat("laceStrings('','')", '')
assertThat("laceStrings('a','')", 'a')
assertThat("laceStrings('','a')", 'a')
assertThat("laceStrings('ab','a')", 'aab')
assertThat("laceStrings('a','ab')", 'aab')
assertThat("laceStrings('Hello','World')", 'HWeolrllod')
assertThat("laceStrings('HloWrd','el ol')", 'Hello World')
assertThat("laceStrings(1,'abc')", 'error')
assertThat("laceStrings('abc',2)", 'error')
assertThat("laceStrings('135','24')", '12345')
assertThat("laceStrings(None,'abc')", 'error')
assertThat("laceStrings('abc',None)", 'error')
