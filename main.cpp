#include <iostream>
#include <string>
#include<vector>
#include<string>

#include "knn.h"

using namespace std;

int main(int argc, char* argv[])
{
	string train_file = argv[1];
	string classes_file = argv[2];
	string unclassified_documents_file = argv[3];
	int k = stoi(argv[4]);
	int number_of_nodes = stoi(argv[5]);
	double decision_factor = stod(argv[6]);
	string output_file = argv[7];
	kNN knn(number_of_nodes, decision_factor);

	knn.train(train_file.c_str(), classes_file.c_str());
	knn.classify(k, unclassified_documents_file.c_str(), output_file.c_str());
	
	cout << "Classificacao realizada com sucesso!" << endl;

	return 0;
}