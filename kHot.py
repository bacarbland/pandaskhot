def kHot(df,cols,dropna=False):    
    from pandas import get_dummies
    return pd.get_dummies(df[cols],prefix=['']*len(cols),prefix_sep='',columns=cols, dummy_na=~dropna).groupby(level=0, axis=1).sum()
