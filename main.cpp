#include <iostream>
#include <string>
#include<vector>

#include "knn.h"

using namespace std;

#define TRAIN_FILE "./Iris/treino.txt"
#define CLASSES_FILE "./Iris/classes.txt"
#define UNCLASSIFIED_DOCUMENTS_FILE "./Iris/entrada.txt"
#define K 5

int main()
{
	kNN knn;

	knn.train(TRAIN_FILE, CLASSES_FILE);
	knn.classify(K, UNCLASSIFIED_DOCUMENTS_FILE);
	
	cout << "Classificacao realizada com sucesso!" << endl;

	return 0;
}