# prompt_engineering.py V1.0
# This script demonstrates how to use the T5 model for text generation.
# It includes a prompt for generating a short story and prints the output.
# Import the necessary libraries
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Define the prompt
prompt = "Generate a short story about a character who learns to play the guitar."

# Tokenize the prompt
tokenizer = T5Tokenizer.from_pretrained('t5-base')
input_ids = tokenizer.encode(prompt, return_tensors='pt')

# Generate the text
model = T5ForConditionalGeneration.from_pretrained('t5-base')
output = model.generate(input_ids, max_length=200)

# Print the generated text
print(tokenizer.decode(output[0], skip_special_tokens=True))
