import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir("C:\Users\mabde\Desktop\wordnet-datum")
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


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
					defby=definition.of(instance)
					if(defby!=None):
						if(defby.a0.O==curdefinition):
							return instance
	return None			

def Getname(wne):
    x=wne.name()
    x=str(x)
    return x						

katum.load('wordnet-nolemmas.datum', atum())
wordnetthing = datum.thing

wordnetroot=wordnetthing.find("wordnet")
wordroot=wordnetroot.find("wordroot")
lemma=wordnetroot.get("lemma")

for w in wordroot.I:
	worditself=w.O
	listofsynsets=wn.synsets(worditself)
	for synset in listofsynsets:
		listoflemmas=synset.lemma_names()
		if(len(listoflemmas)>1):
			exactinstance=Getexactsynset(synset,w,wordnetroot)
			if(exactinstance!=None):						
				for li in listoflemmas:
					if(li!=worditself):					
						lem=lemma.get(li)
						exactinstance._is(lem)


wordnetthing.save('C:/Users/mabde/Desktop/wordnet-datum/wordnet-nohas.datum')