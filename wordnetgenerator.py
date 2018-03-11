import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir("C:\Users\mabde\Desktop\wordnet-datum")
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
#to get the pos_number from synset 'x' => x=str(synset.name()) x.split('.')[2]
#use x.split('.')[0] to get the name
visited={}
antvisited={}
nkatemexample={}
nkateumdefinition={}
words={}
defkatum={}
doneins={}
exkatum={}
def addhyponyms(katum,wne):
    if not visited.get(wne.name(),False):
        visited[wne.name()]=True
        if (len(wne.hyponyms()))>0:             
            for hypo in wne.hyponyms():
                neword=Getname(hypo)
                word = neword.split('.')[0]
                pos = neword.split('.')[1]
                if(hypo.pos()==wne.pos()):
                    word_priority = neword.split('.')[2]
                    foundkatum = wordroot.Get(word)
                    if words.get(neword,False):
                        newkatum=words[neword]
                    else:
                        newkatum = foundkatum.Get(foundkatum.countI + 1)
                        words[neword]=newkatum
                        pr=priority.Get(word_priority)
                        newkatum._is(pr,check=False)
                    newkatum._is(katum,check=False)
                    if(wne.pos()=='v'):
                        newkatum._is(verb,check=False)
                    elif(wne.pos()=='n'):
                        newkatum._is(noun,check=False)           
                    if hypo.definition():
                        if not nkateumdefinition.get(neword,False):
                            nkateumdefinition[neword]=True
                            de=definition.Get(hypo.definition())
                            newkatum._is(de,check=False)
                    if hypo.examples():
                        if not nkatemexample.get(neword,False):
                            nkatemexample[neword]=True
                            ex=examples.Get(hypo.examples()[0])                            
                            newkatum._is(ex,check=False)
                    if hypo.lemmas()[0].antonyms():
                        antonym=hypo.lemmas()[0].antonyms()[0].synset().name()
                        if not antvisited.get(antonym,False):
                            antvisited[antonym]=True
                            antonymkatum=antonyms.Get(antonyms.countI)
                            antonymstr = str(antonym)
                            antonymword = antonymstr.split('.')[0]
                            foundantkatum = wordroot.Get(antonymword)
                            if words.get(antonymstr,False) :
                                antonymk = words[antonymstr]
                            else :
                                antonymk=foundantkatum.Get(foundantkatum.countI+1)
                                words[antonymstr]=antonymk
                                antonympr = antonymstr.split('.')[2]
                                antonympos = antonymstr.split('.')[1]
                                antonymprk = priority.Get(antonympr)
                                antonymk._is(antonymprk,check=False)
                            newkatum._is(antonymkatum,check=False)
                            antonymk._is(antonymkatum,check=False)
                    addhyponyms(newkatum,hypo)


def addfkatum(katum,wne):
    if not visited.get(wne.name(),False):       
        visited[wne.name()]=True             
        neword=Getname(wne)
        word = neword.split('.')[0]
        pos = neword.split('.')[1]
        word_priority = neword.split('.')[2]
        foundkatum = wordroot.Get(word)
        if words.get(neword,False):
            newkatum=words[neword]
        else:
            newkatum = foundkatum.Get(foundkatum.countI + 1)
            words[neword]=newkatum
            pr=priority.Get(word_priority)
            newkatum._is(pr,check=False)
        newkatum._is(katum,check=False) 
        if wne.definition():
            if not nkateumdefinition.get(neword,False):
                nkateumdefinition[neword]=True
                de=definition.Get(wne.definition())
                newkatum._is(de,check=False)
        if wne.examples():
            if not nkatemexample.get(neword,False):
                nkatemexample[neword]=True
                ex=examples.Get(wne.examples()[0])
                newkatum._is(ex,check=False)
        if wne.lemmas()[0].antonyms():
            antonym=wne.lemmas()[0].antonyms()[0].synset().name()
            if not antvisited.get(antonym,False):
                antvisited[antonym]=True
                antonymkatum=antonyms.Get(antonyms.countI)
                antonymstr = str(antonym)
                antonymword = antonymstr.split('.')[0]
                foundantkatum = wordroot.Get(antonymword)
                if words.get(antonymstr,False) :
                    antonymk = words[antonymstr]
                else :
                    antonymk=foundantkatum.Get(foundantkatum.countI+1)
                    words[antonymstr]=antonymk
                    antonympr = antonymstr.split('.')[2]
                    antonympos = antonymstr.split('.')[1]
                    antonymprk = priority.Get(antonympr)
                    antonymk._is(antonymprk,check=False)
                newkatum._is(antonymkatum,check=False)
                antonymk._is(antonymkatum,check=False)
        return newkatum
    else:    
        return None 
        



def Getname(wne):
    x=wne.name()
    x=str(x)
    return x

def Addexceptions(filename):
    file=open(filename,"r")
    for line in file:
        word=line.split(' ')[1]
        ex=line.split(' ')[0]    
        nkatum = exception.Get(exception.countI + 1)
        word_katum=wordroot.Get(word)
        word_katum._is(nkatum,check=False)
        nkatum.Get(ex)



thing = datum.setup(atum())
wordnet = thing.Get("wordnet")
wordroot = wordnet.Get("wordroot")
noun = wordnet.Get("noun")
verb = wordnet.Get("verb")
adjective = wordnet.Get("adjective")
adverb = wordnet.Get("adverb")
definition = wordnet.Get("definition")
examples = wordnet.Get("examples")
antonyms = wordnet.Get("antonyms")
priority= wordnet.Get("priority")
exception = wordnet.Get("exception")
entity = wordroot.Get("entity")
firstinst = entity.Get(1)
firstinst._is(noun,check=False)
addhyponyms(firstinst,wn.synsets('entity')[0])

for synset in list(wn.all_synsets('v')):
    if(len(synset.hypernyms())==0):     
        nverb= str(synset.name())
        verbword=nverb.split('.')[0]
        verbk = wordroot.Get(verbword)        
        verbins = verbk.Get(verbk.countI+1)
        verbins._is(verb,check=False)
        if synset.definition():
            if not nkateumdefinition.get(verbword,False):
                nkateumdefinition[verbword]=True
                de=definition.Get(synset.definition())                
                verbins._is(de,check=False)
        if synset.examples():
            if not nkatemexample.get(verbword,False):
                nkatemexample[verbword]=True
                ex=examples.Get(synset.examples()[0])
                verbins._is(ex,check=False)
        addhyponyms(verbins,synset)

for synset in list(wn.all_synsets('a')):
    if(len(synset.hypernyms())==0):
        nadjective= str(synset.name())
        adjword=nadjective.split('.')[0]
        adjk = wordroot.Get(adjword)
        nkatum=addfkatum(adjk,synset)
        if(nkatum==None):
            nkatum = adjk.Get(adjk.countI + 1)
        nkatum._is(adjective,check=False)        


for synset in list(wn.all_synsets('r')):
    if(len(synset.hypernyms())==0):
        nadverb= str(synset.name())
        advword=nadverb.split('.')[0]
        advk = wordroot.Get(advword)
        nkatum=addfkatum(advk,synset)
        if(nkatum==None):
            nkatum = advk.Get(advk.countI + 1)
        nkatum._is(adverb,check=False)

Addexceptions("noun.exc")
Addexceptions("adj.exc")
Addexceptions("adv.exc")
Addexceptions("verb.exc")

entity.save('C:/Users/mabde/Desktop/wordnet-datum/wordnet-nolemmas.datum')