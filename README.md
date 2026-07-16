# Recurrent Neural Networks (RNNs) for Sequence Data

## Project Overview

This project demonstrates the implementation of a **Recurrent Neural Network (RNN)** using **Long Short-Term Memory (LSTM)** for sentiment analysis on the **IMDB Movie Reviews** dataset.

The objective is to classify movie reviews as **positive** or **negative** by learning sequential patterns in text data. The model is built using **TensorFlow/Keras** and evaluated using standard classification metrics.

---

# Objectives

* Understand sequential data processing using RNNs.
* Build an LSTM-based neural network.
* Perform sentiment analysis on movie reviews.
* Evaluate the model using classification metrics.
* Compare LSTM with traditional RNNs.

---

# Dataset

**Dataset:** IMDB Movie Reviews

* Source: TensorFlow/Keras Datasets
* Training Samples: 25,000
* Testing Samples: 25,000
* Vocabulary Size: 10,000 most frequent words
* Classification Type: Binary (Positive / Negative)

---

# Data Preprocessing

The following preprocessing steps were applied:

* Loaded the IMDB dataset.
* Limited vocabulary to the 10,000 most frequent words.
* Applied sequence padding.
* Fixed sequence length to **200 words**.
* Prepared the dataset for LSTM training.

---

# Model Architecture

The implemented LSTM model consists of:

1. Embedding Layer
2. LSTM Layer (128 Units)
3. Dropout Layer
4. Dense Hidden Layer (64 Neurons)
5. Sigmoid Output Layer

---

# Hyperparameters

| Parameter               | Value               |
| ----------------------- | ------------------- |
| Optimizer               | Adam                |
| Loss Function           | Binary Crossentropy |
| Batch Size              | 32                  |
| Epochs                  | 10                  |
| Vocabulary Size         | 10,000              |
| Maximum Sequence Length | 200                 |

---

# Model Performance

The model was evaluated using:

* Test Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

The LSTM successfully learned sequential dependencies within movie reviews and achieved strong performance on unseen test data.

> **Replace the value below with your actual result from Colab:**
>
> **Final Test Accuracy:** XX.XX%

---

# Project Structure

```text
AI-ML-Internship-Week6-Task1-RNN-Sentiment-Analysis/

│── README.md
│── requirements.txt

├── notebooks/
│     rnn_sentiment_analysis.ipynb

├── src/
│     rnn_model.py
│     preprocess.py

├── docs/
│     performance_evaluation.md

├── assets/
│     training_accuracy.png
│     training_loss.png
│     confusion_matrix.png

├── models/
│     saved_rnn_model.keras
```

---

# Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab

---

# Key Learning Outcomes

Through this project, the following concepts were learned:

* Recurrent Neural Networks (RNNs)
* Long Short-Term Memory (LSTM)
* Natural Language Processing (NLP)
* Sequence Padding
* Word Embeddings
* Binary Sentiment Analysis
* Backpropagation Through Time
* Adam Optimizer
* Model Evaluation
* Confusion Matrix
* Classification Report

---

# Future Improvements

Possible enhancements include:

* Implementing Bidirectional LSTM.
* Comparing LSTM with GRU.
* Applying pre-trained word embeddings (Word2Vec or GloVe).
* Hyperparameter tuning for improved performance.
* Testing on larger sentiment analysis datasets.

---

# Conclusion

This project successfully demonstrated the application of **Long Short-Term Memory (LSTM)** networks for sentiment analysis. Compared to traditional RNNs, LSTMs effectively capture long-term dependencies in sequential text, making them highly suitable for Natural Language Processing tasks such as sentiment analysis, language modeling, and text classification.
