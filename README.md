# Industrial_Shrink_Wrapping_Machine_Failure_Prediction
This peoject is on an industrial shrink wrapper failure prediction for preventive maintenance purpose

### Introduction
The goal of this analysis is to predict failures in a shrink wrapping machine using various machine learning models. The data is preprocessed to handle class imbalance and outliers, and multiple resampling techniques and models are tested to determine the best approach for accurate predictions.

### Data Loading and Preprocessing
The dataset contains various features related to the shrink wrapping machine's operation. The preprocessing steps include:

1. Loading the Data: The data is loaded into a Pandas DataFrame.
2. Feature Scaling: The features are scaled using StandardScaler to normalize the data.
3. Outlier Removal: Outliers are identified and removed based on Z-scores (values more than 3 standard deviations away from the mean).
4. Train-Test Split: The data is split into training and testing sets with stratification to maintain the class distribution.
5. Models Training using Resampling Techniques and Ensemble models

***Various machine learning models are employed, including***:

* Random Forest
* Support Vector Machine (SVM)
* Gradient Boosting Classifier
* K-Nearest Neighbors (KNN)
* Neural Network using Keras

### Resampling techniques used to handle class imbalance:
* Random Under-Sampling
* Random Over-Sampling
* Synthetic Minority Over-sampling Technique (SMOTE)

### Ensemble methods are also explored to enhance model performance:
* Balanced Random Forest
* Easy Ensemble
* Balanced Bagging Classifier

### Model Training and Evaluation
The models are trained using the training set, and their performance is evaluated using the testing set. Cross-validation is used to ensure robust evaluation, and the performance metrics include precision, recall, and F1-score.

### Results and Recommendations
The models are evaluated based on their classification reports and cross-validation scores. Key findings include:

***Behaviour of Lag Error***: This is with relationship to timestamp, speed and torque

***Imbalance Handling***: Resampling techniques like SMOTE significantly improve the model's ability to handle class imbalance.
Model Performance: Ensemble methods such as Balanced Random Forest and Easy Ensemble show promising results in handling imbalance and improving prediction accuracy.
Neural Network: The neural network model also performs well, but it requires careful tuning of hyperparameters.

### Conclusion
Handling class imbalance is crucial for improving the performance of machine learning models in predicting shrink wrapping machine failures. Resampling techniques and ensemble methods are effective in achieving better accuracy and robustness. Future work can focus on getting more data and looking into other opportunities for improved feature engineering.
