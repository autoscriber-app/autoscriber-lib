# %%
import spacy

if not spacy.util.is_package("en_core_web_md"):
    spacy.cli.download("en_core_web_md")

# %%
from summarizer import Summarizer
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download("punkt")

model = Summarizer()


# %%
def summarize(text):
    return [" ".join(sent.strip().split()) for sent in nltk.sent_tokenize(model(text))]
