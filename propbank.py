import nltk
from nltk.corpus import propbank as pb
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
done={}
doneCount=1
def addRoleSet(name):
	global doneCount
	roleSetMainName=name.split('.')[0]
	roleSetMainKatum=roleset.get(roleSetMainName)
	roleSetNewKatum=roleSetMainKatum.get(roleSetMainKatum.countI)
	rolesetsensenum=senseNumber.get(name.split('.')[1])
	roleSetNewKatum._is(rolesetsensenum,False)	
	if(pb.roleset(name)!=None):
		verbnetCls=pb.roleset(name).get('vncls')
		if(verbnetCls!=None):
			verbnetID=verbClassID.find(verbnetCls)
			if(verbnetID!=None):
				for vnClass in verbnetID.I:
					roleSetNewKatum._is(vnClass,False)
					print doneCount,vnClass.a0.O,vnClass.O,roleSetMainKatum.O,roleSetNewKatum.O
					doneCount+=1
		roleSetMeaning=pb.roleset(name).get('name')
		if(roleSetMeaning!=None):
			roleSetMeaningKatum=meaning.get(roleSetMeaning)
			roleSetNewKatum._is(roleSetMeaningKatum,False)
		for role in pb.roleset(name).findall("roles/role"):
			argCount=role.attrib['n']
			argName=role.attrib['descr']
			if argCount != None and argName!=None:
				argumentKatum=argument.get(argName)
				argumentNameNumKatum=argumentKatum.get(argumentKatum.countI)
				argNumKatum=argumentNumber.get(argCount)
				argumentNameNumKatum._is(argNumKatum,False)
				roleSetNewKatum._is(argumentNameNumKatum,False)


katum.load('wordnet-verbnet-framenet.datum', atum())
generalThing = datum.thing
verbnetRoot=generalThing.find("verbnet")
verbClassID=verbnetRoot.find("verb class id")
propbank=generalThing.get("propbank")
senseNumber=propbank.get("sense number")
roleset=propbank.get("role set")
argument=propbank.get("argument")
argumentNumber=propbank.get("argument number")
meaning=propbank.get("meaning")
for instance in pb.instances():
	if instance.roleset.split('.')[1] !='XX':
		if not done.get(instance.roleset,False):
			done[instance.roleset]=True
			addRoleSet(instance.roleset)


generalThing.save('wordnet-verbnet-framenet-propbank.datum')