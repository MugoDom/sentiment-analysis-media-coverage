from tqdm import tqdm
import pandas as pd

def vader_scores(texts):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    an = SentimentIntensityAnalyzer()
    rows = []
    for t in tqdm(texts, desc="VADER"):
        s = an.polarity_scores(t)
        rows.append(s)
    return pd.DataFrame(rows)  # columns: neg, neu, pos, compound

def hf_pipeline_scores(texts, model_name, batch_size=16, device=None):
    from transformers import pipeline
    pipe = pipeline("sentiment-analysis", model=model_name, device=device)
    rows = []
    for i in tqdm(range(0, len(texts), batch_size), desc="HF sentiment"):
        batch = texts[i:i+batch_size]
        preds = pipe(batch, truncation=True)
        rows.extend(preds)
    # normalize to columns: label, score
    return pd.DataFrame(rows)
