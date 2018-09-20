import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

visited={}
def getExactSynset(syn,wordInDatum,wnr):
	wordStr=getName(syn)
	definition=wnr.find("definition")
	currentDefinition=syn.definition()
	priority=wnr.find("priority")
	word = wordStr.split('.')[0]
	pos = wordStr.split('.')[1]
	type_="notfound"	
	if (pos=='n'):
		type_="noun"
	elif(pos=='v'):
		type_="verb"
	elif(pos=='r'):
		type_="adverb"
	elif(pos=='a'):
		type_="adjective"
	if(type_!="notfound"):
		if(wordInDatum.countI>0):					
			for instance in wordInDatum.I:
				if(instance.Is(wnr.find(type_))):
					defin=definition.of(instance)
					if(defin!=None):
						if(defin.O==currentDefinition):
							return instance
	return None			

def getName(wne):
    x=wne.name()
    x=str(x)
    return x						

def addHas(synset,wordInDatum,wordnetRoot,parent):
	listOfMeronyms=synset.part_meronyms()
	if(len(listOfMeronyms)>0):
		for meronym in listOfMeronyms:				
			if not visited.get(meronym,False):
				visited[meronym]=True
				meronymWordnet=wordroot.find(meronym.name().split('.')[0])
				if(meronymWordnet!=None):
					exactMeronym=getExactSynset(meronym,meronymWordnet,wordnetRoot)
					if(exactMeronym!=None):
						meronymName=exactMeronym.a0.O						
						meronymNumber=exactMeronym.countI+1
						newMeronymInstance=parent.get(meronymName+str(meronymNumber))
						newMeronymInstance._is(exactMeronym)
						addHas(meronym,meronymWordnet,wordnetRoot,newMeronymInstance)	



katum.load('wordnet-nohas.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordroot=wordnetRoot.find("wordroot")
has=wordnetRoot.get("has")

for w in wordroot.I:
	wordItself=w.O
	listOfSynsets=wn.synsets(wordItself)
	for synset in listOfSynsets:
		if(synset.name().split('.')[0]==str(wordItself)):
			if (len(synset.part_meronyms()) > 0 and len(synset.part_holonyms())==0):
				if not visited.get(synset,False):
					visited[synset]=True
					exactInstance=getExactSynset(synset,w,wordnetRoot)
					if(exactInstance!=None):
						instanceName=exactInstance.a0.O
						number=exactInstance.countI+1
						newHasInstance=has.get(instanceName+str(number))
						newHasInstance._is(exactInstance)
						addHas(synset,w,wordnetRoot,newHasInstance)

generalThing.save('wordnet-nosister.datum')
