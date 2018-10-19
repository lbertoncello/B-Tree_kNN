#include <iostream>
#include <vector>
#include <fstream>
#include <string>

#include "reading.h"

using namespace std;

int number_of_lines(char* train_file)
{
	string line;
	ifstream train(train_file);

	if (train.is_open())
	{
		getline(train, line);
	}

	train.close();

	return stoi(line.substr(0, 1), nullptr);
}

int number_of_columns(char* train_file)
{
	string line;
	ifstream train(train_file);

	if (train.is_open())
	{
		getline(train, line);
	}

	train.close();

	return stoi(line.substr(2, 1), nullptr);
}

vector<double> read_vector(string line)
{
	vector<double> v;
	double number;

	int i = 0;
	while (i < line.size())
	{
		int pos_espaco = line.find(' ', i);

		if (pos_espaco == -1)
		{
			pos_espaco = line.size();
		}

		//Seleciona o trecho onde ha espaco (fim da coluna)
		number = stod(line.substr(i, pos_espaco));
		v.push_back(number);

		//Incrementa o que foi percorrido
		i = pos_espaco + 1;
	}

	//cout << endl;
	return v;
}

//Le o vetor na linha indicada pela posicao
vector<double> read_at_index(char* train_file, int pos)
{
	string line;
	vector<double> v;
	ifstream train(train_file);

	train.seekg(pos);
	getline(train, line);
	v = read_vector(line);

	train.close();

	return v;
}

string read_class_at_index(char* class_file, int line_number)
{
	string line;
	ifstream class_f(class_file);

	for (int i = 0; i <= line_number; i++)
	{
		getline(class_f, line);
	}

	return line;
}

vector<string> read_classes(char* class_file)
{
	string line;
	vector<string> classes;
	ifstream class_f(class_file);

	while (getline(class_f, line))
	{
		classes.push_back(line);
	}

	return classes;
}

vector<vector<double>> read_unclassified_documents(char* documents_file)
{
	string line;
	vector<double> document;
	vector<vector<double>> documents;
	ifstream documents_f(documents_file);

	while (getline(documents_f, line))
	{
		document = read_vector(line);
		documents.push_back(document);
	}

	return documents;
}

void print_file(char* train_file)
{
	string line;
	ifstream train(train_file);

	cout << "ARQUIVO" << endl;

	cout << "Posicao: " << train.tellg() << endl;
	while (getline(train, line))
	{
		cout << line << endl;
		cout << "Posicao: " << train.tellg() << endl;
	}
}

/*
vector<string> read_classes_at_lines(char* classes_file, vector<int> line_numbers)
{
string line;
ifstream classes(classes_file);

for (int i = 0; i < length; i++)
{

}
}
*/

