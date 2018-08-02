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
	definition = wnr.find("definition")
	currentDefinition = syn.definition()
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

katum.load('wordnet-nosister.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordRoot=wordnetRoot.find("wordRoot")
has=wordnetRoot.find("has")
sister=wordnetRoot.get("sister")

for word in wordRoot.I:
	wordItself=word.O
	listOfSynsets=wn.synsets(wordItself)
	for synset in listOfSynsets:
		if not visited.get(synset.name(),False):
			visited[synset.name()]=True			
			exactInstance=getExactSynset(synset,word,wordnetRoot)
			if(exactInstance!=None):
				if(exactInstance.countI>0):
					currentParent=sister.get(sister.countI+1)				
					for instance in exactInstance.I:
						if(instance.Is(has)==False):
							instance._is(currentParent,check=False)





generalThing.save('wordnet-example-definition.datum')