import tkinter as tk
from tkinter import ttk
import threading
import time

def print_question(*args):
    question = question_entry.get()
    submit_button.config(text="Loading...", state="disabled")
    t = threading.Thread(target=process_question, args=(question,))
    t.start()

# membuat fungsi untuk memproses pertanyaan dan mencetak hasilnya
def process_question(question):
    ans_stat = True
    # menampilkan animasi loading pada tombol submit selama 2 detik
    while ans_stat == True:
        submit_button.config(text="Loading" + ".", state="disabled")
        # mencetak pertanyaan pada terminal
        answer = f"Jawaban dari pertanyaan anda adalah: {question_entry.get()}"
        answer_label2.config(text=answer)
        ans_stat = False   

    # mengubah teks tombol submit menjadi "Submit" dan mengaktifkannya kembali
    submit_button.config(text="Submit", state="normal")

    
def add_recommended_question(event):
    # mendapatkan teks dari pilihan pertanyaan yang dipilih
    selected_question = recommended_question_var.get()

    # memasukkan teks pilihan pertanyaan ke dalam kolom input pertanyaan
    question_entry.delete(0, tk.END)
    question_entry.insert(0, selected_question)


# instance Tkinter
root = tk.Tk()

root.title("Aplikasi Pertanyaan")
root.geometry("900x400")
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# dropdown menu dengan pilihan pertanyaan rekomendasi di samping kiri kolom input pertanyaan
recommended_questions = ["Apa itu kecerdasan buatan?", "Bagaimana cara kerja mesin pencari?", "Apa itu blockchain?", "Bagaimana cara kerja algoritma genetika?", "Apa itu big data?"]
recommended_question_var = tk.StringVar(value="Contoh Pertanyaan")
recommended_question_dropdown = ttk.Combobox(input_frame, textvariable=recommended_question_var, values=recommended_questions, font=("Segoe UI Bold", 12),  state="readonly", width=25, background="pink")
recommended_question_dropdown.bind("<<ComboboxSelected>>", add_recommended_question)
recommended_question_dropdown.pack(side="left",ipady=8)


# kolom input pertanyaan
question_entry = tk.Entry(input_frame, width=50, font=("Segoe UI", 12), borderwidth=2, relief="groove")
question_entry.pack(side="left", ipady=8)

# placeholder pada kolom input pertanyaan
question_entry.insert(0, "Masukkan pertanyaan...")

# fungsi untuk menghapus placeholder
def clear_placeholder(event):
    if question_entry.get() == "Masukkan pertanyaan...":
        question_entry.delete(0, tk.END)

# event binding untuk menghapus placeholder
question_entry.bind("<FocusIn>", clear_placeholder)

# event binding pada kolom input pertanyaan untuk mengeksekusi fungsi print_question saat tombol "Enter" pada keyboard ditekan
question_entry.bind("<Return>", print_question)

# tombol submit
submit_button = tk.Button(input_frame, text="Submit", command=print_question, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0)
submit_button.pack(side="left", padx=10)


# frame untuk kolom jawaban
ans_label_frame = tk.Frame(root)
ans_label_frame.pack()
answer_label = tk.Label(root, text="Jawaban", fg="#FF0000", font=("Sans Bold", 18), padx=10, borderwidth=0)
answer_label.pack()
answer_label2 = tk.Label(root, text="", fg="#0e0e0f", font=("Sans Bold", 18), padx=10, borderwidth=0)
answer_label2.pack()

# label untuk kolom jawaban
answer_text = tk.Label(root, text="")
answer_text.pack(padx=10)

# menjalankan aplikasi
root.mainloop()
