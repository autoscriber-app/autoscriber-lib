from summarizer import Summarizer

model = Summarizer()

def summarize(**args):
    return model(**args)
