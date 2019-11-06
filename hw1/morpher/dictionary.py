def print_dict(dict, output_file):
	ouf = open(output_file, "w")
	for word, lemmas in dict.items():
		if (len(lemmas) == 0):
			res = "NI;"
		elif (len(lemmas) == 1):
			res = "OK;"
		else:
			res = "AM;"
		res += word
		for lemma, pos in lemmas:
			res += ';'
			res += lemma
			res += '='
			res += pos
		res += '\n'
		ouf.write(res)
	ouf.close()
		
def print_dict_debug(dict, output_file):
	ouf = open(output_file, "w")
	for word, lemmas in dict.items():
		flag = False
		if (len(lemmas) == 0):
			res = "NI;"
			flag = True
		elif (len(lemmas) == 1):
			res = "OK;"
		else:
			res = "AM;"
		res += word
		for lemma, pos in lemmas:
			if (pos == "NI"):
				flag = True
				res += ';'
				res += lemma
				res += '='
				res += pos
		res += '\n'
		if (flag == True):
			ouf.write(res)
	ouf.close()
		
'''
dict = {}
dict["green"] = [("green", "adj")]
dict["cars"] = [("car", "noun"), ("carse", "verb")]
dict["joik"] = []
		
print_dict(dict)
'''

'''
inf = open("input.txt", "r")
ouf = open("output.txt", "w")

a = [[0, 0] for i in range(12)]
for string in inf:
	values = string.split()
	class_num = int(values[0])
	height = int(values[2])
	a[class_num][0] += 1
	a[class_num][1] += height
	
for i in range(1, 12):
	ouf.write(str(i) + " ")
	if (a[i][0] == 0):
		ouf.write("-\n")
	else:
		avg = a[i][1] / a[i][0]
		ouf.write(str(avg) + "\n")
		
inf.close()
ouf.close()
'''