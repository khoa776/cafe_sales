import pandas as pd
import numpy as np

def clean_columns_name(df):
    df.columns = (                          #CHUAN HOA TEN COT
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )
    return df

def convert_types(df):
    df['price_per_unit'] = pd.to_numeric(df['price_per_unit'],errors='coerce')      #errors='coerce' BO QUA LOI
    df['quantity'] = pd.to_numeric(df['quantity'],errors='coerce')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'],errors='coerce')
    return df

def handle_missing(df):
    df = df.replace(
        ['',' ', 'UNKNOWN', 'N/A', 'ERROR'],pd.NA)                     #inplace=True THAY DOI TREN BANG HIEN TAI

    df = df.dropna(subset=['quantity','price_per_unit','item', 'transaction_date']).copy()

    df['location'] = df['location'].fillna('unknown')
    df['payment_method'] = df.loc[:,'payment_method'].fillna('unknown')

    return df

def remove_invalid_values(df):
    df = df[df["quantity"] > 0]
    df = df[df["price_per_unit"] > 0]
    return df

def recalculate_totals(df):
    df['total_spent'] = df['quantity'] * df['price_per_unit']
    return df

def main():
    df = pd.read_csv("../data/raw/dirty_cafe_sales.csv")
    df = clean_columns_name(df)
    df = convert_types(df)
    df = handle_missing(df)
    df = remove_invalid_values(df)
    df = recalculate_totals(df)
    pd.set_option('display.max_columns', None)
    df.to_csv("../data/processed/clean_cafe_sales.csv", index=False)

if __name__ == "__main__":
    main()



