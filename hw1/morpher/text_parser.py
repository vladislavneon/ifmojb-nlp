#text_parser.py

def check_punct(symbol):
	if ((symbol == '.') or
		(symbol == '?') or
		(symbol == '!') or
		(symbol == ',')):
		return True
	else:
		return False

def parse_sentence_to_tokens_wpunct(sentence):
	pure_list = sentence.strip().split(sep = ' ')
	res_list = []
	for token in pure_list:
		last_symbol = token[-1]
		if (check_punct(last_symbol)):
			last = 0
			while (check_punct(token[last - 1])):
				last -= 1
			res_list.append(token[:last])
			res_list.append(last_symbol)
		else:
			res_list.append(token)
	return res_list
	
def parse_sentence_to_tokens(sentence):
	pure_list = sentence.strip().lower().split(sep = ' ')
	res_list = []
	for token in pure_list:
		last_symbol = token[-1]
		if (check_punct(last_symbol)):
			last = 0
			while (check_punct(token[last - 1])):
				last -= 1
			res_list.append(token[:last])
		else:
			res_list.append(token)
	return res_list

def parse_text(input_file, output_file):
	textfile = open(input_file, "r")
	parsedfile = open(output_file, "w")
	for sentence in textfile:
		list_of_tokens = parse_sentence_to_tokens_wpunct(sentence)
		for token in list_of_tokens:
			parsedfile.write(token + " ")
		parsedfile.write("\n")
	textfile.close()
	parsedfile.close()

	
def build_dict(input_file):
	map = {}
	textfile = open(input_file, "r")
	for sentence in textfile:
		add_sentence_to_map(sentence, map)
	textfile.close()
	return map
	
def add_sentence_to_map(sentence, map):
	tokens = parse_sentence_to_tokens(sentence)
	for word in tokens:
		if (word not in map):
			map[word] = []
	


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