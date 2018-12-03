import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

visited={}
def getExactSynset(katum):
	name=katum.a0.O
	definitionKatum=definition.of(katum)
	for synset in wn.synsets(name):
		if(synset.definition()==definitionKatum.O):
			return synset
	return None

def getExactKatum(synset):
	name=synset.name()
	word=name.split('.')[0]
	wordKatum=wordRoot.find(word)
	if(wordKatum!=None):
		synsetDefinition=synset.definition()
		for instance in wordKatum.I:
			instanceDefinition=definition.of(instance)
			if(instanceDefinition!=None and instanceDefinition.O==synsetDefinition):
				return instance
	return None

katum.load('wordnet-nousagedomains.datum', atum())
generalThing = datum.thing
wordnetRoot=generalThing.find("wordnet")
wordRoot=wordnetRoot.find("wordroot")
definition=wordnetRoot.find("definition")
usageDomain_=wordnetRoot.get("usage domain")
count=1
for word in wordRoot.I:
	if(word.countI>0):
		for instance in word.I:
			exactSynset=getExactSynset(instance)
			if exactSynset:
				usageDomains=exactSynset.usage_domains()
				if len(usageDomains)>0:
					for usageDomain in usageDomains:
						usageDomainKatum=getExactKatum(usageDomain)
						if usageDomainKatum:
							if usageDomainKatum in visited:
								instance._is(visited[usageDomainKatum], False)
							else:
								usageDomainNewK=usageDomain_.get(count)
								usageDomainNewK._is(usageDomainKatum,False)
								instance._is(usageDomainNewK,False)
								visited[usageDomainKatum]=usageDomainNewK
								count+=1


generalThing.save('wordnet-nolemmas.datum')
