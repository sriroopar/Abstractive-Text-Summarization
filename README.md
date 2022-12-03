# Abstractive-Text-Summarization
A personal project to play around PEGASUS transformer for abstractive summarization.
---
## PEGASUS by Google

*   Pegasus is a text-summarization transforfmer originally sourced from huggingface.co.
*   It provides a human-interpretation like summarization of the text considered.

*   Pegasus is a self-supervised deep learning model.
*   The basic working involves masking the main statements and ignoring the supporting statements and background information to provide compact summaries.
*   Pegasus is a Transformer encoder-decoder model that summarizes by extracting gap sentences.

## Working mechanism 

### Sample Work Flow
---

<img src="https://user-images.githubusercontent.com/80977779/205459626-7a2c124d-c3c5-427f-a80e-1cba3b4b9d25.png"></img>

---

* Text input is taken-in and tokenized.
* Tokenized inputs are masked if important.
* Masked statements are mapped to the output.
* Output is generated in a sequential format.

---

### Use cases

* Text Summarizers
* Paraphrasing
* Gist derival of articles and research papers.

