This is an alternative proposal to the traditional kNN. It uses a Search Tree to increase the speed of the classification process.

To generate the executable, type:

    make

To run tests, just type:
    
    python3 run_experiments.py [indexed dataset] [dataset classes] [k value] [number of nodes] [decision factor] [number of experiments]
    
Example:

    python3 run_experiments.py ./Iris/dataset.txt ./Iris/dataset_classes.txt 1 8 0.5 1 
  
Notes:

  Decision factor is the value at which similarity will be compared to decide whether the search goes left or right.
  
  The indexed dataset file must be in csv format, using ',' as delimiter.
