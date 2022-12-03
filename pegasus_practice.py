# -*- coding: utf-8 -*-
"""pegasus_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ngBOYUuyWY4MVQ935Vn2Y30Tq8_nk0_W

# **ABSTRACTIVE TEXT SUMMARIZATION USING PEGASUS**

---
*   Pegasus is a text-summarization transforfmer originally sourced from huggingface.co.
*   It provides a human-interpretation like summarization of the text considered.

*   Pegasus is a self-supervised deep learning model.
*   The basic working involves masking the main statements and ignoring the supporting statements and background information to provide compact summaries.

### **Importing the necessary libraries**
"""

! pip install transformers #installing transformers library

! pip install sentencepiece # installing sentencepiece library to support tokenizing

from transformers import PegasusForConditionalGeneration, PegasusTokenizer 
import torch

"""### **Initializing variables with the PEGASUS model and setting up the GPA supporting cuda package**"""

summarizer = 'google/pegasus-xsum'

device = 'cuda' if torch.cuda.is_available() else 'cpu'

"""### **Setting up the Tokenizer and the Model**"""

tokenizer = PegasusTokenizer.from_pretrained(summarizer)
model = PegasusForConditionalGeneration.from_pretrained(summarizer).to(device)

"""### **Performing Summarization**"""

text = """
Every year the average surface temperature of the earth gets more than the previous year. 
Every year it gets warmer than the previous year. Since 1880 the average surface temperature of earth has increased by about 0.8°Celsius.
The rate of warming has been around 0.15°-0.2°Celsius per decade. 
This is a global change in the earth’s temperature and must not be confused with local changes that we experience every day, during day and night, summer and winter, etc.
The global average temperature of the earth mainly depends on the amount of heat it receives from the sun and what it radiates back into the atmosphere. 
The heat radiated back by the earth depends on the chemical composition of the atmosphere.

"""

"""### **Creating Tokens**"""

batch = tokenizer.prepare_seq2seq_batch(text, truncation=True, padding='longest')

tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

tokens

"""### **Summarize**"""

summary = model.generate(**tokens)

summary[0]

tokenizer.decode(summary[0],skip_special_tokens=True)