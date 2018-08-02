import nltk
from nltk.corpus import propbank as pb
import re
import os
from collections import deque
from xml.etree import ElementTree
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
done={}

def fileGenerator(rolesetString):
	file = open("propbank-examples.xml","a")
	if(ElementTree.tostring(pb.roleset(rolesetString).find('example'))!=None):		
		file.write(ElementTree.tostring(pb.roleset(rolesetString).find('example')).decode('utf8').strip())		
		file.write("\n")
		file.close()


for instance in pb.instances():
	if instance.roleset.split('.')[1] !='XX':
		if not done.get(instance.roleset,False):
			done[instance.roleset]=True
			fileGenerator(instance.roleset)
