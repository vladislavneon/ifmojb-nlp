#odict_search.py

def create_dict_with_odict(dict):
	odict = open("odict.csv", "r")
	for entry in odict:
		words = entry.strip().lower().split(sep = ',')
		lemma = words[0]
		odict_pos = words[1]
		words.pop(1)
		pos = convert_odict_pos(odict_pos)
		for word in words:
			if (word in dict):
				cur_tuple = lemma, pos
				if (cur_tuple not in dict[word]):
					dict[word].append((lemma, pos))
	odict.close()
				
def convert_odict_pos(op):
	if (op == "м"):
		res = "S"
	elif (op == "ж"):
		res = "S"
	elif (op == "мо"):
		res = "S"
	elif (op == "жо"):
		res = "S"
	elif (op == "с"):
		res = "S"
	elif (op == "со"):
		res = "S"
	elif (op == "мо-жо"):
		res = "S"
	elif (op == "мн."):
		res = "S"
	elif (op == "п"):
		res = "A"
	elif (op == "сравн."):
		res = "A"
	elif (op == "числ.-п"):
		res = "A"
	elif (op == "мс-п"):
		res = "A"
	elif (op == "союз"):
		res = "CONJ"
	elif (op == "межд."):
		res = "ADV"
	elif (op == "част."):
		res = "ADV"
	elif (op == "н"):
		res = "ADV"
	elif (op == "вводн."):
		res = "ADV"
	elif (op == "предик."):
		res = "ADV"
	elif (op == "св"):
		res = "V"
	elif (op == "нсв"):
		res = "V"
	elif (op == "св-нсв"):
		res = "V"
	elif (op == "предл."):
		res = "PR"
	elif (op == "числ."):
		res = "NUM"
	elif (op == ""):
		res = ""
	else:
		res = "NI"
	return res
	
def print_all_tags(output_file):
	odict = open("odict.csv", "r")
	output = open(output_file, "w")
	tags = {}
	for entry in odict:
		words = entry.strip().lower().split(sep = ',')
		lemma = words[0]
		odict_pos = words[1]
		if (odict_pos in tags):
			if (len(tags[odict_pos]) < 4):
				tags[odict_pos].append(lemma)
		else:
			tags[odict_pos] = [lemma]
	for tag, lemmas in tags.items():
		res = tag + ' : '
		for lemma in lemmas:
			res += lemma + ' '
		res += '\n'
		output.write(res)
	odict.close()
	output.close()


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