# Lecture 9: Intro to Monitoring

### 🔍 What is this?
A machine learning model is not a set-it-and-forget-it software product. Models learn from patterns in historical data. Once the model is live, the real world can change around it, making the model's predictions highly inaccurate over time. This loss of accuracy is called **Model Decay**.

### 💡 Real-World Analogy
Imagine you build an AI bot designed to predict flight ticket prices, and you train it entirely on data from 2018. If a global event completely changes world travel habits, your bot’s internal logic will suddenly become completely useless. **Monitoring** is the smoke alarm that rings the second your model starts making weird predictions due to shifts in reality.

### 🔑 Key Pillars
* **Data Drift:** When the live input data coming into your model shifts away from what the training data looked like.
* **Concept Drift:** When the underlying relationship changes (e.g., a house that used to be worth $500K is now worth $1M due to sudden economic changes).