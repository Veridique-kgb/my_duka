import psycopg2

# Establishing a connection between sql and python
conn=psycopg2.connect(host='localhost',port='5432',user='postgres',password='P&ssw@rd1!%#',dbname='my_duka')

# cur object
cur =conn.cursor()

# cur.execute(): a function used to execute sql queries

cur.execute('select * from products')
product_data=cur.fetchall()
print(product_data)

cur.execute("insert into products(name,buying_price,selling_price)values('shirt',1000,1500)")

# recording the data
conn.commit()
print(product_data)

# # Using functions for multiple entries

# Method 1: susceptible to sql injection

def insert_prodcuts(values):
    cur.execute(f"insert into products (name,buying_price,selling_price)values{values}")
    conn.commit

product2=('phone',20000,25000)
product3=('Tv',30000,40000)

insert_prodcuts(product2)
insert_prodcuts(product3)

cur.execute("select * from products")
product_data=cur.fetchall()
print(product_data)

# Method 2: More secure with no sql Injection

def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

def insert_sales(values):
    cur.execute("insert into sales(pid,sales_quantity)(%s,%s,%s)",values)
    conn.commit()

def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)(%s,%s,%s)",values)

product4=('shoe',5000,5500)
product5=('milk',2000,2200)
insert_products2(product4)
insert_products2(product5)


cur.execute("select * from products")

products2_data=cur.fetchall()
print(products2_data)

