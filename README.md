This is an alternative proposal to the traditional kNN. It uses a Search Tree to increase the speed of the classification process.

To run tests in the Iris Dataset, just type:
    
    python3 run_experiments.py [dataset file] [k value] [number of nodes] [decision factor] [number of experiments] [size of the test subset]
    
Example:

    python3 run_experiments.py ./Iris/iris.data.txt 3 5 0.5 10 0.25
  
Notes:

  Decision factor is the value at which similarity will be compared to decide whether the search goes left or right.
  
  The dataset file must be in csv format, using ';' as a separator. The final column should be the document classes.
