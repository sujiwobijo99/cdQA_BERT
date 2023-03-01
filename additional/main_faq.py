# from transformers import BertForQuestionAnswering
# model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# from transformers import BertTokenizer
# tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("Andaf/bert-uncased-finetuned-squad-indonesian")

model = AutoModelForQuestionAnswering.from_pretrained("Andaf/bert-uncased-finetuned-squad-indonesian", from_tf=True)

import torch
import pandas as pd 
from ast import literal_eval

# Question Translation Library
import translators as ts
import translators.server as tss

# Loading Datasets
df = pd.read_csv('data/faq.csv', sep=";", converters={'paragraph': literal_eval})
# print(df.head())
paragraf = df['paragraphs']
judul = df['title']
nomor = df['No']
# data = " ".join(data)
# data = data.replace("'", "")
# print(paragraf)
# print(data)

def answer_question(question, datasets):
    '''
    Takes a `question` string and an `answer_text` string (which contains the
    answer), and identifies the words within the `answer_text` that are the
    answer. Prints them out.
    '''
    # question = tss.google(question, to_language='en')
    score_start = 0
    score_end = 0
    max_score = 0
    id_max = 0
    j=1
    for text in datasets:
        # print(text)
        # text_string = tss.google(text, to_language='en')       
        text_string = str(text)
        # print(text_string)
        # ======== Tokenize ========
        # Apply the tokenizer to the input text, treating them as a text-pair.
        input_ids = tokenizer.encode(question, text_string, truncation= True, max_length= 512, padding= True)

        # Report how long the input sequence is.
        # print('Query has {:,} tokens.\n'.format(len(input_ids)))

        # ======== Set Segment IDs ========
        # Search the input_ids for the first instance of the `[SEP]` token.
        sep_index = input_ids.index(tokenizer.sep_token_id)

        # The number of segment A tokens includes the [SEP] token istelf.
        num_seg_a = sep_index + 1

        # The remainder are segment B.
        num_seg_b = len(input_ids) - num_seg_a

        # Construct the list of 0s and 1s.
        segment_ids = [0]*num_seg_a + [1]*num_seg_b

        # There should be a segment_id for every input token.
        assert len(segment_ids) == len(input_ids)

        # ======== Evaluate ========
        # Run our example through the model.
        outputs = model(torch.tensor([input_ids]), # The tokens representing our input text.
                        token_type_ids=torch.tensor([segment_ids]), # The segment IDs to differentiate question from answer_text
                        return_dict=True) 

        start_scores = outputs.start_logits
        end_scores = outputs.end_logits
        max_start_score = torch.argmax(start_scores)
        # print(max_start_score)
        # max_end_score = torch.argmax(end_scores)
        # print(j)
        if max_start_score > max_score:
            max_score = max_start_score
            score_start = start_scores
            id_max = j
            score_end = end_scores
        j += 1
        # print("End scores", end_scores)
    
    # print("Start Score:", max_score)
    # print("End Score:", score_end)
    # print("ID for max start score:", id_max)
    # print("Article num for Answer:", nomor[id_max])

    text_str = tss.google(datasets[id_max-1], to_language='en')       
    # print(text_string)
    # ======== Tokenize ========
    # Apply the tokenizer to the input text, treating them as a text-pair.
    input_ids = tokenizer.encode(question, text_str)

    # ======== Reconstruct Answer ========
    # Find the tokens with the highest `start` and `end` scores.
    answer_start = torch.argmax(score_start)
    answer_end = torch.argmax(score_end)

    # Get the string versions of the input tokens.
    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    # Start with the first token.
    answer = tokens[answer_start]
    # print("Answer Start Score", answer_start)

    # Select the remaining answer tokens and join them with whitespace.
    for i in range(answer_start + 1, answer_end + 1):
        
        # If it's a subword token, then recombine it with the previous token.
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        
        # Otherwise, add a space then the token.
        else:
            answer += ' ' + tokens[i]
    answer = tss.google(answer, to_language='id')

    # for key, value in paragraf.items():
    #     if value.find(answer) != -1:
    #         print(f"The key of the answer is: {key}")

    print('Answer: "' + answer + '"')


question = str(input("Masukkan pertanyaan: "))

answer_question(question, paragraf)