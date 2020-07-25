# Sentiment Analisis ~ Week 6
## Task
Mengelompokkan text menjadi 5 kelompok sentiment.
## Data
1. `train.csv` : Main train dataset
2. `test.csv` : Main test dataset
3. `test lama.csv` : Test dataset sebelum di revisi
4. `Submission Lama.csv` : Submission test dataset lama sebelum direvisi [Accuracy = 1]
5. `Submission.csv` : Best Submission so far ~ [Accuracy = 0.45]
6. `train baru.csv` : Class balancing dengan ngegabungin `train.csv` dengan `test lama.csv` yang akurasinya 1
## Hal yang Udah Dicoba
1. Frature Extraction using Bag of Words & TF-IDF, Modelling dengan Logistic Regression, dll. <br>`Accuracy` : 0.35 ~ 0.39
2. `Bert TF-Hub` with and without text preprocessing.
<br>`Accuracy` : 0.38 ~ 0.4
3. `Bert Keras Model` with and without preprocessing.
<br>`Accuracy` : 0.38 ~ 0.44
#### Note : Enggak tau kenapa text yang tanpa preprocess bisa dapet akurasi yang lebih bagus.
## To Do
1. Preprocess yang bener
2. Optimalize Model pke `LTSM`
3. Nyoba pake dataset baru `train baru.csv`
4. Embedding pake `Glove` & `Word2Vec`