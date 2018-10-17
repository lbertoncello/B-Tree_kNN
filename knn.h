#include "b-tree.h"

#define NUMBER_OF_NODES 5
#define DECISION_FACTOR 0.65

class kNN
{
private:
	BTree model = BTree(NUMBER_OF_NODES, DECISION_FACTOR);
	char* train_file;

public:
	kNN() {};
	void train(char* train_file, char* classes_file);
	void classify(char* unclassified_documents_file);
};