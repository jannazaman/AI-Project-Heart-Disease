# AI-Project-Heart-Disease

## Overview
This project aims to predict heart disease using machine learning algorithms, specifically Support Vector Machines (SVM) and Multi-Layer Perceptron (MLP) neural networks. The project explores the performance of SVM with different kernels and MLP with various activation functions, highlighting their strengths in capturing both linear and non-linear patterns in the data.

## Features
Below are the details and descriptions of the data features.
- 13 Features and 1 Target

| Variable Name   | Type         | Description                                       |
|-----------|--------------|---------------------------------------------------------|
| Age       | Integer      | Age of the individual                                   |
| Sex       | Categorical  | Gender of the individual                                |      
| CP        | Categorical  | Chest pain type                                         | 
| Trestbps  | Integer      | Resting blood pressure (on admission to the hospital)   |
| Chol      | Integer      | Serum cholesterol                                       |
| Fbs       | Categorical  | Fasting blood sugar > 120 mg/dL                         | 
| Restecg   | Categorical  | Resting electrocardiographic results                    | 
| Thalach   | Integer      | Maximum heart rate achieved                             | 
| Exang     | Categorical  | Exercise-induced angina                                 | 
| Oldpeak   | Integer      | ST depression induced by exercise relative to rest      |    
| Slope     | Categorical  | Slope of the peak exercise ST segment                   |
| Ca        |Integer       | Number of major vessels (0-3) colored by fluoroscopy    |
| Thal      | Categorical  | Thalassemia                                             |
| Num       | Integer      | Diagnosis of heart disease  (TARGET)                    |

## What I Imported to Train/Test the Models
* import random &#8594; for generating random numbers
* import pandas &#8594; for data manipulation and analysis
* import numpy &#8594; for numerical operations
* scikit-learn &#8594; popular machine learning library that provides simple and efficient tools for data analysis, modeling, splitting

## How to Import and Use
1. Clone the Repository:
   ```bash
   git clone https://github.com/jannazaman/AI-Project-Heart-Disease.git
   ```
2. Install Requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. 


## Model Application 
### Home Page
![homepage](images/HomePage.png)
### MLP Details Page
![mlp](images/MLP_page.png)
### SVM Details Page
![svm](images/MLP_page.png)
### Heart Disease Prediction Page
![formpage](images/Form_Page.png)


## Results 
### Superior Performance of MLP with "tanh" Activation: 
Based on experiment outcomes, the MLP model with the "tanh" activation function outperformed both linear and non-linear SVM models, achieving the highest accuracy of 0.885. This indicates that the MLP model is a better fit for this dataset and its ability to simulate non-linear correlations contributes to capturing complex data patterns effectively.
   
### Model Advantages: 
- SVMs excel in handling high-dimensional and non-linearly separable data through kernel functions, offering insights into the decision-making process. 
- MLPs provide greater flexibility, mastering complex mappings. Careful hyperparameter selection is essential to avoid overfitting in MLP, while the symmetric "tanh" activation function aids in better data pattern understanding.

## Download Dataset
You can download the dataset (processed.cleveland.data) from the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Heart+Disease
