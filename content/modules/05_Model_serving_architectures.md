# Lecture 5: Model Serving Architectures

### 🔍 What is this?
Once a model is registered, other software programs (like a mobile app or a company website) need a way to talk to it. **Model Serving** is the method you use to expose your model to the outside world. There are two primary ways to do this: **Batch Processing** and **Real-time Serving**.

### 💡 Real-World Analogy
* **Batch Processing** is like the postal mail. The mail carrier collects a massive stack of letters all day, processes them at night, and delivers the answers the next morning. 
* **Real-time Serving** is like a drive-thru window. You pull up, ask a single question, and the employee hands you your answer immediately.

### 🔑 Key Pillars
* **Batch Serving:** Good for calculating millions of predictions at once when speed isn't crucial (e.g., generating personalized product recommendations for every user overnight).
* **Real-time Serving:** Crucial for split-second decisions (e.g., checking if a credit card transaction is fraudulent at the exact moment the card is swiped).