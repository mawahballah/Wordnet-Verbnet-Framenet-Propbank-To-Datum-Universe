import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


visited=set()

katum.load('wordnet-noverbgroups.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordroot=wordnetRoot.find("wordroot")
verbGroup=wordnetRoot.get("verb group")

def getExactSynset(syn):
	word=str(syn.name()).split('.')[0]
	wordInDatum=wordroot.find(word)
	if wordInDatum!=None:
		definition=wordnetRoot.find("definition")
		currentDefinition=syn.definition()
		priority=wordnetRoot.find("priority")
		pos = syn.pos()
		type_="notfound"	
		if (pos=='n'):
			type_="noun"
		elif(pos=='v'):
			type_="verb"
		elif(pos=='r'):
			type_="adverb"
		elif(pos=='a'):
			type_="adjective"
		elif(pos=='s'):
			type_="adjective satellite"
		if(type_!="notfound"):
			if(wordInDatum.countI>0):					
				for instance in wordInDatum.I:
					if(instance.Is(wordnetRoot.find(type_))):
						defin=definition.of(instance)
						if(defin!=None):
							if(defin.O==currentDefinition):
								return instance
		return None			

def getName(wne):
    x=wne.name()
    x=str(x)
    return x						

def addVerbGroup(synset,verbGroupSynset):
	synsetSenseKatum=getExactSynset(synset)
	verbGroupSenseKatum=getExactSynset(verbGroupSynset)
	if synsetSenseKatum!= None and verbGroupSenseKatum!=None:
		verbGroupKatum=verbGroup.get(verbGroup.countI)
		verbGroupSenseKatum._is(verbGroupKatum,False)
		synsetSenseKatum._is(verbGroupKatum,False)


for synset in list(wn.all_synsets('v')):
	for verbGroupSynset in synset.verb_groups():
		if verbGroupSynset not in visited:
			addVerbGroup(synset,verbGroupSynset)
	visited.add(synset)

generalThing.save('wordnet-nopertainym.datum')
