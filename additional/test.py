import torch
import pandas as pd 
from ast import literal_eval

# Question Translation Library
import translators as ts
import translators.server as tss
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad", from_tf=True)

# tokenizer = AutoTokenizer.from_pretrained("Andaf/bert-uncased-finetuned-squad-indonesian")
# model = AutoModelForQuestionAnswering.from_pretrained("Andaf/bert-uncased-finetuned-squad-indonesian", from_tf=True)

qa_model = pipeline("question-answering", model=model, tokenizer=tokenizer)

df = pd.read_csv('data/faq.csv', sep=";", converters={'paragraph': literal_eval})
# print(df.head())
paragraf = df['paragraphs']
judul = df['title']
nomor = df['No']
data = df['paragraphs']
data = " ".join(data)
data = data.replace("'", "")
data = tss.google(data, to_language='en')
# print(paragraf)
# print(data)
while True:
    question = input("Masukkan Pertanyaan:")
    question = tss.google(question, to_language='en')
    result =qa_model(question = question, context = data)
    result = tss.google(result, to_language='id')
    print(result)

## {'answer': 'İstanbul', 'end': 39, 'score': 0.953, 'start': 31}
