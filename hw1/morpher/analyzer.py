#analyzer.py

import text_parser as TextParser
import random

def process_text(input_file, output_file, dict, stats, method_name):
	text = open(input_file, "r")
	output = open(output_file, "w")
	random.seed()
	output.write(method_name)
	for sentence in text:
		result = process_sentence(sentence, dict, stats)
		for initial_word, lemma, pos in result:
			cur = initial_word + '{' + lemma + '=' + pos + '} '
			output.write(cur)
		output.write('\n')
	text.close()
	output.close()
		
def process_sentence(sentence, dict, stats):
	words = TextParser.parse_sentence_to_tokens_wpunct(sentence)
	result = []
	for word in words:
		if (not TextParser.check_punct(word)):
			initial_word = word
			word = word.lower()
			lemmas = dict[word]
			lemma, pos = get_best_lemma_hard_stats(word, lemmas, stats)
			result.append((initial_word, lemma, pos))
	return result
	
def get_best_lemma_first(word, lemmas):
	if (len(lemmas) == 0):
		lemma = word
		pos = "S"
	elif (len(lemmas) == 1):
		lemma, pos = lemmas[0]
	else:
		lemma, pos = lemmas[0]
	return lemma, pos

def get_best_lemma_random(word, lemmas):
	if (len(lemmas) == 0):
		lemma = word
		pos = "S"
	elif (len(lemmas) == 1):
		lemma, pos = lemmas[0]
	else:
		num = random.randrange(0, len(lemmas))
		lemma, pos = lemmas[num]
	return lemma, pos
	
def get_best_lemma_stats(word, lemmas, stats):
	if (len(lemmas) == 0):
		lemma = word
		pos = "S"
	else:
		num = random.randrange(0, len(lemmas))
		lemma, pos = lemmas[num]
		if (word in stats):
			best_freq = 0
			for cur_lemma, cur_pos in lemmas:
				if (cur_pos in stats[word]):
					cur_freq = stats[word][cur_pos]
					if (cur_freq > best_freq):
						best_freq = cur_freq
						lemma = cur_lemma
						pos = cur_pos
	return lemma, pos
	
def get_best_lemma_hard_stats(word, lemmas, stats):
	if (len(lemmas) == 0):
		if (word in stats):
			lemma, pos = stats[word]
		else:
			lemma, pos = word, "S"
	else:
		if (word in stats):
			lemma, pos = stats[word]
		else:
			num = random.randrange(0, len(lemmas))
			lemma, pos = lemmas[num]
	return lemma, pos

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