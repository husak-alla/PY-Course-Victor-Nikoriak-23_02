"""
Amazon-like e-commerce dataset generator.
Run: python generate_data.py
Creates amazon_ecommerce_1M.csv in the same directory.
"""
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)
N = 50_000  # 50k orders — representative sample

CATEGORIES = [
    'Electronics', 'Clothing', 'Books', 'Home & Garden',
    'Sports & Outdoors', 'Beauty', 'Toys', 'Food & Grocery',
]
STATUSES = ['Delivered', 'Returned', 'Cancelled', 'Pending']
STATUS_WEIGHTS = [0.73, 0.15, 0.08, 0.04]
RETURN_REASONS = [
    'Defective product', 'Wrong item shipped',
    'Changed mind', 'Not as described', 'Better price found',
]
PAYMENT_METHODS = ['Credit Card', 'Debit Card', 'PayPal', 'Amazon Pay', 'Gift Card']
REGIONS = ['North', 'South', 'East', 'West', 'Central']

data_file = Path(__file__).parent / 'amazon_ecommerce_1M.csv'

statuses = np.random.choice(STATUSES, N, p=STATUS_WEIGHTS)
prices = np.round(np.random.lognormal(3.5, 1.2, N).clip(1, 2000), 2)
quantities = np.random.choice([1, 1, 1, 2, 2, 3, 4, 5], N)
discounts = np.random.choice([0, 0, 0, 5, 10, 15, 20, 25, 30, 40, 50], N).astype(float)

df = pd.DataFrame({
    'order_id':       [f'ORD-{i:07d}' for i in range(1, N + 1)],
    'customer_id':    np.random.randint(1_000, 50_000, N),
    'product_id':     [f'PROD-{np.random.randint(1000, 9999)}' for _ in range(N)],
    'category':       np.random.choice(CATEGORIES, N),
    'seller_id':      [f'SELL-{np.random.randint(100, 999)}' for _ in range(N)],
    'order_date':     pd.date_range('2022-01-01', periods=N, freq='1h'),
    'price':          prices,
    'quantity':       quantities,
    'discount_pct':   discounts,
    'total_amount':   np.round(prices * quantities * (1 - discounts / 100), 2),
    'order_status':   statuses,
    'delivery_days':  np.random.randint(1, 20, N),
    'rating':         np.random.choice([1, 2, 3, 4, 4, 5, 5, 5], N),
    'payment_method': np.random.choice(PAYMENT_METHODS, N),
    'region':         np.random.choice(REGIONS, N),
    'return_reason':  [
        np.random.choice(RETURN_REASONS) if s == 'Returned' else None
        for s in statuses
    ],
})

df.to_csv(data_file, index=False)
size_mb = data_file.stat().st_size / 1024 / 1024
print(f'Done: {len(df):,} rows -> {data_file} ({size_mb:.1f} MB)')
