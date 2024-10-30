import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report, accuracy_score

header=st.container()
dataset=st.container()
input =  st.container()
metr=st.container()
with header:
    st.header("What is SVM?")
    st.write("A Support Vector Machine (SVM) is a powerful machine learning algorithm widely used for both linear and nonlinear classification, as well as regression and outlier detection tasks. SVMs are highly adaptable, making them suitable for various applications such as text classification, image classification, spam detection, handwriting identification, gene expression analysis, face detection, and anomaly detection.")
with dataset:
    st.header("Spam-Ham Mail Dataset")
    data= pd.read_csv("data/spamEX10.csv",encoding='ISO-8859-1')
    spam=pd.DataFrame(data['v2'].value_counts()).head(50)
    st.write(data.head(10))
    st.write('Visualisation')
    st.bar_chart(spam)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['v2'])
y = data['v1']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = svm.SVC(kernel='linear',class_weight='balanced')
model.fit(X_train, y_train)

predictions = model.predict(X_test)

st.subheader("Metrics")
col1,col2=st.columns(2)

col1.write("Accuracy Score:")
col2.write(accuracy_score(y_test, predictions))
inputs,col3=st.columns(2)
msg=inputs.text_input("Enter Your Message",'hi')

# Function to predict if a new input message is spam or ham
def predict_message(msg):
    message_vec = vectorizer.transform([msg])  # Vectorize the new input
    if message_vec.nnz == 0:
        return "Unknown message - words not in training data"
    prediction = model.predict(message_vec)  # Predict using the trained model
    return prediction[0]


result = predict_message(msg)
if result=='ham':
    inputs.success(result)
else:
    inputs.error(result)




