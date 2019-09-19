#coding:utf-8

import re

def regular(data, LB = None, RB = None):
	rule = str(LB) + r"(.*?)" + str(RB)  
	#rule = r'"id":"(.*)"'
	#pattern1 = re.compile(rule)
	slotList = re.findall(rule, data)
	return slotList
'''

import re

str = "a123b"

print(re.findall(r"a(.+?)b",str))
'''