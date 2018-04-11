#coding=gbk
import random

raw_input("按Enter开始")

arr = ("1", "0")

def drop():
	a = random.choice(arr)
	b = random.choice(arr)
	c = random.choice(arr)
	global part
	part = a+b+c
	if (part == "110") or (part == "011") or (part == "101"):
		mark1 = "一"#少阳
		print mark1
	elif (part == "001") or (part == "100") or (part == "010"):
		mark2 = "--"#少阴
		print mark2
	elif (part == "111"):
		mark3 = "太阳(变爻-少阴)"
		print mark3
	elif (part == "000"):
		mark4 = "太阴(变爻-少阳)"
		print mark4

for i in range(6):
	drop()