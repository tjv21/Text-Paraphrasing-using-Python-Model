import random
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Paraphrasing mapping (expanded with more variations)
paraphrase_mapping = {
    "hi": ["hello", "hey", "greetings"],
    "i": ["myself", "me", "personally"],
    "am": ["am being", "exist as", "identify as"],
    "superman": ["hero", "savior", "protector"]
    # Add more words and paraphrases here...
}

def paraphrase_word(word):
    synonyms = paraphrase_mapping.get(word, [word])
    return random.choice(synonyms)

def paraphrase_sentence(sentence):
    tokens = sentence.split()
    paraphrased_tokens = [paraphrase_word(token) for token in tokens]
    paraphrased_sentence = ' '.join(paraphrased_tokens)
    return paraphrased_sentence

# Input sentence
input_sentence = "Hi I am tejasvi and i have done my diploma i am parusing b.tech in computer science ."

# Paraphrase the input sentencea
paraphrased_sentence = paraphrase_sentence(input_sentence.lower())

# Print original and paraphrased sentences
print("Original Sentence:", input_sentence)
print("Paraphrased Sentence:", paraphrased_sentence)
