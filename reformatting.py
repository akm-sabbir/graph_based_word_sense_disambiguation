#!usr/bin/env python
#! -*-coding:utf-8-*-
import os
from collections import defaultdict
class encaptulator(object):
	def __init__(self,name,score,preferred_name,cui,text):
		self.name = name
		self.score = score
		self.preferred_name = preferred_name
		self.cui = cui
		self.text = text
		return
def reformat_data(path_name = 'dataset/fdr_preferred_name.txt'):
	with open(path_name) as data_reader,open('dataset/fdr_preferred_reformatted_name.txt','w+') as data_writer:
		data = data_reader.readlines()
		composed_ob = None
		data_list = dict()
		for datum in data:
			datum_ = datum.split('\t')
			if(composed_ob != None and datum_[0].strip() != composed_ob.name.strip() and len(datum_) == 5 ):
				if(data_list.get(composed_ob.name.strip()) == None):
					data_list[composed_ob.name.strip()] = composed_ob
			if(len(datum_) == 5 and datum_.count('END_OF_DEF') == 0):
				if(composed_ob == None):
					composed_ob =  encaptulator(name = datum_[0],score = datum_[1],preferred_name = datum_[2],text= datum_[3],cui = datum_[4].strip())
				else:
					composed_ob.text += datum_[4]
			elif (len(datum_) == 5 and datum_.count('END_OF_DEF') != 0 ):
				if(composed_ob != None):
					composed_ob.text =composed_ob.text + ' ' + datum_[4]
				else:
					composed_ob =  encaptulator(name = datum_[0],score = datum_[1],preferred_name = datum_[2],text = None,cui = datum_[4].strip())
			elif(len(datum_) == 1 and datum_[0] == 'END_OF_DEF'):
				data_list[composed_ob.name.strip()] = composed_ob
				composed_ob = None
			else:
			 	if(composed_ob != None):
					composed_ob.text += datum_[0].strip()
				else:
				 	composed_ob =  encaptulator(name = datum_[0],score = datum_[1],preferred_name = datum_[2],text= datum_[3],cui = datum_[4].strip())

		for each in data_list:
		  data_writer.write(data_list[each].name+'\t'+data_list[each].score+'\t'+data_list[each].preferred_name+'\t'+data_list[each].cui+'\t'+data_list[each].text)

	

	
	return
if __name__ == '__main__':
	reformat_data()
