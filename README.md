# Industrial_Shrink_Wrapping_Machine_Failure_Prediction
In this project I used different models to predict the failure of a shrink wrapping machine. The purpose of knowing the possible failure likelihood of a machine is to ensure proper predictive maintenance and reduce maintenance cost. The dataset was gotten from [https://www.kaggle.com/datasets/inIT-OWL/vega-shrinkwrapper-runtofailure-data]

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
After an in-depth exploratory data analysis and model evalutaion, the Key findings include:

***Better understanding between Lag error relationship to timestamp, speed and torque***

***Imbalance Handling***: Resampling techniques like SMOTE significantly improve the model's ability to handle class imbalance.
Model Performance: Ensemble methods such as Balanced Random Forest and Easy Ensemble show promising results in handling imbalance and improving prediction accuracy.
Neural Network: The neural network model also performs well, but it requires careful tuning of hyperparameters.

### Local User interface and Deployment on streamlit app
To monitor and test out the performace of the model on new information we created a local  user interface using Tkinter an Streamlit was the web app of choice to use.

### Conclusion
* Most of the models performed really well when dataset seemed unbalanced and balanced. I believe it is as a result of the threshold used and the behaviour of the machine generally with response to time.

* Handling class imbalance is crucial for improving the performance of machine learning models in predicting shrink wrapping machine failures. Resampling techniques and ensemble methods are effective in achieving better accuracy and robustness. 

* Future work can focus on some of the challenges encountered by getting a more robust data and looking into other opportunities for improved feature engineering.
