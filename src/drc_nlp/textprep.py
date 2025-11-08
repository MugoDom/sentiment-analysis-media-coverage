import re, pandas as pd
from datetime import datetime

def coalesce_text(row, order=("bodyText","trailText","headline")):
    for c in order:
        txt = row.get(c)
        if isinstance(txt, str) and txt.strip():
            return txt
    return None

def basic_clean(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s

def prepare(df: pd.DataFrame, text_priority, min_chars=200) -> pd.DataFrame:
    out = df.copy()
    out["text"] = out.apply(lambda r: coalesce_text(r, tuple(text_priority)), axis=1)
    out.dropna(subset=["text"], inplace=True)
    out["text"] = out["text"].astype(str).map(basic_clean)
    out["n_chars"] = out["text"].str.len()
    out = out[out["n_chars"] >= min_chars]
    out["pub_date"] = pd.to_datetime(out["pub_date"], errors="coerce")
    out = out.dropna(subset=["pub_date"])
    out["year"] = out["pub_date"].dt.year
    out["month"] = out["pub_date"].dt.to_period("M").astype(str)
    return out[["pub_date","year","month","web_url","section_name","text"]].reset_index(drop=True)
