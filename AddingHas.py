import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir("C:\Users\mabde\Desktop\wordnet-datum")
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

visited={}
meronymdict={}
def Getexactsynset(syn,wordindatum,wnr):
	wordstr=Getname(syn)
	definition=wnr.find("definition")
	curdefinition=syn.definition()
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
					if(defby.a0.O==curdefinition):
						return instance
	return None			

def Getname(wne):
    x=wne.name()
    x=str(x)
    return x						

def addhas(synset,wordindatum,wordnetroot,parent):
	listofmeronyms=synset.part_meronyms()
	if(len(listofmeronyms)>0):
		for li in listofmeronyms:				
			if not visited.get(li,False):
				visited[li]=True
				liwordnet=wordroot.find(li.name().split('.')[0])
				if(liwordnet!=None):
					exactmeronym=Getexactsynset(li,liwordnet,wordnetroot)
					if(exactmeronym!=None):
						meronymname=exactmeronym.a0.O
						if (meronymname == "school_system"):
							here = 1
						meronymnumber=exactmeronym.countI+1
						newmeronyminstance=parent.get(meronymname+str(meronymnumber))
						newmeronyminstance._is(exactmeronym)
						addhas(li,liwordnet,wordnetroot,newmeronyminstance)	



katum.load('wordnet-nohas.datum', atum())
wordnetthing = datum.thing

wordnetroot=wordnetthing.find("wordnet")
wordroot=wordnetroot.find("wordroot")
has=wordnetroot.get("has")

for w in wordroot.I:
	worditself=w.O
	listofsynsets=wn.synsets(worditself)
	for synset in listofsynsets:
		if (len(synset.part_meronyms()) > 0 and len(synset.part_holonyms())==0):
			if not visited.get(synset,False):
				visited[synset]=True
				exactinstance=Getexactsynset(synset,w,wordnetroot)
				if(exactinstance!=None):
					instancename=exactinstance.a0.O
					number=exactinstance.countI+1
					newhasinstance=has.get(instancename+str(number))
					newhasinstance._is(exactinstance)
					addhas(synset,w,wordnetroot,newhasinstance)

wordnetthing.save('C:/Users/mabde/Desktop/wordnet-datum/wordnet.datum')