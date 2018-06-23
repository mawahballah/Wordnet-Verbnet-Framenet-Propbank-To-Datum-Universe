import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union



def addsingleframeelement(frameelementinstance,frameelementvalues,framekatum):
	fedefinition=definition.get(frameelementvalues.definition)
	feabbreviation=abbreviation.get(frameelementvalues.abbrev)
	fecoretype=coretype.get(frameelementvalues.coreType)
	fe_id=id_.get(frameelementvalues.ID)
	frameelementinstance._is(fe_id,False)
	frameelementinstance._is(fedefinition,False)
	frameelementinstance._is(feabbreviation,False)	
	frameelementinstance._is(fecoretype,False)	
	framekatum._is(frameelementinstance,False)
	
		

def addlexicalunits(framekatum,frame):
	for key,value in frame.lexUnit.iteritems():
		lukatum=lexUnit.get(key.split('.')[0])
		luinstance=lukatum.get(lukatum.countI)		
		lupos=POS.get(value.POS)
		luURL=URL.get(value.URL)
		ludefinition=definition.get(value.definition)
		luid=id_.get(value.ID)
		luinstance._is(ludefinition,False)
		luinstance._is(luURL,False)
		luinstance._is(luid,False)
		luinstance._is(lupos,False)	
		framekatum._is(luinstance,False)


def addframeelements(framekatum,frame):
	for key,value in frame.FE.iteritems():
		frameelement=FE.get(key)
		frameelementinstance=frameelement.get(frameelement.countI)
		addsingleframeelement(frameelementinstance,value,framekatum)
		if frame.FEcoreSets!=None:
			for setofcoresets in frame.FEcoreSets:
				for value in setofcoresets:
					if(value.ID==id_.of(frameelementinstance).O):
						frameelementinstance._is(FEcoreSets)

def handleframe(frame):
	framekatum=frame_.get(frame.name)
	frameid=id_.get(frame.ID)
	framedefinition=definition.get(frame.definition)
	frameurl=URL.get(frame.URL)
	framekatum._is(frameid,False)
	framekatum._is(framedefinition,False)
	framekatum._is(frameurl,False)	
	addframeelements(framekatum,frame)
	addlexicalunits(framekatum,frame)

	

katum.load('wordnet-verbnet.datum', atum())
generalthing = datum.thing
Framenetroot=generalthing.get("framenet")
frame_=Framenetroot.get("frame")
id_=Framenetroot.get("id")
URL=Framenetroot.get("URL")
definition=Framenetroot.get("definition")
semtypes=Framenetroot.get("semantic type")
lexUnit=Framenetroot.get("lexical unit")
FE=Framenetroot.get("frame element")
FEcoreSets=Framenetroot.get("frame element core set")
abbreviation=Framenetroot.get("abbreviation")
coretype=Framenetroot.get("core type")
POS=Framenetroot.get("POS")
for frame in fn.frames():
	handleframe(frame)

generalthing.save('wordnet-verbnet-framenet-noframerelations.datum')