import pandas as pd
from ast import literal_eval
from transformers import pipeline
qa_pipeline = pipeline(
    "question-answering",
    model="Rifky/Indobert-QA",
    tokenizer="Rifky/Indobert-QA"
)

df = pd.read_csv('data/faq.csv', sep=";", converters={'paragraph': literal_eval})
# print(df.head())
paragraf = df['paragraphs']
judul = df['title']
nomor = df['No']
data = df['paragraphs']
data = " ".join(data)
data = data.replace("'", "")

def qa_query(question):
    answer = qa_pipeline({
        'context': data,
        'question': question
    })
    return answer[answer]

# status = False
# while status:
#     question = input("Masukkan pertanyaan:")

#     answer = qa_pipeline({
#         'context': data,
#         'question': question
#     })

#     print("Jawaban: {}".format(answer['answer']))
#     next = input("Apakah akan keluar?(Y/N)")
#     if next == "Y" :
#         status = False