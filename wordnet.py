import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
#to get the pos_number from synset 'x' => x=str(synset.name()) x.split('.')[2]



thing = datum.setup(atum())
wordnet = thing.Get("wordnet")
wordroot = wordnet.Get("wordroot")
noun = wordnet.Get("noun")
verb = wordnet.Get("verb")
adjective = wordnet.Get("adjective")
adjectiveSatellite=wordnet.Get("adjective satellite")
adverb = wordnet.Get("adverb")
definition = wordnet.Get("definition")
example_ = wordnet.Get("example")
priority= wordnet.Get("priority")
typeDictionary={'s':adjectiveSatellite,'n':noun,'v':verb,'a':adjective,'r':adverb}

for synset in list(wn.all_synsets()):
	name=synset.name()
	type_=name.split('.')[1]
	if(type_=='s' or type_=='a'or type_=='r'or type_=='v'or type_=='n'):
		wordrootKatum=wordroot.Get(name.split('.')[0])
		wordKatum=wordrootKatum.Get(wordrootKatum.countI)
		if synset.definition()!=None:
			wordDefinition=definition.Get(synset.definition())
			wordKatum._is(wordDefinition,False)
		if synset.examples()!=None:
			for example in synset.examples():
				exampleKatum=example_.Get(example)
				wordKatum._is(exampleKatum,False)
		priorityKatum=priority.Get(name.split('.')[2])
		wordKatum._is(priorityKatum,False)
		wordKatum._is(typeDictionary[type_],False)




thing.save('wordnetonlysynsets.datum')