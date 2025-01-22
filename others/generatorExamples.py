def countdown(k):
    """
    >>> list(countdown(5))
    [5, 4, 3, 2, 1, 'Blast off']
    """
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield 'Blast off'

def prefixes(s):
    """
    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    """
    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])