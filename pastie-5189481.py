## Problem 5 [python]
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0]+s2[0]+helpLaceStrings(s1[1:], s2[1:], out)
    return helpLaceStrings(s1, s2, '')


def assertThat(tst, result):
    print "Testing", tst, ":",
    try:
        res = eval(tst)
    except AssertionError:
        res = "error"
    print "Success" if res == result else ("Expected:", result, "got", res)

assertThat("laceStringsRecur('','')", '')
assertThat("laceStringsRecur('a','')", 'a')
assertThat("laceStringsRecur('','a')", 'a')
assertThat("laceStringsRecur('ab','a')", 'aab')
assertThat("laceStringsRecur('a','ab')", 'aab')
assertThat("laceStringsRecur('Hello','World')", 'HWeolrllod')
assertThat("laceStringsRecur('HloWrd','el ol')", 'Hello World')
assertThat("laceStringsRecur('135','24')", '12345')
#tests below not needed because not given by 600x
#assertThat("laceStringsRecur(1,'abc')", 'error')
#assertThat("laceStringsRecur('abc',2)", 'error')
#assertThat("laceStringsRecur(None,'abc')", 'error')
#assertThat("laceStringsRecur('abc',None)", 'error')
