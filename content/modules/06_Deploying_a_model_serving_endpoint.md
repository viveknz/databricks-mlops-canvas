# Lecture 6: Deploying a Model Serving Endpoint

### 🔍 What is this?
To use real-time serving, you must deploy an **Endpoint**. An endpoint is a secure, unique web address (URL) hosted by Databricks that points directly to your model. When your web application wants a prediction, it sends a packet of data over the internet to that web address, the model processes it, and sends the answer right back.

### 💡 Real-World Analogy
Deploying an endpoint is exactly like setting up a **customer service hotline** telephone number for your model. Once the phone line is turned on (deployed), any external application with the correct security permissions can call the number, speak to the model, and get an answer.

### 🔑 Key Pillars
* **Endpoint URL:** The web address where your model "listens" for requests.
* **Payload:** The data packet sent to the endpoint (usually formatted as a simple JSON text file).
* **Autoscaling:** Databricks automatically buys more server power if millions of requests hit your hotline at the same time, and shuts them down when the traffic drops.