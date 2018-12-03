from nltk.corpus import wordnet as wn
import os
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

visited={}
katum.load('wordnet-nopertainym.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordroot=wordnetRoot.find("wordroot")
pertainymRoot=wordnetRoot.get("pertainym")


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
	elif(pos=='s'):
		type_="adjective satellite"
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

def addPertainym(adverb,pertainym,parent):
    adverbWord=getName(adverb)
    adverbDatum=getExactSynset(adverb,wordroot.find(adverbWord.split('.')[0]),wordnetRoot)
    pertainymWord = getName(pertainym)
    pertainymDatum = getExactSynset(pertainym,wordroot.find(pertainymWord.split('.')[0]), wordnetRoot)
    if pertainymDatum and adverbDatum:
        parent._is(pertainymDatum,False)
        adverbDatum._is(parent,False)


count=1
for adverb in wn.all_synsets('r'):
    if len(adverb.lemmas())>0:
		lemma=adverb.lemmas()
		for pertainym in lemma[0].pertainyms():
			if pertainym.synset() in visited:
				addPertainym(adverb,pertainym.synset(),visited[pertainym.synset()])
			else:
				parent=pertainymRoot.get(count)
				visited[pertainym.synset()]=parent
				addPertainym(adverb,pertainym.synset(),parent)
				count+=1


generalThing.save('wordnet-notopicdomains.datum')
