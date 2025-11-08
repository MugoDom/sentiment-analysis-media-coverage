import argparse, yaml, pandas as pd
from src.drc_nlp.io import read_parquet, save_parquet
from src.drc_nlp.sentiment import vader_scores

parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="in_path", required=True)
parser.add_argument("--out", dest="out_path", required=True)
args = parser.parse_args()

df = read_parquet(args.in_path)
scores = vader_scores(df["text"].tolist())
out = pd.concat([df.reset_index(drop=True), scores], axis=1)
save_parquet(out, args.out_path)
print("Saved:", args.out_path, "rows:", len(out))
