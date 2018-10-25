import sys
import os
import numpy as np
import time
import analyzes_results2 as ar

n_splits = 4
		
def run_tests(dirname, k, number_of_nodes, decision_factor):
	accuracy_avg = 0
	precision_micro_avg = 0
	precision_macro_avg = 0
	recall_micro_avg = 0
	recall_macro_avg = 0
	duration_avg = 0

	for i in range(n_splits):
		dataset_dirname = "%s/%s" % (dirname, i)

		start = time.time()
		os.system("./knn %s/treino.txt %s/classes.txt %s/entrada.txt %s %s %s %s/classifieds.txt > /dev/null" % (dataset_dirname, dataset_dirname, 
			dataset_dirname, k, number_of_nodes, decision_factor, dataset_dirname))
		end = time.time()

		duration = end - start	

		accuracy, precision_micro, precision_macro, recall_micro, recall_macro = ar.analyze(dataset_dirname + "/classes_corretas.txt", dataset_dirname + "/classifieds.txt")

		accuracy_avg += accuracy
		precision_micro_avg += precision_micro
		precision_macro_avg += precision_macro
		recall_micro_avg += recall_micro
		recall_macro_avg += recall_macro
		duration_avg += duration
	
	accuracy_avg = accuracy_avg / n_splits
	precision_micro_avg = precision_micro_avg / n_splits
	precision_macro_avg = precision_macro_avg / n_splits
	recall_micro_avg = recall_micro_avg / n_splits
	recall_macro_avg = recall_macro_avg / n_splits
	duration_avg = duration_avg / n_splits

	return accuracy, precision_micro_avg, precision_macro_avg, recall_micro_avg, recall_macro_avg, duration_avg

def print_results(accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, duration_avg):
	print("=======================Result=======================")
	print("Average Accuracy: %s" % accuracy_avg)
	print("Precision Micro: %s" % precision_micro)
	print("Precision Macro: %s" % precision_macro)
	print("Recall Micro: %s" % recall_micro)
	print("Recall Macro: %s" % recall_macro)
	print("Time: %s" % duration_avg)
	print("====================================================")

def write_results(dir, accuracy, precision_micro, precision_macro, recall_micro, recall_macro, duration_avg, k, number_of_nodes, decision_factor, number_of_tests):
	with open('%s/results.txt' % dir, 'w') as f:
		f.write("%s\n" % accuracy)
		f.write("%s\n" % precision_micro)
		f.write("%s\n" % precision_macro)
		f.write("%s\n" % recall_micro)
		f.write("%s\n" % recall_macro)

	with open('%s/experiment_data.txt' % dir, 'w') as f:
		f.write("%s\n" % k)
		f.write("%s\n" % number_of_nodes)
		f.write("%s\n" % decision_factor)
		f.write("%s\n" % number_of_tests)

def main():
	dirname = sys.argv[1]
	k = int(sys.argv[2])
	number_of_nodes = sys.argv[3]
	decision_factor = sys.argv[4]
	number_of_tests = int(sys.argv[5])
	output_dir = sys.argv[6]

	accuracy_avg = 0
	precision_micro_avg = 0
	precision_macro_avg = 0
	recall_micro_avg = 0
	recall_macro_avg = 0
	duration_avg = 0

	print("---------------------Experiment---------------------")

	for i in range(number_of_tests):

		accuracy, precision_micro, precision_macro, recall_micro, recall_macro, duration = run_tests(dirname, k, number_of_nodes, decision_factor)

		print("#################Test#################")
		print("Accuracy: %s" % accuracy)
		print("Precision Micro: %s" % precision_micro)
		print("Precision Macro: %s" % precision_macro)
		print("Recall Micro: %s" % recall_micro)
		print("Recall Macro: %s" % recall_macro)
		print("Time: %s" % duration)
		print("######################################")
		
		accuracy_avg += accuracy
		precision_micro_avg += precision_micro
		precision_macro_avg += precision_macro
		recall_micro_avg += recall_micro
		recall_macro_avg += recall_macro
		duration_avg += duration

	print("----------------------------------------------------")

	accuracy_avg = accuracy_avg / number_of_tests
	precision_micro_avg = precision_micro_avg / number_of_tests
	precision_macro_avg = precision_macro_avg / number_of_tests
	recall_micro_avg = recall_micro_avg / number_of_tests
	recall_macro_avg = recall_macro_avg / number_of_tests
	duration_avg = duration_avg / number_of_tests

	print_results(accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, duration_avg)
	write_results(output_dir, accuracy, precision_micro, precision_macro, recall_micro, recall_macro, duration_avg, k, number_of_nodes, decision_factor, number_of_tests)
	

if __name__ == "__main__":
    main()
