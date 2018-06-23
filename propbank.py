import nltk
from nltk.corpus import propbank as pb
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
done={}
def addroleset(name):
	rolesetmainname=name.split('.')[0]
	rolesetmainkatum=roleset.get(rolesetmainname)
	rolesetnewkatum=rolesetmainkatum.get(rolesetmainkatum.countI)
	rolesetsensenum=sensenumber.get(name.split('.')[1])
	rolesetnewkatum._is(rolesetsensenum,False)
	if(pb.roleset(name)!=None):
		rolesetmeaning=pb.roleset(name).get('name')
		if(rolesetmeaning!=None):
			rolesetmeaningkatum=meaning.get(rolesetmeaning)
			rolesetnewkatum._is(rolesetmeaningkatum,False)
		for role in pb.roleset(name).findall("roles/role"):
			argcount=role.attrib['n']
			argname=role.attrib['descr']
			if argcount != None and argname!=None:
				argumentkatum=argument.get(argname)
				argumentnamenumkatum=argumentkatum.get(argumentkatum.countI)
				argnumkatum=argumentnumber.get(argcount)
				argumentnamenumkatum._is(argnumkatum,False)
				rolesetnewkatum._is(argumentnamenumkatum,False)


katum.load('wordnet-verbnet-framenet.datum', atum())
generalthing = datum.thing
propbank=generalthing.get("propbank")
sensenumber=propbank.get("sense number")
roleset=propbank.get("role set")
argument=propbank.get("argument")
argumentnumber=propbank.get("argument number")
meaning=propbank.get("meaning")

for instance in pb.instances():
	if instance.roleset.split('.')[1] !='XX':
		if not done.get(instance.roleset,False):
			done[instance.roleset]=True
			addroleset(instance.roleset)


generalthing.save('wordnet-verbnet-framenet-propbank.datum')