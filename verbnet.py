import nltk
from nltk.corpus import verbnet as vn
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
classToKatumDict={}
numToClassName={9:"verbs of putting", 10:"verbs of removing",11:"verbs of sending and carrying",12:"verbs of exerting force:push/pull verbs",13:"verbs of change of possession",14:"learn verbs",15:"hold and keep verbs",16:"verbs of concealment",17:"verbs of throwing",18:"verbs of contact by impact",19:"poke verbs",20:"verbs of contact: touch verbs",21:"verbs of cutting",22:"verbs of combining and attaching",23:"verbs of separating and disassembling",24:"verbs of coloring",25:"image creating verbs",26:"verbs of creation and transformation",27:"engender verbs",28:"calve verbs",29:"verbs with predictive complements",30:"verbs of perception",31:"psych-verbs(verbs of psychological state)",32:"verbs of desire",33:"judgment verbs",34:"verbs of assessment",35:"verbs of searching",36:"verbs of social interaction",37:"verbs of communication",38:"verbs of sounds made by animals",39:"verbs of ingesting",40:"verbs involving the body",41:"verbs of grooming and bodily care",42:"verbs killing",43:"verbs of emission",44:"destroy verbs",45:"verbs of change of state",46:"lodge verbs",47:"verbs of existence",48:"verbs of appearance, disappearance, and occurence",49:"verbs of body-internal motion",50:"verbs pf assuming a position",51:"verbs of motion",52:"avoid verbs",53:"verbs of lingering and rushing",54:"measure verbs",55:"aspectual verbs",56:"weekend verbs",57:"weather verbs",58:"verbs of urging and begging",59:"force verbs",60:"order verbs",61:"try verbs",62:"wish verbs",63:"enforce verbs",64:"allow verbs",65:"admit verbs",66:"consume verbs",67:"forbid verbs",68:"pay verbs",69:"refrain verbs",70:"rely verbs",71:"conspire verbs",72:"help verbs",73:"cooperate verbs",74:"succeed verbs",75:"neglect verbs",76:"limit verbs",77:"approve verbs",78:"indicate verbs",79:"dedicate verbs",80:"free verbs",81:"suspect verbs",82:"withdraw verbs",83:"cope verbs",84:"discover verbs",85:"defend verbs",86:"verbs of correlating and relating",87:"verbs of focusing and comprehending",88:"verbs of caring and empathizing",89:"settle verbs",90:"exceed verbs",91:"matter verbs",92:"confine verbs",93:"adopt verbs",94:"risk verbs",95:"acquiesce verbs",96:"addict verbs",97:"verbs of basing and deducing",98:"confront verbs",99:"ensure verbs",100:"own verbs",101:"patent verbs",102:"promote verbs",103:"require verbs",104:"verbs of spending time",105:"use verbs",106:"void verbs",107:"involve verbs",108:"multiply verbs",109:"seem verbs"}
sense_key_regex = r"(.*)\%(.*):(.*):(.*):(.*):(.*)"
synset_types = {1:'n', 2:'v', 3:'a', 4:'r', 5:'s'}

def synsetFromSenseKey(sense_key):
    lemma, ss_type, lex_num, lex_id, head_word, head_id = re.match(sense_key_regex, sense_key).groups()
    ss_idx = '.'.join([lemma, synset_types[int(ss_type)], lex_id])
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
	wordstr=getName(synset)
	definition=wnr.find("definition")
	currentDefinition=synset.definition()
	priority=wnr.find("priority")
	wordroot=wordnetRoot.find("wordroot")
	word = wordstr.split('.')[0]
	wordInDatum=wordroot.find(word)
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
	elif(pos=='s'):
		typ="adjective satellite"
	if(typ!="notfound"):
		if(wordInDatum.countI>0):					
			for instance in wordInDatum.I:
				if(instance.Is(wnr.find(typ))):
					defin=definition.of(instance)
					if(defin!=None):
						if(defin.O==currentDefinition):
							return instance
	return None			

def parseClass(classID):
	args=classID.split('-')
	verb=args[0]
	classID=args[1].split('.')[0]
	return verb,classID

def classToKatum(classID):	
	currentVerbClassID=verbclassID.get(classID.split('-',1)[1])
	verb,classID=parseClass(classID)
	verbClassKatum=verbclass_.get(verb)
	numVerbKatum=verbClassKatum.get(verbClassKatum.countI)
	classKatum=class_.get(numToClassName[int(classID)])		
	numVerbKatum._is(classKatum,False)	
	numVerbKatum._is(currentVerbClassID,False)
	return numVerbKatum


def processSyntax(framesInstance,frame,argumentsKatum):  
	if(len(frame)>0):		
	  	for key,value in frame.iteritems():
	  		if type(value)==list:
	  			newParent=argumentsKatum.get(key)
	  			for v in value:
	  				processSyntax(framesInstance,v,newParent)
	  		elif type(value)==dict:
	  			newParent=argumentsKatum.get(key)
	  			processSyntax(framesInstance,value,newParent)
	 		else:
	  			argumentsInst=argumentsKatum.get(key)  				
	  			argumentsInstValue=argumentsInst.get(value)
	  			framesInstance._is(argumentsInstValue,False)

def processThemRoles(katumClass,classID):
	tRoles=vn.themroles(classID)
	for tRole in tRoles:
		currentRole=themroles.get(themroles.countI)
		katumClass._is(currentRole,False)
		thisRole=roleType.get(tRole.get('type'))
		myRolesLists=tRole.get('modifiers')
		if(len(myRolesLists)==0):
			emptyRole=thisRole.get("")
			currentRole._is(emptyRole,False)
		else:
			for myRolesList in myRolesLists:
				typeKatum=thisRole.get(myRolesList.get('type'))
				valueKatum=typeKatum.get(myRolesList.get('value'))
				currentRole._is(valueKatum,False)


def processDescription(descriptionDictionary,katumClass):
	for key,value in descriptionDictionary.iteritems():
		descriptionInstance=description.get(key)
		descriptionValue=descriptionInstance.get(value)
		katumClass._is(descriptionValue,False)


def processExample(exampleString,katumClass):
	exampleInstance=example.get(exampleString)
	katumClass._is(exampleInstance,False)
	return exampleInstance



def processClass(katumClass,classID):
	frames=vn.frames(classID)	
	for frame in frames:
		syntaxFrames=frame['syntax']
		semanticsFrames=frame['semantics']
		exampleKatum=processExample(frame['example'],katumClass)		
		if(len(syntaxFrames)>0):
			syntaxInstance=syntax.get(syntax.countI)
			exampleKatum._is(syntaxInstance,False)
			for syntaxFrame in syntaxFrames:
				syntaxFramesInstance=syntaxFramesKatum.get(syntaxFramesKatum.countI)
				syntaxInstance._is(syntaxFramesInstance,False)
				processSyntax(syntaxFramesInstance,syntaxFrame,syntaxArguments)		
		if(len(semanticsFrames)>0):
			semanticsInstance=semantics.get(semantics.countI)
			exampleKatum._is(semanticsInstance,False)
			for semanticsFrame in semanticsFrames:
				predicateVal=semanticsFrame.get('predicate_value')
				predicateKatum=predicateValue.get(predicateVal)
				numPredicateKatum=predicateKatum.get(predicateKatum.countI)
				semanticsFramesInstance=semanticsFramesKatum.get(semanticsFramesKatum.countI)
				semanticsInstance._is(semanticsFramesInstance,False)
				semanticsFramesInstance._is(numPredicateKatum,False)
				for argument_ in semanticsFrame.get('arguments'):
					argumentType=semanticsArguments.get(argument_.get('type'))
					argumentValue=argumentType.get(argument_.get('value'))
					numPredicateKatum._is(argumentValue,False)				
		processDescription(frame['description'],exampleKatum)		



def processClassID(classIDs):
	helper="::"
	done=1
	for classID in classIDs:
		numVerbKatum=classToKatum(classID)
		if(len(vn.wordnetids(classID))>0):
			for wordnetInstance in vn.wordnetids(classID):			
				synset=synsetFromSenseKey(wordnetInstance+helper)
				if(synset!=None):
					wordKatum=exactKatumFromSynset(wn.synset(synset),wordnetRoot)
					if(wordKatum!=None):
						wordKatum._is(numVerbKatum,False)
						print done, wordKatum.a0.O,wordKatum.O,numVerbKatum.a0.O,numVerbKatum.O
						done+=1
		classToKatumDict[classID]=numVerbKatum
		processClass(numVerbKatum,classID)
		processThemRoles(numVerbKatum,classID)


katum.load('wordnet-example-definition.datum', atum())
generalThing = datum.thing
verbnetRoot=generalThing.get("verbnet")
wordnetRoot=generalThing.find("wordnet")
class_=verbnetRoot.get("class")
verbclassID=verbnetRoot.get("verb class id")
verbroot=verbnetRoot.get("verbroot")
example=verbnetRoot.get("example")
semantics=verbnetRoot.get("semantics")
syntax=verbnetRoot.get("syntax")
verbclass_=verbnetRoot.get("verb class")
description=verbnetRoot.get("description")
semanticsArguments=verbnetRoot.get("semantics argument")
syntaxArguments=verbnetRoot.get("syntax argument")
syntaxFramesKatum= verbnetRoot.get("syntactic argument")
semanticsFramesKatum= verbnetRoot.get("semantics predicate")
predicateValue=verbnetRoot.get("predicate value")
themroles=verbnetRoot.get("thematic role")
roleType=verbnetRoot.get("role")
listOfAllLemmas=vn.lemmas()
uniqueClassIDs=[]
for lemma in listOfAllLemmas:
	uniqueClassIDs.extend(vn.classids(lemma))
uniqueClassIDs=list(set(uniqueClassIDs))	
processClassID(uniqueClassIDs)
for v in vn.lemmas():
	verbRootInstance=verbroot.get(v)
	for verbclass in vn.classids(v):
		verbRootInstance._is(classToKatumDict[verbclass],False)

generalThing.save('wordnet-verbnet.datum')
