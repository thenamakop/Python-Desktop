# generate_data.py

import numpy as np
import pandas as pd

def main():
    # 1. Generate synthetic dataset
    n = 1_000_000
    np.random.seed(42)
    timestamps = (
        pd.to_datetime('2024-01-01') +
        pd.to_timedelta(np.random.randint(0, 365*24*60*60, size=n), unit='s')
    )
    customer_ids = np.random.randint(1, 100_001, size=n)
    amounts = np.round(np.random.exponential(scale=50, size=n), 2)
    categories = np.random.choice(
        ['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports'],
        size=n, p=[0.2, 0.3, 0.25, 0.15, 0.1]
    )
    segments = np.random.choice(['New', 'Returning', 'VIP'], size=n, p=[0.5, 0.4, 0.1])

    df = pd.DataFrame({
        'transaction_id': np.arange(1, n+1),
        'customer_id': customer_ids,
        'timestamp': timestamps,
        'amount': amounts,
        'category': categories,
        'segment': segments
    })

    # 2. Feature engineering
    df['hour']         = df['timestamp'].dt.hour
    df['day_of_week']  = df['timestamp'].dt.day_name()
    df['month']        = df['timestamp'].dt.month_name()

    # 3. Save to CSV
    csv_path = 'ecommerce_transactions.csv'
    df.to_csv(csv_path, index=False)
    print(f"Saved {n}-row dataset to {csv_path}")

if __name__ == '__main__':
    main()
