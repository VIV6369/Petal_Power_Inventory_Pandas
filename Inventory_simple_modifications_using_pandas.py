#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
#1 Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.

inventory = pd.read_csv('inventory.csv')

#2 Inspect the first 10 rows of inventory.

print(inventory.head(10))

#3 The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.

staten_island = inventory[:10]
print(staten_island)

#4 A customer just emailed you asking what products are sold at your Staten Island location. 
# Select the column product_description from staten_island and save it to the variable product_request.

product_request = staten_island.product_description
print(product_request)

#5 Another customer emails to ask what types of seeds are sold at the Brooklyn location.
# Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

#6 Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.

inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
print(inventory)

#7 Petal Power wants to know how valuable their current inventory is.
# Create a column called total_value that is equal to price multiplied by quantity.

inventory['total_value'] = round(inventory.price * inventory.quantity,2)
print(inventory)

#8 The Marketing department wants a complete description of each product for their catalog.
# The following lambda function combines product_type and product_description into a single string:

combine_lambda = lambda row:     '{} - {}'.format(row.product_type,
                     row.product_description)

#9 Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)
