#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include "writing.h"

void write_results(vector<string> classes, const char* output_file)
{
	ofstream saida;

	saida.open(output_file);
	
	for (int i = 0; i < classes.size(); i++)
	{
		saida << classes[i] << endl;
	}

	saida.close();
}