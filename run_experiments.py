import sys
import os
import numpy as np
from sklearn.model_selection import StratifiedKFold

dataset_file_name = sys.argv[1]
classes_file_name = sys.argv[2]
k = int(sys.argv[3])
number_of_nodes = sys.argv[4]
decision_factor = sys.argv[5]
number_of_experiments = int(sys.argv[6])

def create_subsets(dataset_file_name, classes_file_name):
	dataset_file = open(dataset_file_name, 'r')
	lines = dataset_file.readlines()

	dataset_file.close()

	dataset = []

	for line in lines:
		vec = np.array(line.replace('\n', '').split(','))
		dataset.append(vec)
		#dataset.append(vec.astype(np.float))
		
	classes_file = open(classes_file_name, 'r')
	lines = classes_file.readlines()

	classes_file.close()

	classes = []

	for line in lines:
		vec = np.array(line.replace('\n', '').split(','))
		classes.append(vec)
	
	return (dataset, classes)
		
def run_tests(dataset_file_name, classes_file_name, k, number_of_nodes, decision_factor):
	dataset, classes = create_subsets(dataset_file_name, classes_file_name)

	dataset_dirname = os.path.dirname(dataset_file_name)
	np.set_printoptions(precision=2)

	skf = StratifiedKFold(n_splits=4)

	for train_index, test_index in skf.split(dataset, classes):
		with open('%s/treino.txt' % dataset_dirname, 'w') as f:
			for index in train_index:
				f.write("%s\n" % str(" ".join(map(str, dataset[index].astype(np.float)))))
			
		with open('%s/classes.txt' % dataset_dirname, 'w') as f:
			for index in train_index:
				f.write("%s\n" % str(" ".join(map(str, classes[index]))))
				
		with open('%s/entrada.txt' % dataset_dirname, 'w') as f:
			for index in test_index:
				f.write("%s\n" % str(" ".join(map(str, dataset[index].astype(np.float)))))
		
		with open('%s/classes_corretas.txt' % dataset_dirname, 'w') as f:
			for index in test_index:
				f.write("%s\n" % str(" ".join(map(str, classes[index]))))
				
		os.system("./knn %s/treino.txt %s/classes.txt %s/entrada.txt %s %s %s %s/classifieds.txt" % (dataset_dirname, dataset_dirname, 
			dataset_dirname, k, number_of_nodes, decision_factor, dataset_dirname))
			
		os.system("python3 analyzes_results.py %s/classes_corretas.txt %s/classifieds.txt" % (dataset_dirname, dataset_dirname))
	
def main():
	for i in range(number_of_experiments):
		print("---------------------Experiment---------------------")
		run_tests(dataset_file_name, classes_file_name, k, number_of_nodes, decision_factor)
		print("----------------------------------------------------")

if __name__ == "__main__":
    main()