# Sentiment Analisis ~ Week 6
## Task
Mengelompokkan text menjadi 5 kelompok sentiment.
## Data
1. `train.csv` : Main train dataset
2. `test.csv` : Main test dataset
3. `test lama.csv` : Test dataset sebelum di revisi
4. `Submission Lama.csv` : Submission test dataset lama sebelum direvisi [Accuracy = 1]
## Hal yang Udah Dicoba
1. Frature Extraction using Bag of Words & TF-IDF, Modelling dengan Logistic Regression, dll. <br>`Accuracy` : 0.35 ~ 0.39
2. `Bert TF-Hub` with and without text preprocessing.
<br>`Accuracy` : 0.38 ~ 0.4
3. `Bert Keras Model` with and without preprocessing.
<br>`Accuracy` : 0.38 ~ 0.44
4. TF-IDF & Logistic Regression menggunakan StratifiedKfold.
<br>`Accuracy` : 0.41 ~ 0.44
5. `XLMRoberta` + Addictional data menggunakan StratifiedKfold.
<br>`Accuracy` : 0.49 ~ 0.51 # Best 

#### Note : Enggak tau kenapa text yang tanpa preprocess bisa dapet akurasi yang lebih bagus.