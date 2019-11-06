#statistic_methods.py

def build_pos_stats(stats_file):
	inf = open(stats_file, "r")
	stats = {}
	for line in inf:
		entry = line.strip().split(sep = ";")
		word = entry[0]
		tag = entry[1]
		freq = int(entry[2])
		if (word in stats):
			stats[word][tag] = freq
		else:
			stats[word] = {}
			stats[word][tag] = freq
	inf.close()
	return stats
	
def build_hard_stats(stats_file):
	inf = open(stats_file, "r")
	stats = {}
	for line in inf:
		entry = line.strip().split(sep = ";")
		word = entry[0]
		lemma = entry[1]
		pos = entry[2]
		stats[word] = (lemma, pos)
	return stats
		
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