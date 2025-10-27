import pandas as pd
from src.data_prep import clean_df
def test_clean_df():
    df = pd.DataFrame({'a':[1,2,3],'price':[10,20,30],'quantity':[1,0,2]})
    out = clean_df(df)
    assert out is not None
