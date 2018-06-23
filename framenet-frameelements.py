import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def exactframe(frame):
	mainfe=frameelement.find(frame.name)
	if mainfe!=None:
		for mainfeinst in mainfe.I:
			mainfeinstID=id_.of(mainfeinst)
			if mainfeinstID.O == frame.ID:
				return mainfeinst
	return None


katum.load('wordnet-verbnet-framenet-fr.datum', atum())
generalthing = datum.thing
Framenetroot=generalthing.find("framenet")
frameelement=Framenetroot.find("frame element")
id_=Framenetroot.find("id")
Relation=Framenetroot.get("Relation")
requires=Relation.get("requires frame element")
excludes=Relation.get("excludes frame element")
for fe in fn.fes():	
	if(fe.excludesFE!=None):
		mainfe=exactframe(fe)
		excludedfe=exactframe(fe.excludesFE)
		if(mainfe!=None and excludedfe!=None):
			excludeskatum=excludes.get(excludes.countI)
			mainfe._is(excludeskatum,False)
			excludedfe._is(excludeskatum,False)				
	if(fe.requiresFE!=None):
		mainfe=exactframe(fe)
		requiredfe=exactframe(fe.requiresFE)
		if(mainfe!=None and requiredfe!=None):
			requireskatum=requires.get(requires.countI)
			mainfe._is(requireskatum,False)
			requiredfe._is(requireskatum,False)						

generalthing.save('wordnet-verbnet-framenet-fes.datum')