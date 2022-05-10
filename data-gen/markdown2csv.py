import pandas as pd
import argparse

def md_to_df(md_path):
    df = pd.read_table(md_path, sep="|", header=0, index_col=1, skipinitialspace=True).dropna(axis=1, how='all').iloc[1:]
    df.columns = df.columns.str.strip()
    return df

def md_to_csv(md_path, csv_path):
    df = md_to_df(md_path)
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown table to CSV')
    parser.add_argument('--md', type=str, help='path to the source markdown file')
    parser.add_argument('--csv', type=str, help='path to the destination csv file')
    args = parser.parse_args()
    md_to_csv(args.md, args.csv)

