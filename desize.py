def desize(df):
""" 
Given a dataframe, reduce size of columns
"""
    flt_cols = [i for i in df if df[i].dtype == "float64"]
    int_cols = [i for i in df if df[i].dtype in ["int64"]]
    df[flt_cols] = df[flt_cols].astype(np.float32)
    df[int_cols] = df[int_cols].astype(np.int16)
    return df
