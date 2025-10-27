def add_time_features(df, date_col='order_date'):
    import pandas as pd
    if date_col in df.columns:
        df['order_month'] = pd.to_datetime(df[date_col]).dt.to_period('M').dt.to_timestamp()
        df['order_week'] = pd.to_datetime(df[date_col]).dt.to_period('W').dt.start_time
    return df
