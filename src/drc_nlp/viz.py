import matplotlib.pyplot as plt

def plot_monthly_counts(df, ax=None, title="Articles per Month"):
    ax = ax or plt.gca()
    (df.groupby("month")["web_url"].count()
       .reindex(sorted(df["month"].unique()))
       .plot(ax=ax))
    ax.set_title(title); ax.set_xlabel("Month"); ax.set_ylabel("Count")
    plt.tight_layout()
