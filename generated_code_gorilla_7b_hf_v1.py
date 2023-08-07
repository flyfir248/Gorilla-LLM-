
from transformers import pipeline

def load_model():
    generator = pipeline('text2image', model='Lykon/DreamShaper')
    return generator

def process_data(text, generator):
    generated_image = generator(text)
    response = generated_image[0]['image']
    return response

text = "This is an example text to generate an image"

# Load the model
generator = load_model()

# Generate an image from the text
response = process_data(text, generator)

print(response)