import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def exactsemtype(semantictype):
	queue=deque()
	for sem in semtype.I0:
		queue.append(sem)
	while(len(queue)!=0):
		currentelement=queue.popleft()
		currentelementid=id_.of(currentelement)
		if(currentelement.O==semantictype.name and currentelementid.O==semantictype.ID):
			return currentelement
		if(currentelement.countI!=0):
			for instance in currentelement.I0:
				queue.append(instance)
	return None

def exactfe(fnframeelement):
	mainkatum=frameelement.find(fnframeelement.name)
	if mainkatum!=None:
		if(mainkatum.countI!=0):		
			for fe in mainkatum.I0:
				feid=id_.of(fe)
				if(feid!=None):
					if(feid.O==fnframeelement.ID):
						return fe
	return None


def exactlu(fnlexicalunit):
	luname=fnlexicalunit.name.split('.')[0]
	mainkatum=lexicalunit.find(luname)
	if mainkatum!=None:
		if(mainkatum.countI!=0):
			for lu in mainkatum.I0:
				luid=id_.of(lu)
				if(luid.O==fnlexicalunit.ID):
					return lu
	return None

def exactframe(fnframe):
	framekatum=frames.find(fnframe.name)
	if framekatum!=None:
		return framekatum
	return None

katum.load('wordnet-verbnet-framenet-semtypes.datum', atum())
generalthing = datum.thing
Framenetroot=generalthing.find("framenet")
frameelement=Framenetroot.find("frame element")
lexicalunit=Framenetroot.find("lexical unit")
semtype=Framenetroot.find("semantic type")
id_=Framenetroot.find("id")
frames=Framenetroot.find("frame")

for fe in fn.fes():
	if fe.semType!=None:
		semantictypekatum=exactsemtype(fe.semType)
		frameelementkatum=exactfe(fe)
		if(semantictypekatum!=None and frameelementkatum!=None):
			frameelementkatum._is(semantictypekatum,False)

for lu in fn.lus():
	if len(lu.semTypes)!=0:
		for semtypeinstance in lu.semTypes:
			semantictypekatum=exactsemtype(semtypeinstance)
			lukatum=exactlu(lu)
			if(semantictypekatum!=None and lukatum!=None):
				lukatum._is(semantictypekatum,False)

for frame in fn.frames():
	if len(frame.semTypes)!=0:
		for semtypeinstance in frame.semTypes:
			semantictypekatum=exactsemtype(semtypeinstance)
			framekatum=exactframe(frame)
			if(semantictypekatum!=None and framekatum!=None):
				framekatum._is(semantictypekatum,False)

generalthing.save('wordnet-verbnet-framenet.datum')