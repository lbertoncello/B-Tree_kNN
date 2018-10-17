#include <vector>
#include <string>

#include "knn.h"
#include "reading.h"
#include "writing.h"

using namespace std;

void kNN::train(char* train_file, char* classes_file)
{
	this->train_file = train_file;
	this->model.generate_tree(train_file, classes_file);
}

void kNN::classify(char* unclassified_documents_file)
{
	Document doc;
	vector<string> classes;
	vector<vector<double>> documents = read_unclassified_documents(unclassified_documents_file);

	for (int i = 0; i < documents.size(); i++)
	{
		doc = model.most_similar_document(train_file, documents[i]);
		classes.push_back(doc.doc_class);

		cout << "CLASSE: " << doc.doc_class << endl;
	}

	write_results(classes);
}
