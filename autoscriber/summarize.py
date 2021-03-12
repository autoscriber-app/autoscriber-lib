from summarizer import Summarizer

model = Summarizer()


def summarize(text):
    return model(text)
