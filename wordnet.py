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
adjectivesatellite=wordnet.Get("adjective satellite")
adverb = wordnet.Get("adverb")
definition = wordnet.Get("definition")
example = wordnet.Get("example")
priority= wordnet.Get("priority")
typedict={'s':adjectivesatellite,'n':noun,'v':verb,'a':adjective,'r':adverb}

for synset in list(wn.all_synsets()):
	name=synset.name()
	type_=name.split('.')[1]
	if(type_=='s' or type_=='a'or type_=='r'or type_=='v'or type_=='n'):
		wordrootkatum=wordroot.Get(name.split('.')[0])
		wordkatum=wordrootkatum.Get(wordrootkatum.countI)
		if synset.definition()!=None:
			worddefinition=definition.Get(synset.definition())
			wordkatum._is(worddefinition,False)
		if synset.examples()!=None:
			for ex in synset.examples():
				examplekatum=example.Get(ex)
				wordkatum._is(examplekatum,False)
		prioritykatum=priority.Get(name.split('.')[2])
		wordkatum._is(prioritykatum,False)
		wordkatum._is(typedict[type_],False)




thing.save('wordnetonlysynsets.datum')