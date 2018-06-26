import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

katum.load('wordnet-verbnet-framenet-fes.datum', atum())
generalthing = datum.thing
Framenetroot=generalthing.find("framenet")
semtypekatum=Framenetroot.find("semantic type")
id_=Framenetroot.find("id")
definition=Framenetroot.find("definition")
abbreviation=Framenetroot.find("abbreviation")
lexicaltype=fn.semtype('Lexical_type')
lexicaltypekatum=semtypekatum.get(lexicaltype.name)
lexicaltypedefinition=definition.get(lexicaltype.definition)
lexicaltypekatum._is(lexicaltypedefinition,False)
lexicaltypeid=id_.get(lexicaltype.ID)
lexicaltypekatum._is(lexicaltypeid,False)
lexicaltypeabb=abbreviation.get(lexicaltype.abbrev)
lexicaltypekatum._is(lexicaltypeabb,False)
ontologicaltype=fn.semtype('Ontological_type')
ontologicaltypekatum=semtypekatum.get(ontologicaltype.name)
ontologicaltypedefinition=definition.get(ontologicaltype.definition)
ontologicaltypekatum._is(ontologicaltypedefinition,False)
ontologicaltypeid=id_.get(ontologicaltype.ID)
ontologicaltypekatum._is(ontologicaltypeid,False)
ontologicaltypeabb=abbreviation.get(ontologicaltype.abbrev)
ontologicaltypekatum._is(ontologicaltypeabb,False)
queue=deque()
queue.append(lexicaltypekatum)
queue.append(ontologicaltypekatum)
while(len(queue)!=0):
	currentsemantictype=queue.popleft()
	for childsemantic in fn.semtype(currentsemantictype.O).subTypes:
		childsemantickatum=currentsemantictype.get(childsemantic.name)
		childsemanticid=id_.get(childsemantic.ID)
		childsemanticdefinition=definition.get(childsemantic.definition)
		childsemanticabb=abbreviation.get(childsemantic.abbrev)
		childsemantickatum._is(childsemanticid,False)
		childsemantickatum._is(childsemanticabb,False)
		childsemantickatum._is(childsemanticdefinition,False)
		queue.append(childsemantickatum)


generalthing.save('wordnet-verbnet-framenet-semtypes.datum')