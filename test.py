import tkinter as tk
from tkinter import ttk

def print_question():
    question = question_input.get()
    print(f"Pertanyaan: {question}")

def on_select(event):
    selected_question = event.widget.get()
    question_input.delete(0, tk.END)
    question_input.insert(0, selected_question)

root = tk.Tk()
root.title("Sistem QA")
root.geometry("600x300")

# create label for question input
question_label = ttk.Label(root, text="Masukkan pertanyaan", font=("Segoe UI", 14))
question_label.grid(row=0, column=0, padx=20, pady=10)

# create input field for question
question_input = ttk.Entry(root, font=("Segoe UI", 14))
question_input.grid(row=1, column=0, padx=20, pady=10)
question_input.bind("<Return>", lambda event: print_question())

# create submit button
submit_button = ttk.Button(root, text="Submit", command=print_question)
submit_button.grid(row=2, column=0, padx=20, pady=10)

# create dropdown for recommended questions
recommended_questions = ["Apa itu machine learning?", "Bagaimana cara membuat model deep learning?"]
recommended_questions_label = ttk.Label(root, text="Pertanyaan rekomendasi", font=("Segoe UI", 14))
recommended_questions_label.grid(row=0, column=1, padx=20, pady=10)
question_dropdown = ttk.Combobox(root, values=recommended_questions, font=("Segoe UI", 14))
question_dropdown.grid(row=1, column=1, sticky="W", padx=20, pady=10)
question_dropdown.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
