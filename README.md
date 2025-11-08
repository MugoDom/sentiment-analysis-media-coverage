# DRC Guardian NLP

NLP + Sentiment mini-project on Guardian coverage of the Democratic Republic of the Congo (2000–2025).

## Quick start
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Put `guardian_drc_2000_2025.csv` into `data/raw/`.
4. `make ingest` (clean/normalize), then `make vader` or `make xfm` (transformer).
5. Explore notebooks in `notebooks/`.

## Data
- Expected columns: `pub_date, headline, trailText, bodyText, web_url, section_name`