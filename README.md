# 📧 Spam Detection Project  

## 📌 Project Overview  
This project aims to **detect spam emails** using machine learning models to prevent **phishing attacks** and unwanted messages.  
We trained four different models:  

- **Neural Network** (**Best Model - 99% Accuracy**)  
- **Naive Bayes**  
- **Logistic Regression**  
- **Support Vector Machine (SVM)**  

The best-performing model was the **Neural Network**, which achieved **99% accuracy**.  
The model was trained using **Google Colab**, and the trained model along with the dictionary were saved for use in the application.  

## 📂 Project Structure  

📂 Spam_Detection_Project │── 📂 dataset # Contains the spam_ham_dataset.csv │── 📂 notebook # colab notebook used for training and evaluation │── 📂 results # Evaluation reports and model performance │── 📂 demo # Video demonstration of the app usage │── 📂 app # Application files │ │── spam_detector.py # Main script for spam detection │ │── mon_modele_spam.h5 # Trained Neural Network model │ │── mon_dictionnaire.dict # Dictionary for text processing │── README.md # Project documentation




## 🔧 Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Samii05/Spam_Detection_Project.git
cd Spam_Detection_Project/app

### 2️⃣ Install dependencies

Make sure you have Python 3.8+ installed. Then, install the required libraries:

pip install tensorflow gensim spacy numpy tkinter

### 3️⃣ Download the Spacy NLP model

python -m spacy download en_core_web_sm


### 🚀 Running the Spam Detector App

To launch the GUI-based Spam Detector, follow these steps:

    Open the terminal (Command Prompt / PowerShell / Bash)
    Navigate to the project directory

cd C:\...

    Run the application

python spam_detector.py

This will open a graphical interface where you can enter an email message and classify it as Spam or Ham (Not Spam).


### 📌 Demo

A video demonstration of how to use the application is available in the demo/ folder.
📜 License

This project is open-source and available under the MIT License.


Author
Sami Ramzi REZIG 
