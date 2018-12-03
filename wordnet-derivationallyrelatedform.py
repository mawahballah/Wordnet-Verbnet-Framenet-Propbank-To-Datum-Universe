import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


visited=set()
katum.load('wordnet-norelatedform.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordroot=wordnetRoot.find("wordroot")
relatedForm=wordnetRoot.get("derivationally related form")

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

def addDerivationallyRelatedForm(synset,relatedFormSynset):
	synsetSenseKatum=getExactSynset(synset)
	relatedFormSynsetSenseKatum=getExactSynset(relatedFormSynset)
	if synsetSenseKatum!= None and relatedFormSynsetSenseKatum!=None:
		relatedFormKatum=relatedForm.get(relatedForm.countI)
		relatedFormSynsetSenseKatum._is(relatedFormKatum,False)
		synsetSenseKatum._is(relatedFormKatum,False)


for synset in list(wn.all_synsets()):
	for lemma in synset.lemmas():
		if lemma.synset() not in visited:
			for derivationallyRelatedForm in lemma.derivationally_related_forms():
				if derivationallyRelatedForm.synset() not in visited:
					addDerivationallyRelatedForm(synset,derivationallyRelatedForm.synset())
			visited.add(lemma.synset())

generalThing.save('wordnet-noverbgroups.datum')
