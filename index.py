import pandas as pd

file_path = 'sales_data.csv'

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['id'] = df['id'].astype(str)  
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def create_record(df, new_record):
    if new_record['id'] in df['id'].values:
        print(f"Record with id {new_record['id']} already exists. No new record added.")
    else:
        new_row = pd.DataFrame([new_record])
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df, file_path)
        print(f"New record added: {new_record}")
    return df

def read_records(df, product_name):
    result = df[df['Product name'] == product_name]
    print(f"Records for product '{product_name}':")
    print(result)
    return result

def update_record(df, order_id, new_data):
    if order_id in df['id'].values:
        df.loc[df['id'] == order_id, 'Quantity'] = new_data['Quantity']
        df.loc[df['id'] == order_id, 'Price'] = new_data['Price']
        save_data(df, file_path)
        print(f"Record with id {order_id} updated.")
    else:
        print(f"Record with id {order_id} not found. No update performed.")
    return df

def delete_record(df, order_id):
    if order_id in df['id'].values:
        df = df[df['id'] != order_id]
        save_data(df, file_path)
        print(f"Record with id {order_id} deleted.")
    else:
        print(f"Record with id {order_id} not found. No deletion performed.")
    return df

# Example usage
if __name__ == "__main__":
    # Load initial data from CSV
    df = load_data(file_path)

    # CREATE operation: Insert a new record (only if the ID does not already exist)
    new_record = {'id': '4', 'Product name': 'Tablet', 'Quantity': 10, 'Price': 450.00, 'Date': '2025-01-14',
                  'id': '8', 'Product name': 'AC', 'Quantity': 50, 'Price': 200.00, 'Date': '2025-08-14',
                  'id': '6', 'Product name': 'Fan', 'Quantity': 20, 'Price': 7500.00, 'Date': '2025-12-14',
                  'id': '5', 'Product name': 'abc', 'Quantity': 10, 'Price': 4500.00, 'Date': '2025-03-14',
                  'id': '10', 'Product name': 'Tablet', 'Quantity': 10, 'Price': 4500.00, 'Date': '2025-01-14'}
    df = create_record(df, new_record)

    # READ operation: Retrieve all records for 'Laptop'
    df_laptop = read_records(df, 'Laptop')

    # UPDATE operation: Change the quantity and price for id '4'
    updated_data = {'Quantity': 15, 'Price': 500.00}
    df = update_record(df, '4', updated_data)

    # DELETE operation: Remove the record with id '4'
    df = delete_record(df, '3')

    # View final dataset after operations
    print("Final dataset after operations:")
    print(df)




