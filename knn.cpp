#include <vector>
#include <string>
#include<algorithm>
#include <map>
#include <iterator>

#include "knn.h"
#include "reading.h"
#include "writing.h"

using namespace std;

bool comparator(Document* d1, Document* d2)
{
	return d1->similarity < d2->similarity;
}

void kNN::train(char* train_file, char* classes_file)
{
	this->train_file = train_file;
	this->model.generate_tree(train_file, classes_file);
}

string most_frequent_class(vector<Document*> nearest_neighbors, int k)
{
	map<string, int> counter;
	int maior = 0;
	string chosen_class;

	for (int i = 0; i < k; i++)
	{
		//Verifica se o elemento já está no map
		if (counter.find(nearest_neighbors[i]->doc_class) != counter.end())
		{
			counter[nearest_neighbors[i]->doc_class]++;
		}
		else
		{
			counter[nearest_neighbors[i]->doc_class] = 1;
		}
	}

	for (std::map<string, int>::iterator it = counter.begin(); it != counter.end(); ++it)
	{
		if (it->second > maior)
		{
			maior = it->second;
			chosen_class = it->first;
		}
	}
	
	return chosen_class;
}

void kNN::classify(int k, char* unclassified_documents_file)
{
	vector<string> classes;
	vector<vector<double>> documents = read_unclassified_documents(unclassified_documents_file);

	for (int i = 0; i < documents.size(); i++)
	{
		vector<Document*> nearest_neighbors;

		model.most_similar_documents(train_file, documents[i], k, nearest_neighbors);

		std::sort(nearest_neighbors.rbegin(), nearest_neighbors.rend(), comparator);

		classes.push_back(most_frequent_class(nearest_neighbors, k));

		cout << "CLASSE: " << classes[i] << endl;
	}

	write_results(classes);
}
