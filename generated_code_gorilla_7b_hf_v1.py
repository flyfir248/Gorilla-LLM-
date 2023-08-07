
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def load_model():
    tokenizer = AutoTokenizer.from_pretrained('d4data/biomedical-ner-all')
    model = AutoModelForSequenceClassification.from_pretrained('d4data/biomedical-ner-all')
    return tokenizer, model

def process_data(text, tokenizer, model):
    ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy='simple')
    response = ner(text)
    return response

text = "The patient's blood pressure was 150/90 mmHg."
# Load the model and tokenizer
tokenizer, model = load_model()

# Process the data
response = process_data(text, tokenizer, model)

print(response)