import sys

correct = sys.argv[1]
predicted = sys.argv[2]

file = open(correct, 'r')
correct_classes = file.readlines()
file.close()

file = open(predicted, 'r')
predicted_classes = file.readlines()
file.close()

error_count = 0

for i in range(len(correct_classes)):
	if correct_classes[i] != predicted_classes[i]:
		#print("Correto: %s" % correct_classes[i])
		#print("Predito: %s" % predicted_classes[i])
		error_count += 1
		
acurracy = 1 - error_count / len(correct_classes)

print("Quantidade de erros: %s" % error_count)
print("Taxa de acertos: %s" % acurracy)