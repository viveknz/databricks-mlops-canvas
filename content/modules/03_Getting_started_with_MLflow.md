# Lecture 3: Getting Started with MLflow

### 🔍 What is this?
When building a machine learning model, you will try hundreds of different combinations of data settings, algorithms, and knobs (called **parameters**). **MLflow** is an open-source tool built into Databricks that tracks every single experiment you run. It automatically saves your settings, your code version, and your results (called **metrics**) so you never lose track of your work.

### 💡 Real-World Analogy
Think of MLflow as a **digital lab notebook** with a built-in camera. Every time you mix a new batch of chemicals (run an experiment), MLflow automatically snaps a picture of your exact recipe checklist and writes down how well the experiment performed. If you stumble into a breakthrough, you can look back at the notebook to see exactly how you did it.

### 🔑 Key Pillars
* **Parameters:** The setup inputs or configuration settings you chose before training the model (e.g., learning rate).
* **Metrics:** The output scores or performance results of your model (e.g., accuracy percentage).
* **Tracking UI:** A visual dashboard where you can compare 20 different model runs side-by-side to see which one won.