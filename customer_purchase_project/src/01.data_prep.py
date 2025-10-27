import pandas as pd, os
def load_excel(path):
    return pd.read_excel(path, sheet_name=0)
def infer_date_col(df):
    for c in df.columns:
        if 'date' in c.lower():
            return c
    return None
def clean_df(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    date_col = infer_date_col(df)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    # numeric coercion
    for c in df.columns:
        if df[c].dtype == object:
            coerced = pd.to_numeric(df[c], errors='coerce')
            if coerced.notna().sum() > len(df)/2:
                df[c] = coerced
    # add total_price if possible
    lowcols = [c.lower() for c in df.columns]
    if 'quantity' in lowcols and 'price' in lowcols:
        q = [c for c in df.columns if c.lower()=='quantity'][0]
        p = [c for c in df.columns if c.lower()=='price'][0]
        df['total_price'] = df[q]*df[p]
    return df
def main():
    inp = os.path.join('data','raw','dataset_original.xlsx')
    out = os.path.join('data','processed','dataset_clean.csv')
    df = load_excel(inp)
    dfc = clean_df(df)
    dfc.to_csv(out, index=False)
    print('Wrote', out)
if __name__ == '__main__':
    main()
