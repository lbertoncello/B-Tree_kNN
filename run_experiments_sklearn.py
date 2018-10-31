import sys
import os
import numpy as np
import time
from sklearn.model_selection import StratifiedKFold
import create_subsets_sklearn as cs
import analyzes_results3 as ar
import sklearn_knn as sk_knn

n_splits = 4
		
def run_tests(dirname, k):
	accuracy_avg = 0
	precision_micro_avg = 0
	precision_macro_avg = 0
	recall_micro_avg = 0
	recall_macro_avg = 0
	f1_micro_avg = 0
	f1_macro_avg = 0
	duration_avg = 0

	for i in range(n_splits):
		dataset_dirname = "%s/%s" % (dirname, i)

		file = open(dataset_dirname + "/treino.txt", "r")
		text = file.readlines()
		file.close()

		train_dataset = np.zeros([len(text), text[0].count(' ') + 1])

		i = 0
		for line in text:
			j = 0
			vec = line.split(' ')

			for num in vec:
				train_dataset[i][j] = float(num)
				j += 1
			i += 1

		file = open(dataset_dirname + "/classes.txt", "r")
		text = file.readlines()
		file.close()

		train_classes = np.chararray(len(text), itemsize=30, unicode=True)

		i = 0
		for line in text:
			train_classes[i] = line.replace('\n', '')
			i += 1

		file = open(dataset_dirname + "/entrada.txt", "r")
		text = file.readlines()
		file.close()

		test_dataset = np.zeros([len(text), text[0].count(' ') + 1])

		i = 0
		for line in text:
			j = 0
			vec = line.split(' ')

			for num in vec:
				test_dataset[i][j] = float(num)
				j += 1
			i += 1

		start = time.time()
		sk_knn.classify(k, train_dataset, train_classes, test_dataset, dataset_dirname)
		end = time.time()

		duration = end - start	

		accuracy, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro = ar.analyze(dataset_dirname + "/classes_corretas.txt", dataset_dirname + "/classifieds.txt")

		accuracy_avg += accuracy
		precision_micro_avg += precision_micro
		precision_macro_avg += precision_macro
		recall_micro_avg += recall_micro
		recall_macro_avg += recall_macro
		f1_micro_avg += f1_micro
		f1_macro_avg += f1_macro
		duration_avg += duration
	
	accuracy_avg = accuracy_avg / n_splits
	precision_micro_avg = precision_micro_avg / n_splits
	precision_macro_avg = precision_macro_avg / n_splits
	recall_micro_avg = recall_micro_avg / n_splits
	recall_macro_avg = recall_macro_avg / n_splits
	f1_micro_avg = f1_micro_avg / n_splits
	f1_macro_avg = f1_macro_avg / n_splits
	duration_avg = duration_avg / n_splits

	return accuracy, precision_micro_avg, precision_macro_avg, recall_micro_avg, recall_macro_avg, f1_micro_avg, f1_macro_avg, duration_avg

def print_results(accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro, duration_avg):
	print("=======================Result=======================")
	print("Average Accuracy: %s" % accuracy_avg)
	print("Precision Micro: %s" % precision_micro)
	print("Precision Macro: %s" % precision_macro)
	print("Recall Micro: %s" % recall_micro)
	print("Recall Macro: %s" % recall_macro)
	print("F1 Micro: %s" % f1_micro)
	print("F1 Macro: %s" % f1_macro)
	print("Time: %s" % duration_avg)
	print("====================================================")

def write_results(dir, accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro, duration_avg, k, number_of_tests):
	with open('%s/results.txt' % dir, 'w') as f:
		f.write("%s\n" % accuracy_avg)
		f.write("%s\n" % precision_micro)
		f.write("%s\n" % precision_macro)
		f.write("%s\n" % recall_micro)
		f.write("%s\n" % recall_macro)
		f.write("%s\n" % f1_micro)
		f.write("%s\n" % f1_macro)
		f.write("%s\n" % duration_avg)

	with open('%s/experiment_data.txt' % dir, 'w') as f:
		f.write("%s\n" % k)
		f.write("%s\n" % number_of_tests)

def main():
	dirname = sys.argv[1]
	k = int(sys.argv[2])
	number_of_tests = int(sys.argv[3])
	output_dir = sys.argv[4]

	accuracy_avg = 0
	precision_micro_avg = 0
	precision_macro_avg = 0
	recall_micro_avg = 0
	recall_macro_avg = 0
	f1_micro_avg = 0
	f1_macro_avg = 0
	duration_avg = 0

	print("---------------------Experiment---------------------")

	for i in range(number_of_tests):

		accuracy, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro, duration  = run_tests(dirname, k)

		print("#################Test#################")
		print("Accuracy: %s" % accuracy)
		print("Precision Micro: %s" % precision_micro)
		print("Precision Macro: %s" % precision_macro)
		print("Recall Micro: %s" % recall_micro)
		print("Recall Macro: %s" % recall_macro)
		print("F1 Micro: %s" % f1_micro)
		print("F1 Macro: %s" % f1_macro)
		print("Time: %s" % duration)
		print("######################################")
		
		accuracy_avg += accuracy
		precision_micro_avg += precision_micro
		precision_macro_avg += precision_macro
		recall_micro_avg += recall_micro
		recall_macro_avg += recall_macro
		f1_micro_avg += f1_micro
		f1_macro_avg += f1_macro
		duration_avg += duration

	print("----------------------------------------------------")

	accuracy_avg = accuracy_avg / number_of_tests
	precision_micro_avg = precision_micro_avg / number_of_tests
	precision_macro_avg = precision_macro_avg / number_of_tests
	recall_micro_avg = recall_micro_avg / number_of_tests
	recall_macro_avg = recall_macro_avg / number_of_tests
	f1_micro_avg = f1_micro / number_of_tests
	f1_macro_avg = f1_macro / number_of_tests
	duration_avg = duration_avg / number_of_tests

	print_results(accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro, duration_avg)
	write_results(output_dir, accuracy_avg, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro, duration_avg, k, number_of_tests)

if __name__ == "__main__":
    main()