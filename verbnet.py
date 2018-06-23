import nltk
from nltk.corpus import verbnet as vn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
classtokatumdict={}
numtoclassname={9:"verbs of putting", 10:"verbs of removing",11:"verbs of sending and carrying",12:"verbs of exerting force:push/pull verbs",13:"verbs of change of possession",14:"learn verbs",15:"hold and keep verbs",16:"verbs of concealment",17:"verbs of throwing",18:"verbs of contact by impact",19:"poke verbs",20:"verbs of contact: touch verbs",21:"verbs of cutting",22:"verbs of combining and attaching",23:"verbs of separating and disassembling",24:"verbs of coloring",25:"image creating verbs",26:"verbs of creation and transformation",27:"engender verbs",28:"calve verbs",29:"verbs with predictive complements",30:"verbs of perception",31:"psych-verbs(verbs of psychological state)",32:"verbs of desire",33:"judgment verbs",34:"verbs of assessment",35:"verbs of searching",36:"verbs of social interaction",37:"verbs of communication",38:"verbs of sounds made by animals",39:"verbs of ingesting",40:"verbs involving the body",41:"verbs of grooming and bodily care",42:"verbs killing",43:"verbs of emission",44:"destroy verbs",45:"verbs of change of state",46:"lodge verbs",47:"verbs of existence",48:"verbs of appearance, disappearance, and occurence",49:"verbs of body-internal motion",50:"verbs pf assuming a position",51:"verbs of motion",52:"avoid verbs",53:"verbs of lingering and rushing",54:"measure verbs",55:"aspectual verbs",56:"weekend verbs",57:"weather verbs",58:"verbs of urging and begging",59:"force verbs",60:"order verbs",61:"try verbs",62:"wish verbs",63:"enforce verbs",64:"allow verbs",65:"admit verbs",66:"consume verbs",67:"forbid verbs",68:"pay verbs",69:"refrain verbs",70:"rely verbs",71:"conspire verbs",72:"help verbs",73:"cooperate verbs",74:"succeed verbs",75:"neglect verbs",76:"limit verbs",77:"approve verbs",78:"indicate verbs",79:"dedicate verbs",80:"free verbs",81:"suspect verbs",82:"withdraw verbs",83:"cope verbs",84:"discover verbs",85:"defend verbs",86:"verbs of correlating and relating",87:"verbs of focusing and comprehending",88:"verbs of caring and empathizing",89:"settle verbs",90:"exceed verbs",91:"matter verbs",92:"confine verbs",93:"adopt verbs",94:"risk verbs",95:"acquiesce verbs",96:"addict verbs",97:"verbs of basing and deducing",98:"confront verbs",99:"ensure verbs",100:"own verbs",101:"patent verbs",102:"promote verbs",103:"require verbs",104:"verbs of spending time",105:"use verbs",106:"void verbs",107:"involve verbs",108:"multiply verbs",109:"seem verbs"}
def parseclass(classid):
	args=classid.split('-')
	verb=args[0]
	classid=args[1].split('.')[0]
	return verb,classid

def classtokatum(classid):
	verb,classid=parseclass(classid)
	verbclasskatum=verbclass_.get(verb)
	num_verbkatum=verbclasskatum.get(verbclasskatum.countI)
	classkatum=class_.get(numtoclassname[int(classid)])
	num_verbkatum._is(classkatum,False)
	return num_verbkatum


def processsyntax(framesinstance,frame,argumentskatum):  
	if(len(frame)>0):		
	  	for key,value in frame.iteritems():
	  		if type(value)==list:
	  			newparent=argumentskatum.get(key)
	  			for v in value:
	  				processsyntax(framesinstance,v,newparent)
	  		elif type(value)==dict:
	  			newparent=argumentskatum.get(key)
	  			processsyntax(framesinstance,value,newparent)
	 		else:
	  			argumentsinst=argumentskatum.get(key)  				
	  			argumentsinstvalue=argumentsinst.get(value)
	  			framesinstance._is(argumentsinstvalue,False)

def processthemaroles(katumclass,classid):
	troles=vn.themroles(classid)
	for trole in troles:
		currole=themroles.get(themroles.countI)
		katumclass._is(currole,False)
		thisrole=roletype.get(trole.get('type'))
		myroleslists=trole.get('modifiers')
		if(len(myroleslists)==0):
			emptyrole=thisrole.get("")
			currole._is(emptyrole,False)
		else:
			for myroleslist in myroleslists:
				typek=thisrole.get(myroleslist.get('type'))
				valuek=typek.get(myroleslist.get('value'))
				currole._is(valuek,False)


def processdescription(description_dictionary,katumclass):
	for key,value in description_dictionary.iteritems():
		descriptioninst=description.get(key)
		descriptionvalue=descriptioninst.get(value)
		katumclass._is(descriptionvalue,False)


def processexample(examplestring,katumclass):
	exampleinsta=example.get(examplestring)
	katumclass._is(exampleinsta,False)
	return exampleinsta



def processclass(katumclass,classid):
	frames=vn.frames(classid)	
	for frame in frames:
		syntaxframes=frame['syntax']
		semanticsframes=frame['semantics']
		examplekatum=processexample(frame['example'],katumclass)		
		if(len(syntaxframes)>0):
			syntaxinstance=syntax.get(syntax.countI)
			examplekatum._is(syntaxinstance,False)
			for syntaxframe in syntaxframes:
				syntaxframesinstance=syntaxframeskatum.get(syntaxframeskatum.countI)
				syntaxinstance._is(syntaxframesinstance,False)
				processsyntax(syntaxframesinstance,syntaxframe,syntaxarguments)		
		if(len(semanticsframes)>0):
			semanticsinstance=semantics.get(semantics.countI)
			examplekatum._is(semanticsinstance,False)
			for semanticsframe in semanticsframes:
				predicatev=semanticsframe.get('predicate_value')
				predkatumn=predicatevalue.get(predicatev)
				predkatum=predkatumn.get(predkatumn.countI)
				semanticsframesinstance=semanticsframeskatum.get(semanticsframeskatum.countI)
				semanticsinstance._is(semanticsframesinstance,False)
				semanticsframesinstance._is(predkatum,False)
				for argument_ in semanticsframe.get('arguments'):
					argumenttype=semanticsarguments.get(argument_.get('type'))
					argumentvalue=argumenttype.get(argument_.get('value'))
					predkatum._is(argumentvalue,False)				
		processdescription(frame['description'],examplekatum)		



def processclassid(classids):
	for classid in classids:
		num_verbkatum=classtokatum(classid)
		classtokatumdict[classid]=num_verbkatum
		processclass(num_verbkatum,classid)
		processthemaroles(num_verbkatum,classid)



katum.load('wordnet.datum', atum())
generalthing = datum.thing
verbnetroot=generalthing.get("verbnet")
class_=verbnetroot.get("class")
verbroot=verbnetroot.get("verbroot")
example=verbnetroot.get("example")
semantics=verbnetroot.get("semantics")
syntax=verbnetroot.get("syntax")
verbclass_=verbnetroot.get("verb class")
description=verbnetroot.get("description")
semanticsarguments=verbnetroot.get("semantics argument")
syntaxarguments=verbnetroot.get("syntax argument")
syntaxframeskatum= verbnetroot.get("syntactic argument")
semanticsframeskatum= verbnetroot.get("semantics predicate")
predicatevalue=verbnetroot.get("predicate value")
themroles=verbnetroot.get("thematic role")
roletype=verbnetroot.get("role")
listofallelammas=vn.lemmas()
uniqueclassids=[]
for lemma in listofallelammas:
	uniqueclassids.extend(vn.classids(lemma))
uniqueclassids=list(set(uniqueclassids))	
processclassid(uniqueclassids)
for v in vn.lemmas():
	verbrootinstance=verbroot.get(v)
	for verbclass in vn.classids(v):
		verbrootinstance._is(classtokatumdict[verbclass],False)

generalthing.save('wordnet-verbnet.datum')