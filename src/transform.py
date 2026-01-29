import pandas as pd
import numpy as np

def extract_date(df):
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df['year'] = df['transaction_date'].dt.year
    df['month'] = df['transaction_date'].dt.month
    df['day'] = df['transaction_date'].dt.day
    df['weekday'] = df['transaction_date'].dt.day_name()
    return df

def item_classification(df):
    drink = ['Juice', 'Coffee', 'Smoothie', 'Tea']
    df['item_type'] = np.where(df['item'].isin(drink), 'drink', 'food' )
    return df

def month_revenue(df):
    month_revenue = (
        df.groupby(["year", "month"],as_index=False)
        .agg(
            total_revenue_month = ('total_spent', 'sum'),
            total_order_month = ('transaction_id', 'count')
        )
    )
    return month_revenue

def item_revenue(df):
    item_revenue = (
        df.groupby("item", as_index=False)
        .agg(
            total_revenue_item = ('total_spent', 'sum'),
            total_quantity_item = ('quantity', 'sum'),
        )
    )
    drink = ['Juice', 'Coffee', 'Smoothie', 'Tea']
    item_revenue['item_type'] = np.where(item_revenue['item'].isin(drink), 'drink', 'food' )
    return item_revenue

def item_types_revenue(df):
    item_types = (
        df.groupby("item_type", as_index=False)
        .agg(
            total_revenue_item_type = ('total_spent', 'sum'), )
    )
    return item_types

def payment_revenue(df):
    payment_revenue = (
        df.groupby("payment_method", as_index=False)
        .agg(
            total_revenue_payment = ('total_spent', 'sum'),
            total_order = ('transaction_id', 'count'),
        )
    )
    return payment_revenue

def main():
    df = pd.read_csv('../data/processed/clean_cafe_sales.csv')

    df = extract_date(df)
    df = item_classification(df)

    revenue_by_month = month_revenue(df)
    revenue_by_item = item_revenue(df)
    revenue_by_payment_method = payment_revenue(df)
    revenue_by_item_type = item_types_revenue(df)

#   ==== SORT ====
    revenue_by_month = revenue_by_month.sort_values(['year', 'month'], ascending=True)
    revenue_by_item = revenue_by_item.sort_values('total_revenue_item', ascending=False)
    revenue_by_payment_method = revenue_by_payment_method.sort_values('total_revenue_payment', ascending=False)

#   ==== SAVE ====
    revenue_by_month.to_csv("../data/processed/revenue_by_month.csv", index=False)
    revenue_by_item.to_csv("../data/processed/revenue_by_item.csv", index=False)
    revenue_by_payment_method.to_csv("../data/processed/revenue_by_payment_method.csv", index=False)
    revenue_by_item_type.to_csv("../data/processed/revenue_by_item_type.csv", index=False)

if __name__ == '__main__':
    main()