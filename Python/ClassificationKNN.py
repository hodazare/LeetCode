import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, KFold
import random

# read the data
trainDT = r"C:\Users\Hoda\Desktop\interview\train_data.csv"
testDT = r"C:\Users\Hoda\Desktop\interview\test_data.csv"

train_dt = pd.read_csv(trainDT)
test_dt = pd.read_csv(testDT)

# separate features and categories
features = train_dt.iloc[:,:-1]
features.drop('id', axis=1, inplace=True)
test_ids = test_dt.iloc[:,1]
test_dt.drop('id', axis=1, inplace=True)
categories = train_dt.iloc[:,-1]

# create train and test variables
X_train, X_test, y_train, y_test = train_test_split(features, categories, test_size=0.2, random_state=23)
print('------------------------------------------------ KNN')
knn = KNeighborsClassifier(n_neighbors=6)
# fit the model with data (occurs in-place)
model = knn.fit(X_train, y_train)
# predict the test result for evaluating the model
prediction = knn.predict(X_test)
print('Classification accuracy is: ', metrics.accuracy_score(y_test, prediction)*100, '%')
print(metrics.classification_report(y_test, prediction))
print('------------------------------------------------ provide related categories for unlabelled data and save the result in a csv file (final_result.csv)')
predict_unlabeled_data = knn.predict(test_dt)
df_predicted = pd.DataFrame(predict_unlabeled_data)
df_predicted.to_csv(r'C:\Users\Hoda\Desktop\interview\Diligen_categories_resultKNN.csv')
print('Done.')
col = categories.unique()
df = pd.DataFrame(0, index=range(len(predict_unlabeled_data)), columns=range(len(categories.unique())))
df.columns = categories.unique()
for i in range(len(predict_unlabeled_data)):
    df.loc[i][predict_unlabeled_data[i]] = 1

df.to_csv(r'C:\Users\Hoda\Desktop\interview\Diligen_final_resultKNN.csv')
print('Saved.')