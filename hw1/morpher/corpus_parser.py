def check_bad_type(type):
	if (type == "PUNCT"):
		return True
	elif (type == "X"):
		return True
	else:
		return False

def parse_corpus():
	corpus = open("corpus.txt", "r")
	out = open("parsed_corpus.txt", "w")
	for line in corpus:
		line = line.strip().replace('_', '')
		tokens = line.split()
		if ((len(tokens) >= 4) and (not check_bad_type(tokens[3]))):
			for i in range(1, 4):
				out.write(tokens[i] + " ")
			out.write("\n")
	corpus.close()
	out.close()
		
def tags():
	file = open("parsed_corpus.txt", "r")
	out = open("tags_synt.txt", "w")
	s = {}
	for line in file:
		tags = line.strip().split()
		tag = tags[2]
		if (tag in s):
			if (len(s[tag]) < 3):
				s[tag].append(tags[1])
		else:
			s[tag] = [tags[1]]
	for tag, words in s.items():
		out.write(tag + " ")
		for word in words:
			out.write(word + " ")
		out.write("\n")
		
def convert_tag(tag):
	if (tag == "NOUN"):
		res = "S"
	elif (tag == "VERB"):
		res = "V"
	elif (tag == "PART"):
		res = "ADV"
	elif (tag == "ADP"):
		res = "PR"
	elif (tag == "ADJ"):
		res = "A"
	elif (tag == "PROPN"):
		res = "S"
	elif (tag == "INTJ"):
		res = "ADV"
	else:
		res = tag
	return res
		
def create_pos_only_stat():
	file = open("parsed_oc+synt.txt", "r")
	out = open("stats_oc+synt.txt", "w")
	stats = {}
	for line in file:
		entry = line.strip().split()
		word = entry[0].lower()
		tag = convert_tag(entry[2])
		if (word in stats):
			if (tag in stats[word]):
				stats[word][tag] += 1
			else:
				stats[word][tag] = 1
		else:
			stats[word] = {}
			if (tag in stats[word]):
				stats[word][tag] += 1
			else:
				stats[word][tag] = 1
	for word in stats:
		for tag in stats[word]:
			res = word + ";" + tag + ";" + str(stats[word][tag]) + "\n"
			out.write(res)
	file.close()
	out.close()
	
def create_best_lemma_pos_stat():
	file = open("parsed_oc+synt.txt", "r")
	out = open("stats_hard_oc+synt.txt", "w")
	stats = {}
	for line in file:
		entry = line.strip().split()
		word = entry[0].lower()
		lemma = entry[1].lower()
		tag = convert_tag(entry[2])
		if (word in stats):
			if ((lemma, tag) in stats[word]):
				stats[word][(lemma, tag)] += 1
			else:
				stats[word][(lemma, tag)] = 1
		else:
			stats[word] = {}
			if ((lemma, tag) in stats[word]):
				stats[word][(lemma, tag)] += 1
			else:
				stats[word][(lemma, tag)] = 1
	for word in stats:
		pairs = stats[word]
		best_freq = 0
		for cur_lemma, cur_pos in pairs:
			cur_freq = pairs[(cur_lemma, cur_pos)]
			#out.write(str(cur_lemma) + " " + str(cur_pos) + " " + str(cur_freq) + "\n")
			if (cur_freq > best_freq):
				best_freq = cur_freq
				lemma = cur_lemma
				pos = cur_pos
		res_str = word + ";" + lemma + ";" + pos + ";" + str(best_freq) + "\n"
		out.write(res_str)
	file.close()
	out.close()
	
create_best_lemma_pos_stat()
			

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