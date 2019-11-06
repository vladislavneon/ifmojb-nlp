#morpher.py

import text_parser as TextParser
import odict_search as OdictSearch
import dictionary as Dictionary
import analyzer as Analyzer
import statistic_methods as Statistic
import sys

args = sys.argv
test_number = args[1]
text_file = ".\datasets\dataset" + test_number + ".txt"
method_name = "#ODict with OpenCorpora+Syntagrus hard lemma+pos statistic resolutionfor all words\n"
parsed_file = "parsed.txt"
morph_file = "morph.txt"
output_file = "output.txt"
main_dictionary = TextParser.build_dict(text_file)
pos_statistics = Statistic.build_hard_stats("stats_hard_oc+synt.txt")
#pos_statistics = Statistic.build_pos_stats("stats_oc+synt.txt")
OdictSearch.create_dict_with_odict(main_dictionary)
Dictionary.print_dict(main_dictionary, morph_file)
Analyzer.process_text(text_file, output_file, main_dictionary, pos_statistics, method_name)

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