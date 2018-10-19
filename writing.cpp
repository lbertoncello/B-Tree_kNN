#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include "writing.h"

#define OUTPUT_FILE_NAME "./Iris/classifieds.txt"

void write_results(vector<string> classes)
{
	ofstream saida;

	saida.open(OUTPUT_FILE_NAME);
	
	for (int i = 0; i < classes.size(); i++)
	{
		saida << classes[i] << endl;
	}

	saida.close();
}