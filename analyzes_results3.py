from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

def read_results(correct, predicted):
	file = open(correct, 'r')
	correct_classes = file.readlines()
	file.close()

	file = open(predicted, 'r')
	predicted_classes = file.readlines()
	file.close()

	return correct_classes, predicted_classes

def analyze(correct, predicted):
	correct_classes, predicted_classes = read_results(correct, predicted)

	accuracy = accuracy_score(correct_classes, predicted_classes)

	precision_micro = precision_score(correct_classes, predicted_classes, average='micro')
	precision_macro = precision_score(correct_classes, predicted_classes, average='macro')

	recall_micro = recall_score(correct_classes, predicted_classes, average='micro')
	recall_macro = recall_score(correct_classes, predicted_classes, average='macro')

	f1_micro = f1_score(correct_classes, predicted_classes, average='micro') 
	f1_macro = f1_score(correct_classes, predicted_classes, average='macro')  

	return accuracy, precision_micro, precision_macro, recall_micro, recall_macro, f1_micro, f1_macro
