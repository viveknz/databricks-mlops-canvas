# Lecture 4: Log and Register Models with MLflow

### 🔍 What is this?
Training a model is only half the battle; you also need a safe way to store it and tag it for production. 
* **Logging** a model means saving the final trained model files (artifacts) into a cloud storage closet. 
* **Registering** a model means taking that saved file and submitting it to a central library called the **Model Registry**, where it is assigned an official version number and a status tag.

### 💡 Real-World Analogy
**Logging** a model is like an artist finishing a painting and wrapping it up safely in a moving box. **Registering** the model is like hanging that painting on a gallery wall with a clear placard reading: *"House Price Predictor, Version 3, Status: Approved for Public Viewing."*

### 🔑 Key Pillars
* **Artifacts:** The heavy, physical files that contain the patterns your model learned during training.
* **Model Registry:** A secure digital catalog for managing all your team's models.
* **Model Versions:** Tracks how your model updates over time (Version 1 ➡️ Version 2 ➡️ Version 3).