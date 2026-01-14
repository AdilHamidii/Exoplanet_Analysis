import numpy as np
import pandas as pd

data = pd.read_csv(
    "exodata.csv",
    sep=",",
    comment="#",
    low_memory=False
)

planet_id = "pl_name"

numeric_cols = data.select_dtypes(include=[np.number]).columns
categorical_cols = data.select_dtypes(exclude=[np.number]).columns.drop(planet_id)

agg = {}

for col in numeric_cols:
    agg[col] = "median"

for col in categorical_cols:
    agg[col] = lambda x: x.dropna().iloc[0] if not x.dropna().empty else np.nan

clean_data = data.groupby(planet_id, as_index=False).agg(agg)

clean_data.to_csv("exodata_clean.csv", index=False)
