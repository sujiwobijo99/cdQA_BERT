import pandas as pd
from ast import literal_eval
import json

# Buat dictionary kosong untuk menyimpan data SquAD v1.1
data = {"data": []}

# Baca file CSV dengan format "title,content,link"
with open('dataset.csv', newline='') as csvfile:
    reader = pd.read_csv(csvfile, sep=";", converters={'paragraph': literal_eval})
    print(reader)
    for row in reader:
        # Buat dictionary untuk setiap pasangan pertanyaan dan jawaban
        paragraph = {
            "context": row[1],
            "qas": []
        }
        # Tambahkan pasangan pertanyaan dan jawaban ke dalam data SquAD v1.1
        data["data"].append({
            "title": row[0],
            "paragraphs": [paragraph],
            "link": row[2]
        })

# Simpan data SquAD v1.1 dalam format JSON
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
