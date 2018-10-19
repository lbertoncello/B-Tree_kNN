import sys
import os

dataset_file = sys.argv[1]
number_of_experiments = int(sys.argv[2])
test_size = float(sys.argv[3])

dataset_dirname = os.path.dirname(dataset_file)

for i in range(number_of_experiments):
	print("---------------------Experiment---------------------")
	os.system("python3 create_subsets.py %s %s" % (dataset_file, str(test_size)))
	os.system("./knn")
	os.system("python3 analyzes_results.py %s/classes_corretas.txt %s/classifieds.txt" % (dataset_dirname, dataset_dirname))
	print("----------------------------------------------------")