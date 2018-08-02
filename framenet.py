import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union



def addSingleframeElement(frameElementInstance,frameElementValues,frameKatum):
	feDefinition=definition.get(frameElementValues.definition)
	feAbbreviation=abbreviation.get(frameElementValues.abbrev)
	fecoreType=coreType.get(frameElementValues.coreType)
	feID=id_.get(frameElementValues.ID)
	frameElementInstance._is(feID,False)
	frameElementInstance._is(feDefinition,False)
	frameElementInstance._is(feAbbreviation,False)	
	frameElementInstance._is(fecoreType,False)	
	frameKatum._is(frameElementInstance,False)
	
		

def addLexicalUnits(frameKatum,frame):
	for key,value in frame.lexUnit.iteritems():
		luKatum=lexUnit.get(key.split('.')[0])
		luInstance=luKatum.get(luKatum.countI)		
		luPOS=POS.get(value.POS)
		luURL=URL.get(value.URL)
		luDefinition=definition.get(value.definition)
		luID=id_.get(value.ID)
		luInstance._is(luDefinition,False)
		luInstance._is(luURL,False)
		luInstance._is(luID,False)
		luInstance._is(luPOS,False)	
		frameKatum._is(luInstance,False)


def addFrameElements(frameKatum,frame):
	for key,value in frame.FE.iteritems():
		frameElement=FE.get(key)
		frameElementInstance=frameElement.get(frameElement.countI)
		addSingleframeElement(frameElementInstance,value,frameKatum)
		if frame.FEcoreSets!=None:
			for setOfCoreSets in frame.FEcoreSets:
				for value in setOfCoreSets:
					if(value.ID==id_.of(frameElementInstance).O):
						frameElementInstance._is(FEcoreSets)

def handleFrame(frame):
	frameKatum=frame_.get(frame.name)
	frameID=id_.get(frame.ID)
	frameDefinition=definition.get(frame.definition)
	frameURL=URL.get(frame.URL)
	frameKatum._is(frameID,False)
	frameKatum._is(frameDefinition,False)
	frameKatum._is(frameURL,False)	
	addFrameElements(frameKatum,frame)
	addLexicalUnits(frameKatum,frame)

	

katum.load('wordnet-verbnet.datum', atum())
generalThing = datum.thing
Framenetroot=generalThing.get("framenet")
frame_=Framenetroot.get("frame")
id_=Framenetroot.get("id")
URL=Framenetroot.get("URL")
definition=Framenetroot.get("definition")
semTypes=Framenetroot.get("semantic type")
lexUnit=Framenetroot.get("lexical unit")
FE=Framenetroot.get("frame element")
FEcoreSets=Framenetroot.get("frame element core set")
abbreviation=Framenetroot.get("abbreviation")
coreType=Framenetroot.get("core type")
POS=Framenetroot.get("POS")
for frame in fn.frames():
	handleFrame(frame)

generalThing.save('wordnet-verbnet-framenet-noframerelations.datum')