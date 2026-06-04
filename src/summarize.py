from pathlib import Path
import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/demo_public_budget.csv')
    parser.add_argument('--output-dir', default='reports')
    args = parser.parse_args()
    df = pd.read_csv(args.input)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    for col in ['agency', 'category', 'supplier', 'month']:
        df.groupby(col, as_index=False)['amount'].sum().sort_values('amount', ascending=False).to_csv(out / f'{col}_summary.csv', index=False)
    print(out)


if __name__ == '__main__':
    main()
