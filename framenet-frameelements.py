import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def exactFrame(frame):
	mainFE=frameElement.find(frame.name)
	if mainFE!=None:
		for mainFEinst in mainFE.I:
			mainFEinstID=id_.of(mainFEinst)
			if mainFEinstID.O == frame.ID:
				return mainFEinst
	return None


katum.load('wordnet-verbnet-framenet-fr.datum', atum())
generalThing = datum.thing
framenetRoot=generalThing.find("framenet")
frameElement=framenetRoot.find("frame element")
id_=framenetRoot.find("id")
relation=framenetRoot.get("relation")
requires=relation.get("requires frame element")
excludes=relation.get("excludes frame element")
for fe in fn.fes():	
	if(fe.excludesFE!=None):
		mainFE=exactFrame(fe)
		excludedFE=exactFrame(fe.excludesFE)
		if(mainFE!=None and excludedFE!=None):
			excludeskatum=excludes.get(excludes.countI)
			mainFE._is(excludeskatum,False)
			excludedFE._is(excludeskatum,False)				
	if(fe.requiresFE!=None):
		mainFE=exactFrame(fe)
		requiredFE=exactFrame(fe.requiresFE)
		if(mainFE!=None and requiredFE!=None):
			requiresKatum=requires.get(requires.countI)
			mainFE._is(requiresKatum,False)
			requiredFE._is(requiresKatum,False)						

generalThing.save('wordnet-verbnet-framenet-fes.datum')