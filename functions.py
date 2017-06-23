#! /usr/bin/env python
import json

#Modify value representation in the form of bytes to KB, MB, GB or TB as needed
def show_as_xb(value, operator):
	defs = {'KB':1024, 'MB':1024*1024, 'GB':1024*1024*1024, 'TB':1024*1024*1024*1024}
	output = float(value) / defs[operator]
	return '{:.2f} {}'.format(output, operator)

#Formats seconds to minutes
def format_as(value):
	pass
	
#return average of a list of int or long values
def find_average(valueList):
	return reduce(lambda x, y: float(x) + float(y), valueList) / len(valueList)

#Returns a dictionary with all the number of times each item in the set is present
#inside the provided list
def find_occurrences(itemSet, itemList):
	output_dict = {}
	for item in itemSet:
		output_dict[item] = itemList.count(item)
	return output_dict

	
