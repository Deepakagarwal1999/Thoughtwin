# Thoughtwin

First I explored the dataset. I find some duplicate values and I removed them. Then I see most of the features has maximum times zero values. Also I see in the dependent variable 0 has more values than 1. so it's kind of imbalanced. I used here Decision trees types models. Because of No effect of different range of values in features. 
I tried:
  A. Random Forest 
  B. XBGoost
  C. Pycaret library to get results for all classifier at the same time(For example: Catboost, Extratrees
    1. with features removed which have more than 70% zero values and 
    2. with all features and 
    3. with getting only important features extracted using XGB:
  
I also tried Pandas Profiling to get some insights from the dataset.

PS: I have attached the trained model and prediction file as final.csv and required libraries file.
