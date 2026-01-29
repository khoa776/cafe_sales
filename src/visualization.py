import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize_revenue_by_month(revenue_by_month):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.bar(list(revenue_by_month['month']), revenue_by_month['total_order_month'])
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Order')

    ax2 = ax1.twinx()
    ax2.plot(list(revenue_by_month['month']), revenue_by_month['total_revenue_month'], color='red',
             label='revenue by month')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Total Revenue($)')

    plt.title('BIEN DONG DOANH THU VA DON HANG THEO THANG')
    plt.show()

def main():
    df = pd.read_csv('../data/processed/clean_cafe_sales.csv')
    revenue_by_item = pd.read_csv('../data/processed/revenue_by_item.csv')
    revenue_by_month = pd.read_csv('../data/processed/revenue_by_month.csv')
    revenue_by_payment_method = pd.read_csv('../data/processed/revenue_by_payment_method.csv')

    visualize_revenue_by_month(revenue_by_month)

if __name__ == '__main__':
    main()
