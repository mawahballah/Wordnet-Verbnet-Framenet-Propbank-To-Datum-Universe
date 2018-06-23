import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
visited={}

def Getexactsynset(syn,wordindatum,wnr):
	wordstr=Getname(syn)
	definition = wnr.find("definition")
	curdefinition = syn.definition()
	priority=wnr.find("priority")
	word = wordstr.split('.')[0]
	pos = wordstr.split('.')[1]
	typ="notfound"	
	if (pos=='n'):
		typ="noun"
	elif(pos=='v'):
		typ="verb"
	elif(pos=='r'):
		typ="adverb"
	elif(pos=='a'):
		typ="adjective"
	if(typ!="notfound"):
		if(wordindatum.countI>0):
			for instance in wordindatum.I:
				if(instance.Is(wnr.find(typ))):
					defin=definition.of(instance)
					if(defin!=None):
						if(defin.O==curdefinition):
							return instance
	return None			

def Getname(wne):
    x=wne.name()
    x=str(x)
    return x						

katum.load('wordnet-nosister.datum', atum())
wordnetthing = datum.thing

wordnetroot=wordnetthing.find("wordnet")
wordroot=wordnetroot.find("wordroot")
has=wordnetroot.find("has")
sister=wordnetroot.get("sister")

for w in wordroot.I:
	worditself=w.O
	listofsynsets=wn.synsets(worditself)
	for synset in listofsynsets:
		if not visited.get(synset.name(),False):
			visited[synset.name()]=True			
			exactinstance=Getexactsynset(synset,w,wordnetroot)
			if(exactinstance!=None):
				if(exactinstance.countI>0):
					currentparent=sister.get(sister.countI+1)				
					for instance in exactinstance.I:
						if(instance.Is(has)==False):
							instance._is(currentparent,check=False)





wordnetthing.save('wordnet-example-definition.datum')