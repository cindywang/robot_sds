__author__ = 'ray'

import os
from StanfordTagger_Revised import StanfordNERTagger

classpath = "/Users/Ray/Documents/Dev/stanford-ner/stanford-ner.jar:/Users/Ray/Documents/Dev/stanford-ner/lib/*"
os.environ['CLASSPATH'] = classpath
print 'CLASSPATH: ', os.environ['CLASSPATH']

st = StanfordNERTagger('/Users/Ray/Documents/Dev/stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz')
# st = StanfordNERTagger('/Users/Ray/Documents/Dev/stanford-ner/classifiers/english.conll.4class.distsim.crf.ser.gz')
# st = StanfordNERTagger('/Users/Ray/Documents/Dev/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz')
# ret = st.tag('Rami Eid is studying at Stony Brook University in New York'.split())
ret = st.tag('tell me about professor Inkpen'.split())
for r in ret: print r, type(r), type(r[0])

# who is the us president
# i visited London last summer
# I went to Ottawa from Toronto.
# Dr. Inkpen is a very nice professor.
# Ray bought 300 shares of Acme Corp. in 2006.

