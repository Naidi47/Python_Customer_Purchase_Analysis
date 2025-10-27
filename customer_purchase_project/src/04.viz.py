import os, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
def plot_monthly():
    p = os.path.join('outputs','tables','monthly_revenue.csv')
    if not os.path.exists(p):
        print('Run analysis first')
        return
    df = pd.read_csv(p, parse_dates=['order_month'])
    plt.figure(figsize=(8,4))
    sns.lineplot(data=df, x='order_month', y='total_revenue', marker='o')
    os.makedirs('outputs/figures', exist_ok=True)
    plt.savefig('outputs/figures/monthly_revenue.png', dpi=150)
    plt.close()
    print('Saved figure')
if __name__ == '__main__':
    plot_monthly()
