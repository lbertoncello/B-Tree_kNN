#!/bin/bash

python3 run_experiments3.py Iris/Subsets Iris/k.txt 6 0.5 1 ./Iris/Experiments/Tree/1

python3 run_experiments3.py Iris/Subsets Iris/k.txt 8 0.5 1 ./Iris/Experiments/Tree/2

python3 run_experiments3.py Iris/Subsets Iris/k.txt 10 0.5 1 ./Iris/Experiments/Tree/3

python3 run_experiments3.py Iris/Subsets Iris/k.txt 15 0.5 1 ./Iris/Experiments/Tree/4