import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk  # Pour un meilleur design
import tensorflow as tf
import gensim
import spacy

# Charger le modèle                                 
model = tf.keras.models.load_model("mon_modele_spam.h5")

# Charger le dictionnaire
dictionary = gensim.corpora.Dictionary.load("mon_dictionnaire.dict")

# Charger le modèle NLP (ex: Spacy)
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    new_text = []
    new_doc = nlp(text)
    for token in new_doc:
        if not token.is_stop and not token.is_punct and not token.like_num:
            new_text.append(token.lemma_)
    new_bow = dictionary.doc2bow(new_text)
    new_tfidf_vector = gensim.models.TfidfModel(dictionary=dictionary)[new_bow]
    new_dense_vector = gensim.matutils.corpus2dense([new_tfidf_vector], num_terms=len(dictionary)).T
    return new_dense_vector

def classify_message():
    message = entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showwarning("Attention", "Veuillez entrer un message.")
        return
    
    new_vector = preprocess_text(message)
    prediction = model.predict(new_vector)
    result = "HAM (Légitime)" if prediction[0] < 0.5 else "SPAM (Indésirable)"
    result_label.config(text=f"Résultat : {result}", bootstyle=("success" if result == "HAM (Légitime)" else "danger"))

def reset():
    entry.delete("1.0", tk.END)
    result_label.config(text="Résultat :", bootstyle="secondary")

# Interface Tkinter avec ttkbootstrap
root = ttk.Window(themename="superhero")  # Thème moderne
root.title("Détection de Spams")
root.geometry("500x400")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

label = ttk.Label(frame, text="Entrez un message :", font=("Arial", 12, "bold"))
label.pack(pady=10)

entry = tk.Text(frame, height=5, width=60, font=("Arial", 10))
entry.pack(pady=10)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

btn_classify = ttk.Button(btn_frame, text="Classifier", command=classify_message, bootstyle="primary")
btn_classify.pack(side="left", padx=10)

btn_reset = ttk.Button(btn_frame, text="Réinitialiser", command=reset, bootstyle="secondary")
btn_reset.pack(side="right", padx=10)

result_label = ttk.Label(frame, text="Résultat :", font=("Arial", 12, "bold"), bootstyle="secondary")
result_label.pack(pady=20)

root.mainloop()