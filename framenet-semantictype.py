import nltk
from nltk.corpus import framenet as fn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union

katum.load('wordnet-verbnet-framenet-fes.datum', atum())
generalThing = datum.thing
framenetRoot=generalThing.find("framenet")
semTypeKatum=framenetRoot.find("semantic type")
id_=framenetRoot.find("id")
definition=framenetRoot.find("definition")
abbreviation=framenetRoot.find("abbreviation")
lexicalType=fn.semtype('Lexical_type')
lexicalTypeKatum=semTypeKatum.get(lexicalType.name)
lexicalTypeDefinition=definition.get(lexicalType.definition)
lexicalTypeKatum._is(lexicalTypeDefinition,False)
lexicalTypeID=id_.get(lexicalType.ID)
lexicalTypeKatum._is(lexicalTypeID,False)
lexicalTypeAbb=abbreviation.get(lexicalType.abbrev)
lexicalTypeKatum._is(lexicalTypeAbb,False)
ontologicalType=fn.semtype('Ontological_type')
ontologicalTypeKatum=semTypeKatum.get(ontologicalType.name)
ontologicalTypeDefinition=definition.get(ontologicalType.definition)
ontologicalTypeKatum._is(ontologicalTypeDefinition,False)
ontologicalTypeID=id_.get(ontologicalType.ID)
ontologicalTypeKatum._is(ontologicalTypeID,False)
ontologicalTypeAbb=abbreviation.get(ontologicalType.abbrev)
ontologicalTypeKatum._is(ontologicalTypeAbb,False)
queue=deque()
queue.append(lexicalTypeKatum)
queue.append(ontologicalTypeKatum)
while(len(queue)!=0):
	currentSemanticType=queue.popleft()
	for childSemantic in fn.semtype(currentSemanticType.O).subTypes:
		childSemanticKatum=currentSemanticType.get(childSemantic.name)
		childSemanticID=id_.get(childSemantic.ID)
		childSemanticDefinition=definition.get(childSemantic.definition)
		childSemanticAbb=abbreviation.get(childSemantic.abbrev)
		childSemanticKatum._is(childSemanticID,False)
		childSemanticKatum._is(childSemanticAbb,False)
		childSemanticKatum._is(childSemanticDefinition,False)
		queue.append(childSemanticKatum)


generalThing.save('wordnet-verbnet-framenet-semtypes.datum')