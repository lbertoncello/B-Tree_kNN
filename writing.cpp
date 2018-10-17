#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include "writing.h"

void write_results(vector<string> classes)
{
	ofstream saida;

	saida.open("classifieds.txt");
	
	for (int i = 0; i < classes.size(); i++)
	{
		saida << classes[i] << endl;
	}

	saida.close();
}