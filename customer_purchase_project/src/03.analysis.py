import pandas as pd, os
from src.features import add_time_features
def save_summaries(df):
    os.makedirs(os.path.join('outputs','tables'), exist_ok=True)
    if 'total_price' in df.columns:
        top = df.groupby(['customer_id']).agg(total_revenue=('total_price','sum')).reset_index().sort_values('total_revenue', ascending=False)
        top.to_csv(os.path.join('outputs','tables','top_customers.csv'), index=False)
        monthly = add_time_features(df).groupby('order_month').agg(total_revenue=('total_price','sum')).reset_index()
        monthly.to_csv(os.path.join('outputs','tables','monthly_revenue.csv'), index=False)
        print('Saved summaries')
    else:
        print('No total_price column found')
def main():
    df = pd.read_csv(os.path.join('data','processed','dataset_clean.csv'), parse_dates=True)
    save_summaries(df)
if __name__ == '__main__':
    main()
