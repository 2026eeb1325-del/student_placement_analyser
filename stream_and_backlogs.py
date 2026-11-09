"""Member 2 - Stream and backlog analysis.
Run from the repo folder:  python stream_and_backlogs.py
Needs: pandas, matplotlib  (placements.csv in same folder)
Outputs: stream_summary.csv, backlog_summary.csv, stream_placement.png, backlog_placement.png
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("placements.csv")

def summarise(data, col):
    t = data.groupby(col)["PlacedOrNot"].agg(Total_Students="count", Placed="sum")
    t["Not_Placed"] = t["Total_Students"] - t["Placed"]
    t["Placement_%"] = (t["Placed"] / t["Total_Students"] * 100).round(2)
    return t.sort_values("Placement_%", ascending=False)

streams = summarise(df, "Stream")
backlog = summarise(df, "HistoryOfBacklogs")
backlog.index = backlog.index.map({0: "No backlog history", 1: "Has backlog history"})

print("Overall placement %:", round(df.PlacedOrNot.mean() * 100, 2))
print("\nBy stream:\n", streams, "\n\nBy backlog history:\n", backlog)
streams.to_csv("stream_summary.csv")
backlog.to_csv("backlog_summary.csv")

# Robustness check: dataset has many repeated rows, so also look at unique rows only
uniq = df.drop_duplicates()
print("\nRows:", len(df), "| unique rows:", len(uniq))
print("\nUnique-rows stream check:\n", summarise(uniq, "Stream")["Placement_%"])
print("\nUnique-rows backlog check:\n", summarise(uniq, "HistoryOfBacklogs")["Placement_%"])

overall = df.PlacedOrNot.mean() * 100

def bar(t, title, fname, color, figsize):
    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(t.index, t["Placement_%"], color=color)
    ax.axhline(overall, ls="--", color="grey")
    ax.text(len(t) - 0.5, overall + 1, f"Overall {overall:.1f}%", ha="right", color="grey")
    for b, (_, r) in zip(bars, t.iterrows()):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1,
                f"{r['Placement_%']:.1f}%\n({int(r['Placed'])}/{int(r['Total_Students'])})", ha="center", fontsize=9)
    ax.set_ylim(0, 80); ax.set_ylabel("Placement %"); ax.set_title(title)
    plt.xticks(rotation=20, ha="right")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(fname, dpi=200); plt.close()

bar(streams, "Placement % by engineering stream", "stream_placement.png", "#0F766E", (9, 5))
bar(backlog, "Placement % by backlog history", "backlog_placement.png", "#D97706", (6, 5))
