import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def addframeRelations(frame):
	for frameRelation in frame.frameRelations:
		if 'Parent' in frameRelation:
			parentKatum=frame_.get(frameRelation.Parent.name)
			childKatum=frame_.get(frameRelation.Child.name)
			childKatum._is(frameRelations,False)
			childKatum._is(parentKatum,False)
			parentKatum._is(frameRelations,False)


katum.load('wordnet-verbnet-framenet-noframeRelations.datum', atum())
generalThing = datum.thing
framenetRoot=generalThing.find("framenet")
frame_=framenetRoot.find("frame")
for frame in frame_.I:
	framenetFrame=fn.frame(frame.O)
	for frameRelation in framenetFrame.frameRelations:
		if 'Parent' in frameRelation:
			parentKatum=frame_.find(frameRelation.Parent.name)
			if 'Child' in frameRelation:
				childKatum=frame_.find(frameRelation.Child.name)
				if(parentKatum!=None and childKatum!=None):			
					childKatum._is(parentKatum,False)			




generalThing.save('wordnet-verbnet-framenet-fr.datum')