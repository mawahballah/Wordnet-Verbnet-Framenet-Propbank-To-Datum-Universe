import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def exactSemType(semanticType):
	queue=deque()
	for sem in semType.I0:
		queue.append(sem)
	while(len(queue)!=0):
		currentElement=queue.popleft()
		currentElementID=id_.of(currentElement)
		if(currentElement.O==semanticType.name and currentElementID.O==semanticType.ID):
			return currentElement
		if(currentElement.countI!=0):
			for instance in currentElement.I0:
				queue.append(instance)
	return None

def exactFE(fnFrameElement):
	mainKatum=frameElement.find(fnFrameElement.name)
	if mainKatum!=None:
		if(mainKatum.countI!=0):		
			for fE in mainKatum.I0:
				fEID=id_.of(fE)
				if(fEID!=None):
					if(fEID.O==fnFrameElement.ID):
						return fE
	return None


def exactlU(fnLexicalUnit):
	lUName=fnLexicalUnit.name.split('.')[0]
	mainKatum=lexicalUnit.find(lUName)
	if mainKatum!=None:
		if(mainKatum.countI!=0):
			for lU in mainKatum.I0:
				lUID=id_.of(lU)
				if(lUID.O==fnLexicalUnit.ID):
					return lU
	return None

def exactFrame(fnFrame):
	frameKatum=frames.find(fnFrame.name)
	if frameKatum!=None:
		return frameKatum
	return None

katum.load('wordnet-verbnet-framenet-semTypes.datum', atum())
generalThing = datum.thing
framenetRoot=generalThing.find("framenet")
frameElement=framenetRoot.find("frame element")
lexicalUnit=framenetRoot.find("lexical unit")
semType=framenetRoot.find("semantic type")
id_=framenetRoot.find("id")
frames=framenetRoot.find("frame")

for fE in fn.fes():
	if fE.semType!=None:
		semanticTypeKatum=exactSemType(fE.semType)
		frameElementkatum=exactFE(fE)
		if(semanticTypeKatum!=None and frameElementkatum!=None):
			frameElementkatum._is(semanticTypeKatum,False)

for lU in fn.lus():
	if len(lU.semTypes)!=0:
		for semTypeInstance in lU.semTypes:
			semanticTypeKatum=exactSemType(semTypeInstance)
			lUkatum=exactlU(lU)
			if(semanticTypeKatum!=None and lUkatum!=None):
				lUkatum._is(semanticTypeKatum,False)

for frame in fn.frames():
	if len(frame.semTypes)!=0:
		for semTypeInstance in frame.semTypes:
			semanticTypeKatum=exactSemType(semTypeInstance)
			frameKatum=exactFrame(frame)
			if(semanticTypeKatum!=None and frameKatum!=None):
				frameKatum._is(semanticTypeKatum,False)

generalThing.save('wordnet-verbnet-framenet.datum')