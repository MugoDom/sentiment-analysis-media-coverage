import argparse, yaml
from src.drc_nlp.io import load_guardian_csv, save_parquet
from src.drc_nlp.textprep import prepare

parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="in_path", required=True)
parser.add_argument("--out", dest="out_path", required=True)
parser.add_argument("--config", default="config/settings.yml")
args = parser.parse_args()

with open(args.config, "r") as f:
    cfg = yaml.safe_load(f)

df = load_guardian_csv(args.in_path)
df_clean = prepare(df,
                   text_priority=cfg["text_column_priority"],
                   min_chars=cfg["min_chars"])
save_parquet(df_clean, args.out_path)
print("Saved:", args.out_path, "rows:", len(df_clean))
