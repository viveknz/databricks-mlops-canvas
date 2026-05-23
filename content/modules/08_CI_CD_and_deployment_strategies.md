# Lecture 8: CI/CD and Deployment Strategies

### 🔍 What is this?
**CI/CD** stands for **Continuous Integration and Continuous Deployment**. It uses automated pipelines (like GitHub Actions) to run automated software tests every single time an engineer submits new code. If all tests pass, the pipeline automatically deploys the update to production without any human intervention.

### 💡 Real-World Analogy
Think of CI/CD like an **automated car manufacturing assembly line**. Before a new car leaves the factory floor, automated robot arms slam the doors, test the brakes, and check the tire pressure. If a flaw is detected, the assembly line freezes immediately. If everything passes, the car rolls right out to the dealership.

### 🔑 Key Pillars
* **Continuous Integration (CI):** Automatically testing your code modifications for bugs or broken parts.
* **Continuous Deployment (CD):** Automatically shipping approved code updates to the live production server.
* **Rollback:** The ability to instantly flip a switch and restore the old, working version of your app if something goes wrong with a new update.