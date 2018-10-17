#include <vector>

using namespace std;

int number_of_columns(char* train_file);
int number_of_lines(char* train_file);
vector<double> read_vector(string line);
vector<double> read_at_index(char* train_file, int pos);
string read_class_at_index(char* classes_file, int line_number);
vector<string> read_classes(char* classes_file);
vector<vector<double>> read_unclassified_documents(char* documents_file);