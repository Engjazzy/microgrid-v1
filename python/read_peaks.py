import pandas as pd
df = pd.read_csv("python/peaks.csv")
print(df)
print(df["pac_w"] / df["sun_wm2"])