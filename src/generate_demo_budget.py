from pathlib import Path
import argparse
import numpy as np
import pandas as pd


def generate(rows=1200, seed=42):
    rng = np.random.default_rng(seed)
    agencies = ['Health', 'Education', 'Infrastructure', 'Administration', 'Social Assistance']
    categories = ['Services', 'Supplies', 'Equipment', 'Maintenance', 'Training']
    suppliers = [f'Supplier {i:03d}' for i in range(1, 61)]
    dates = pd.date_range('2025-01-01', periods=365, freq='D')
    df = pd.DataFrame({
        'record_id': range(1, rows + 1),
        'date': rng.choice(dates, rows),
        'agency': rng.choice(agencies, rows),
        'category': rng.choice(categories, rows),
        'supplier': rng.choice(suppliers, rows),
        'amount': rng.lognormal(mean=8.2, sigma=0.8, size=rows).round(2),
    })
    df['month'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=1200)
    parser.add_argument('--output', default='data/demo_public_budget.csv')
    args = parser.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    generate(args.rows).to_csv(out, index=False)
    print(out)


if __name__ == '__main__':
    main()
