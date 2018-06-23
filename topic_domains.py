import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

def Getexactsynset(katum):
	name=katum.a0.O
	definitionkatum=definition.of(katum)
	for synset in wn.synsets(name):
		if(synset.definition()==definitionkatum.O):
			return synset
	return None

def Getexactkatum(synset):
	name=synset.name()
	word=name.split('.')[0]
	wordkatum=wordroot.find(word)
	if(wordkatum!=None):
		synsetdefinition=synset.definition()
		for instance in wordkatum.I:
			instancedefinition=definition.of(instance)
			if(instancedefinition!=None and instancedefinition.O==synsetdefinition):
				return instance				
	return None

katum.load('wordnet-hyponyms-exceptions.datum', atum())
generalthing = datum.thing
wordnetroot=generalthing.find("wordnet")
wordroot=wordnetroot.find("wordroot")
definition=wordnetroot.find("definition")
topicdomain=wordnetroot.get("topic domain")
for word in wordroot.I:
	if(word.countI>0):
		for instance in word.I:
			exactsynset=Getexactsynset(instance)
			if exactsynset:
				topicdomains=exactsynset.topic_domains()
				if len(topicdomains)>0:
					for tdomain in topicdomains:
						tdomainkatum=Getexactkatum(tdomain)
						if tdomainkatum:
							tdomainkatum._is(topicdomain,False)
							instance._is(tdomainkatum,False)


generalthing.save('wordnet-hyponyms-exceptions-topicdomains.datum')