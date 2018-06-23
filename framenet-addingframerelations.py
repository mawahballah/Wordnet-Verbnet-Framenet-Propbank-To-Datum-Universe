import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def addframerelations(frame):
	for framerelation in frame.frameRelations:
		if 'Parent' in framerelation:
			parentkatum=frame_.get(framerelation.Parent.name)
			childkatum=frame_.get(framerelation.Child.name)
			childkatum._is(frameRelations,False)
			childkatum._is(parentkatum,False)
			parentkatum._is(frameRelations,False)


katum.load('wordnet-verbnet-framenet-noframerelations.datum', atum())
generalthing = datum.thing
Framenetroot=generalthing.find("framenet")
frame_=Framenetroot.find("frame")
for frame in frame_.I:
	framenetframe=fn.frame(frame.O)
	for framerelation in framenetframe.frameRelations:
		if 'Parent' in framerelation:
			parentkatum=frame_.find(framerelation.Parent.name)
			if 'Child' in framerelation:
				childkatum=frame_.find(framerelation.Child.name)
				if(parentkatum!=None and childkatum!=None):			
					childkatum._is(parentkatum,False)			




generalthing.save('wordnet-verbnet-framenet-fr.datum')