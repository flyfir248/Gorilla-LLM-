
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model():
    tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')
    model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B')
    return tokenizer, model

def process_data(text, tokenizer, model):
    input_ids = tokenizer.encode(text, return_tensors='pt')
    output = model.generate(input_ids, max_length=1500, do_sample=True, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

text = 'Write an article about Asia.'

# Load the model and tokenizer
tokenizer, model = load_model()

# Process the data
response = process_data(text, tokenizer, model)

print(response)