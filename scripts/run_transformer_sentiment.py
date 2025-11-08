import argparse, yaml, pandas as pd
from src.drc_nlp.io import read_parquet, save_parquet
from src.drc_nlp.sentiment import hf_pipeline_scores
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="in_path", required=True)
parser.add_argument("--out", dest="out_path", required=True)
parser.add_argument("--config", default="config/settings.yml")
args = parser.parse_args()

with open(args.config, "r") as f:
    cfg = yaml.safe_load(f)

df = read_parquet(args.in_path)
texts = df["text"].tolist()
scores = hf_pipeline_scores(texts,
                            model_name=cfg["transformer_model"],
                            batch_size=cfg["batch_size"])
# Normalize transformer labels to {NEG, NEU, POS} if needed
if "label" in scores.columns:
    scores.rename(columns={"label":"hf_label","score":"hf_score"}, inplace=True)
out = pd.concat([df.reset_index(drop=True), scores], axis=1)
save_parquet(out, args.out_path)
print("Saved:", args.out_path, "rows:", len(out))
