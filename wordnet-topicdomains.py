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

katum.load('wordnet-notopicdomains.datum', atum())
generalThing = datum.thing
wordnetRoot=generalThing.find("wordnet")
wordRoot=wordnetRoot.find("wordroot")
definition=wordnetRoot.find("definition")
topicDomain_=wordnetRoot.get("topic domain")
count=1
for word in wordRoot.I:
	if(word.countI>0):
		for instance in word.I:
			exactSynset=getExactSynset(instance)
			if exactSynset:
				topicDomains=exactSynset.topic_domains()
				if len(topicDomains)>0:
					for topicDomain in topicDomains:
						topicDomainKatum=getExactKatum(topicDomain)
						if topicDomainKatum:
							if topicDomainKatum in visited:
								instance._is(visited[topicDomainKatum], False)
							else:
								topicDomainNewK=topicDomain_.get(count)
								topicDomainNewK._is(topicDomainKatum,False)
								instance._is(topicDomainNewK,False)
								visited[topicDomainKatum]=topicDomainNewK
								count+=1


generalThing.save('wordnet-noregiondomains.datum')
