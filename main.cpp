#include <iostream>
#include <string>
#include<vector>

#include "knn.h"

using namespace std;

#define TRAIN_FILE "treino.txt"
#define CLASSES_FILE "classes.txt"
#define UNCLASSIFIED_DOCUMENTS_FILE "entrada.txt"

int main()
{
	kNN knn;

	knn.train(TRAIN_FILE, CLASSES_FILE);
	knn.classify(UNCLASSIFIED_DOCUMENTS_FILE);
	
	return 0;
}