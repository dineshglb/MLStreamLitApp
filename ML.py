import streamlit as st
import time 
st.header("**Welcome to Machine Learning**")

st.write("Machine learning (ML) is a field of artificial intelligence where computers learn to make decisions or predictions based on data rather than being explicitly programmed with specific instructions. Essentially, it’s like training a computer to recognize patterns, adapt to new situations, and improve over time.")
c1=st.container()
c1.write("Machine learning, or ML, is like teaching a computer how to learn from examples. Imagine you’re teaching your friend how to tell cats and dogs apart. You show them lots of pictures of cats and dogs and say, This is a **cat**, or This is a **dog**. After seeing enough examples, your friend starts to figure out what makes a cat different from a dog.In machine learning, we do something similar with computers. We give the computer lots of examples, like pictures of cats and dogs, and it starts to learn patterns. After seeing a lot of examples, the computer gets good at guessing if a new picture shows a cat or a dog, even if it’s never seen that picture before.So, ML is all about helping computers learn patterns from examples instead of telling them exactly what to do.")
c2=st.container(border=True)
c2.write("*Machine learning is the study of computer algorithms that allow computer programs to automatically improve through experience.*")
        
c2.write("*-Tom M. Mitchell*")

st.header("**Types of Machine Learning**")

col1,col2,col3=st.columns(3)
col1.write("**Supervised Learning**")
col1.image("images\supervised.png")
col1.write("In supervised learning, the algorithm learns from labeled training data, which helps the model make predictions or decisions without being explicitly programmed to do so. Each example in the training dataset includes the input objects and the desired output. The goal is for the model to eventually make predictions that are as accurate as possible.")

col2.write("**Unsupervised Learning**")
col2.image("images\\Unsupervised.png")
col2.write("In unsupervised learning, the algorithm is given data without any labels. The goal is to find hidden patterns or intrinsic structures in the input data. This type of learning is often used for clustering and association tasks. For example, clustering algorithms can group customers based on purchasing behavior without predefined labels.")
col3.write("**Reinforcement Learning**")
col3.image("\\images\\Reinforcement.png")
col3.write("In reinforcement learning, an agent learns to make decisions by taking actions in an environment to maximize some notion of cumulative reward. The agent receives feedback in the form of rewards or penalties and uses this to learn the optimal behavior or policy. This type of learning is often used in robotics, gaming, and navigation.")
st.spinner(text="In progress...")




