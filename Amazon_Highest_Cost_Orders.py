# Import your libraries
import pandas as pd
import datetime as dt
from functools import reduce

# Start writing code
df1 = customers.drop_duplicates()
df2 = orders.drop_duplicates()

# Join df1 and df2 together
#df3 = pd.merge(df2, df1, how = 'left', left_on = 'cust_id', right_on = 'id')
df_list = [df2, df1]
df3 = reduce(lambda l,r: pd.merge(l, r, left_on = 'cust_id', right_on = 'id',how = 'left'), df_list)

# Create date variable 
df3['date'] = df3.order_date.dt.date

# Group by id and date, then sum the cost
df4 = df3.groupby(['first_name', 'date'])['total_order_cost'].sum().reset_index(name = 'cost')

x = dt.datetime(2019, 2, 1).date()
y = dt.datetime(2019, 5, 1).date()

# query out the highest daily cost between 2019-02-01 and 2019-05-01

df4[(df4.date >= x) & (df4.date <= y) & (df4.cost == df4.cost.max())]

#not working df4.query('cost == cost.max() & date >= "2019-02-01"')

# -------------------------------------------
# Another way without using datetime library
# Import your libraries
import pandas as pd
#import datetime as dt
from functools import reduce

# Start writing code
df1 = customers.drop_duplicates()
df2 = orders.drop_duplicates()

# Join df1 and df2 together
#df3 = pd.merge(df2, df1, how = 'left', left_on = 'cust_id', right_on = 'id')
df_list = [df2, df1]
df3 = reduce(lambda l,r: pd.merge(l, r, left_on = 'cust_id', right_on = 'id',how = 'left'), df_list)

# Create date variable 
#df3['date'] = df3.order_date.dt.date

# Group by id and date, then sum the cost
df4 = df3.groupby(['first_name', 'order_date'])['total_order_cost'].sum().reset_index(name = 'cost')

#x = dt.datetime(2019, 2, 1).date()
#y = dt.datetime(2019, 5, 1).date()

#query out the highest daily cost between 2019-02-01 and 2019-05-01

#df4[(df4.date >= x) & (df4.date <= y) & (df4.cost == df4.cost.max())]

df4.query('cost == cost.max() & order_date >= "2019-02-01" & order_date <= "2019-05-01"')
