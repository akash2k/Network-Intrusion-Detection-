import pandas as pd
df = pd.read_csv('dataset_review3.csv')
df.shape
df.head()
df = df.iloc[:,1:28]
count_class_0, count_class_1, count_class_2 = df.TCP_Protocol.value_counts()
print(count_class_0)
print(count_class_1)
print(count_class_2)
df_class_0 = df[df['TCP_Protocol'] == 'TCP']
df_class_1 = df[df['TCP_Protocol'] == 'UDP']
df_class_2 = df[df['TCP_Protocol'] == 'Others']
df_class_0_under = df_class_0.sample(15000)
df_class_1_under = df_class_1.sample(15000)
df_under = pd.concat([df_class_0_under, df_class_1_under], axis = 0)
df_under = pd.concat([df_under, df_class_2], axis = 0)
print(df_under.TCP_Protocol.value_counts())
df_n = df_under
df_n.head()
df_n.shape


x = df_n.iloc[:,0:26]
y = df_n.iloc[:,26]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, random_state = 42)
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression()
model.fit(x_train, y_train)

from sklearn.metrics import classification_report, accuracy_score
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
print("Accuracy: ",accuracy_score(y_pred, y_test))
