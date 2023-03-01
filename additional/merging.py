from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("indolem/indobert-base-uncased")

model = AutoModelForQuestionAnswering.from_pretrained("indolem/indobert-base-uncased", from_tf=True)