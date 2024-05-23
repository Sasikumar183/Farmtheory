import pandas as pd

sales_data = pd.read_csv('./sales_data.csv')
buying_data = pd.read_csv('./buy_data.csv')


#Q1
sales_data['sales_price'] = sales_data['total_revenue'] / sales_data['sku_quantity']
print("Q1: Sales Prices")
print(sales_data[['selling_date', 'customer_id', 'sku_name', 'sales_price']])

#Q2
total_bill = sales_data.groupby(['selling_date', 'customer_id'])['total_revenue'].sum().reset_index()
total_bill.columns = ['selling_date', 'customer_id', 'total_bill']
print("Q2: Total Customer Bill")
print(total_bill)


#Q3
buying_data['buying_date'] = pd.to_datetime(buying_data['buying_date'])
sales_data['selling_date'] = pd.to_datetime(sales_data['selling_date'])
buying_data['selling_date'] = buying_data['buying_date'] + pd.Timedelta(days=1)

merged_data = pd.merge(
    sales_data,
    buying_data,
    how='left',
    on=['sku_name', 'selling_date']
)
print("Q3: Merged Data")
print(merged_data)


#Q4
merged_data['gross_margin'] = merged_data['sales_price'] - merged_data['buying_price']
print("Q4: Gross Margin")
print(merged_data[['selling_date', 'sku_name', 'gross_margin']])


#Q5
highest_gross_margin = merged_data.loc[merged_data.groupby('selling_date')['gross_margin'].idxmax()]
print("Q5: Highest Selling Gross Margin SKU")
print(highest_gross_margin[['selling_date', 'sku_name', 'gross_margin']])
