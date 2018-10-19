import sys
import os

dataset_file = sys.argv[1]
k = int(sys.argv[2])
number_of_nodes = sys.argv[3]
decision_factor = sys.argv[4]
number_of_experiments = int(sys.argv[5])
test_size = float(sys.argv[6])

dataset_dirname = os.path.dirname(dataset_file)

for i in range(number_of_experiments):
	print("---------------------Experiment---------------------")
	os.system("python3 create_subsets.py %s %s" % (dataset_file, str(test_size)))
	os.system("./knn %s/treino.txt %s/classes.txt %s/entrada.txt %s %s %s %s/classifieds.txt" % (dataset_dirname, dataset_dirname, 
		dataset_dirname, k, number_of_nodes, decision_factor, dataset_dirname))
	os.system("python3 analyzes_results.py %s/classes_corretas.txt %s/classifieds.txt" % (dataset_dirname, dataset_dirname))
	print("----------------------------------------------------")