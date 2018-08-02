import nltk
import re
import os
from collections import deque
os.chdir(os.getcwd())
from nltk.corpus import wordnet as wn
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
#to get the pos_number from synset 'x' => x=str(synset.name()) x.split('.')[2]
sense_key_regex = r"(.*)\%(.*):(.*):(.*):(.*):(.*)"
synset_type_es = {1:'n', 2:'v', 3:'a', 4:'r', 5:'s'}

def synsetFromSenseKey(sense_key):
    lemma, ss_type_e, lex_num, lex_id, head_word, head_id = re.match(sense_key_regex, sense_key).groups()
    ss_idx = '.'.join([lemma, synset_type_es[int(ss_type_e)], lex_id])
    word=ss_idx.split('.')[0]
    if(len(wn.synsets(word))>0):
    	for synset in wn.synsets(word):
    		if(synset.name()==ss_idx):
    			return ss_idx
    return None

def getName(wne):
    x=wne.name()
    x=str(x)
    return x

def exactKatumFromSynset(synset,wnr):
	wordStr=getName(synset)
	definition=wnr.find("definition")
	currentDefinition=synset.definition()
	priority=wnr.find("priority")
	wordroot=wordnetRoot.find("wordroot")
	word = wordStr.split('.')[0]
	wordInDatum=wordroot.find(word)
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

def framnetMatch(frameWord,lexicalUnitWord):
	frameKatum=frame.find(frameWord)
	if frameKatum!=None:
		for attribute in frameKatum.A:
			if lexicalUnitWord == attribute.a0.O:
				return attribute
	return None


katum.load('wordnet-verbnet-framenet-propbank.datum', atum())
thing = datum.thing
wordnetRoot=thing.find("wordnet")
framenetRoot=thing.find("framenet")
frame=framenetRoot.find("frame")
lexicalUnit= framenetRoot.find("lexical unit")
done=1
for line in open('FnWnVerbMap.1.0.txt', 'r'):	
	myList=line.split()	
	if len(myList)>=3:
   		if myList[len(myList)-1]!="0":
			frameKatum=framnetMatch(myList[0].title(),myList[1])
			if frameKatum!=None:
				i=2
				while i<len(myList):
					if myList[i]!="0":
						synset=synsetFromSenseKey(myList[i])
						if synset!=None:
							wordkatum=exactKatumFromSynset(wn.synset(synset),wordnetRoot)
							if wordkatum!=None:
								wordkatum._is(frameKatum,False)
								print done,wordkatum.a0.O,wordkatum.O,frameKatum.a0.O,frameKatum.O
								done+=1
					i+=1
thing.save('wordnet-verbnet-framenet-propbank-linked.datum')
    	 