
from pyspark.sql.functions import *

# transformations defined as follows:

# 1. filter the orders dataframe based on order_status
# 2. join the orders filtered with customers (customer_id)
# 3. do a groupby on state and do the aggregation

def filter_closed_orders(orders_df):
    return orders_df.filter("order_status = 'CLOSED'")

def join_orders_customers(orders_df, customers_df):
    return orders_df.join(customers_df, "customer_id")

def count_orders_state(joined_df):
    return joined_df.groupBy('state').count()