import pandas as pd

def extract_date(df):
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df['year'] = df['transaction_date'].dt.year
    df['month'] = df['transaction_date'].dt.month
    df['day'] = df['transaction_date'].dt.day
    df['weekday'] = df['transaction_date'].dt.day_name()
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
    return item_revenue

def main():
    df = pd.read_csv('../data/processed/clean_cafe_sales.csv')
    print(df['transaction_date'].dtype)
    print(month_revenue(df))
    print(item_revenue(df))
    print(df['price_per_unit'].dtype)

if __name__ == '__main__':
    main()