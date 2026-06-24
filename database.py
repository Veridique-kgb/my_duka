import psycopg2

# Establishing a connection between sql and python
conn=psycopg2.connect(host='localhost',port='5432',user='postgres',password='P&ssw@rd1!%#',dbname='my_duka')

# cur object
cur =conn.cursor()

# cur.execute(): a function used to execute sql queries

cur.execute('select * from products')
product_data=cur.fetchall()
# print(product_data)

cur.execute("insert into products(name,buying_price,selling_price)values('shirt',1000,1500)")

# recording the data
conn.commit()
# print(product_data)

# # Using functions for multiple entries

# Method 1: susceptible to sql injection

def insert_products(values):
    cur.execute(f"insert into products (name,buying_price,selling_price)values{values}")
    conn.commit

product2=('phone',20000,25000)
product3=('Tv',30000,40000)

insert_products(product2)
insert_products(product3)

cur.execute("select * from products")
product_data=cur.fetchall()
# print(product_data)

# Method 2: More secure with no sql Injection

def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product4=('shoe',5000,5500)
product5=('milk',2000,2200)
insert_products2(product4)
insert_products2(product5)
cur.execute("select * from products")

products2_data=cur.fetchall()
# print(products2_data)

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity) values (%s,%s)",values)
    conn.commit()

sales1=(2,2)
sales2=(3,4)
sales3=(4,3)
sales4=(5,2)

insert_sales(sales1)
insert_sales(sales2)
insert_sales(sales3)
insert_sales(sales4)
cur.execute("select * from sales")

sales_data=cur.fetchall()
# print(sales_data)



def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",values)
    conn.commit()

stock1=(2,10)
stock2=(3,6)
stock3=(4,5)
stock4=(5,3)


insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)
insert_stock(stock4)

cur.execute("select * from stock")

stock_data=cur.fetchall()
# print(stock_data)


def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data
    

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def get_stock():
    cur.execute("select * from stock")
    stock_data = cur.fetchall()
    return stock_data


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data


def sales_per_day():
    cur.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = cur.fetchall()
    return daily_sales


def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price -
        products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by date;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit



def sales_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)  as total_sales
        from products join sales on sales.pid = products.id group by p_name;
    """)
    product_sales = cur.fetchall()
    return product_sales


def profit_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity *( products.selling_price - 
        products.buying_price))  as total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    product_profit = cur.fetchall()
    return product_profit

def check_available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid=%s",(pid,))
    total_stock=cur.fetchone()[0] or 0

    cur.execute("select sum(sales.quantity) from sales where pid=%s",(pid,))
    total_sold=cur.fetchone()[0] or 0

    return total_stock-total_sold

def check_user_exists(email):
    cur.execute("select * from users where users.email =%s",(email,))
    user=cur.fetchone()
    return user

def create_user(user_details):
    cur.execute("insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",user_details)
    conn.commit()

user = check_user_exists('johnkamau@gmail.com')
print(user)