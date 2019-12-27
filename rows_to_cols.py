def rowstocols(df, key, value, join_how='outer'):
    """Given a dataframe, transform rows to 
        columns
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns and value in df.columns
    assert join_how in ['outer', 'inner']
    
    fixed_vars = df.columns.difference([key, value])
    tibble = pd.DataFrame(columns=fixed_vars) # empty frame
    
    new_vars = df[key].unique()
    for c in new_vars:
        df_v = df[df[key] == c]
        del df_v[key]
        df_v = df_v.rename(columns = {value:c})       
        tibble = tibble.merge(df_v, on=list(fixed_vars), how=join_how)
    return tibble
