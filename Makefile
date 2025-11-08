.PHONY: setup ingest vader xfm lint fmt notebooks

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ingest:
	python -m scripts.ingest_guardian_csv --in data/raw/guardian_drc_2000_2025.csv --out data/interim/guardian_clean.parquet

vader:
	python -m scripts.run_vader --in data/interim/guardian_clean.parquet --out data/processed/sentiment_vader.parquet

xfm:
	python -m scripts.run_transformer_sentiment --in data/interim/guardian_clean.parquet --out data/processed/sentiment_xfm.parquet

lint:
	ruff check src scripts

fmt:
	black src scripts

notebooks:
	jupyter notebook