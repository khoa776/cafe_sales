import matplotlib.pyplot as plt
import pandas as pd

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

def visualize_revenue_by_item(revenue_by_item):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(list(revenue_by_item['item']), revenue_by_item['total_revenue_item'], color='blue')
    ax.set_xlabel('Item')
    ax.set_ylabel('Total Revenue($)')

    plt.title('DOANH THU THEO SAN PHAM')
    plt.show()

def visualize_revenue_by_item_types(revenue_by_item_type):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.pie(list(revenue_by_item_type['total_revenue_item_type'])
           ,autopct='%1.1f%%', startangle=140)

    plt.title('SO SANH DOANH THU DO AN VA DO UONG')
    plt.legend(list(revenue_by_item_type['item_type']),loc='center right')
    plt.show()

def main():
    df = pd.read_csv('../data/processed/clean_cafe_sales.csv')
    revenue_by_item = pd.read_csv('../data/processed/revenue_by_item.csv')
    revenue_by_item_type = pd.read_csv('../data/processed/revenue_by_item_type.csv')
    revenue_by_month = pd.read_csv('../data/processed/revenue_by_month.csv')
    revenue_by_payment_method = pd.read_csv('../data/processed/revenue_by_payment_method.csv')

    while True:
        print('Nhap 0 de dung\n')
        print('Nhap 1 de xem Doanh thu va Don hang theo thang\n')
        print('Nhap 2 de xem Doanh thu theo san pham\n')
        print('Nhap 3 de xem so sanh Doanh thu theo loai san pham\n')
        press = int(input())

        if press == 0:
            break
        elif press == 1:
            visualize_revenue_by_month(revenue_by_month)
        elif press == 2:
            visualize_revenue_by_item(revenue_by_item)
        elif press == 3:
            visualize_revenue_by_item_types(revenue_by_item_type)


if __name__ == '__main__':
    main()
