import pandas as pd
import  numpy as np
import time
start=time.time()
df = pd.read_csv('heart.csv')
df.shape
df.head()
df = df.iloc[:,0:14]
count_class_0, count_class_1 = df.TCP_Protocol.value_counts()
print(count_class_0)
print(count_class_1)

df_class_0 = df[df['TCP_Protocol'] == 'TCP']
df_class_1 = df[df['TCP_Protocol'] == 'UDP']
df_class_2 = df[df['TCP_Protocol'] == 'Others']
df_class_0_under = df_class_0.sample(11000)
df_class_1_under = df_class_1.sample(11000)
df_under = pd.concat([df_class_0_under, df_class_1_under], axis = 0)
df_under = pd.concat([df_under, df_class_2], axis = 0)
print(df_under.TCP_Protocol.value_counts())
df_n = df_under
df_n.head()
df_n.shape

"""
x = df_n.iloc[:,0:26]
y = df_n.iloc[:,26]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, random_state = 42)
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression()
model.fit(x_train, y_train)

param_grid = [{'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
    'C' : np.logspace(-10, 10, 40),
    'solver' : ['lbfgs','newton-cg','liblinear','sag','saga'],
    'max_iter' : [100, 1000, 2500, 5000]}]

from sklearn.model_selection import RandomizedSearchCV
clf = RandomizedSearchCV(model, param_distributions = param_grid, cv = 3, verbose=True, n_jobs=-1)
clf.fit(x_train, y_train)
parameters = clf.best_params_
print(parameters)

from sklearn.linear_model import LogisticRegression 
final_model = LogisticRegression(penalty = parameters['penalty'], C = parameters['C'], max_iter = parameters['max_iter'], solver = parameters['solver'])
final_model.fit(x_train, y_train)
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score (final_model, x_train, y_train, cv=10, scoring = "f1_micro")
print(accuracies)

from sklearn.metrics import classification_report, accuracy_score
y_pred = final_model.predict(x_test)
print(classification_report(y_test, y_pred))
print("Accuracy: ",accuracy_score(y_pred, y_test))
end=time.time()
print("Computation Time: ",end-start) 
"""
