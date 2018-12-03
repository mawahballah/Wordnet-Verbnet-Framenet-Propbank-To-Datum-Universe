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

katum.load('wordnet-noregiondomains.datum', atum())
generalThing = datum.thing
wordnetRoot=generalThing.find("wordnet")
wordRoot=wordnetRoot.find("wordroot")
definition=wordnetRoot.find("definition")
regionDomain_=wordnetRoot.get("region domain")
count=1
for word in wordRoot.I:
	if(word.countI>0):
		for instance in word.I:
			exactSynset=getExactSynset(instance)
			if exactSynset:
				regionDomains=exactSynset.region_domains()
				if len(regionDomains)>0:
					for regionDomain in regionDomains:
						regionDomainKatum=getExactKatum(regionDomain)
						if regionDomainKatum:
							if regionDomainKatum in visited:
								instance._is(visited[regionDomainKatum], False)
							else:
								regionDomainNewK=regionDomain_.get(count)
								regionDomainNewK._is(regionDomainKatum,False)
								instance._is(regionDomainNewK,False)
								visited[regionDomainKatum]=regionDomainNewK
								count+=1


generalThing.save('wordnet-nousagedomains.datum')
