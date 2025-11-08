.PHONY: setup ingest vader xfm lint fmt notebooks

setup:
\tpython -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ingest:
\tpython scripts/ingest_guardian_csv.py --in data/raw/guardian_drc_2000_2025.csv --out data/interim/guardian_clean.parquet

vader:
\tpython scripts/run_vader.py --in data/interim/guardian_clean.parquet --out data/processed/sentiment_vader.parquet

xfm:
\tpython scripts/run_transformer_sentiment.py --in data/interim/guardian_clean.parquet --out data/processed/sentiment_xfm.parquet

lint:
\truff check src scripts

fmt:
\tblack src scripts

notebooks:
\tjupyter notebook
