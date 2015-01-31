#!/usr/bin/python
import codecs, string

with codecs.open('/etc/dictionaries-common/words', encoding='utf-8') as f:
    words = [x.lower().rstrip() for x in f.readlines() if "'" not in x]

with codecs.open('tubes.csv', encoding='utf-8') as f:
    collection = [''.join(ch for ch in s if ch not in string.punctuation).lower() for s in f.readlines()]
#collection = ('apple', 'banana', 'cherry', 'damson', 'elderberry', 'fig', 'grape')

def criteria(item, candidate):
    return not any(letter in candidate for letter in item)

matches = {item: set([candidate for candidate in words if criteria(item, candidate)]) for item in collection}
uniquely_identifying_matches = {item: matches[item].difference(set(reduce(lambda a, b: a.union(b), [matches[n] for n in [x for x in collection if not x == item]]))) for item in collection}
 
print uniquely_identifying_matches
#s.difference(t)

