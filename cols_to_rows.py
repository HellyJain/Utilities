def colstorows(df, col_vals, key, value):
"""
Given a dataframe, transform columns to rows
"""
    assert type(df) is pd.DataFrame
    keep_vars = df.columns.difference(col_vals)
    melted_sections = []
    for c in col_vals:
        melted_c = df[keep_vars].copy()
        melted_c[key] = c
        melted_c[value] = df[c]
        melted_sections.append(melted_c)
    melted = pd.concat(melted_sections)
    return melted
