import psycopg2

conn = psycopg2.connect(host="localhost",user="postgres",dbname="my_duka",password="P&ssw@rd1!%#",port="5432")

cur =conn.cursor()

cur.execute("select * from products;")
row =cur.fetchall()

for row in row:
    print(row)

cur.execute("insert into products (id,name,buying_price,selling_price)values(%s,%s,%s,%s)",(6,'sugar',50,100))
conn.commit()

cur.execute('select * from products;')
row =cur.fetchall()

for row in row:
    print(row)

def delete_products():
    cur.execute("delete from products")
    conn.commit()

prdt_data=delete_products()
print(prdt_data)



def insert_products(values):
    cur.execute(f"insert into products(id,name,buying_price,selling_price)values{values}")
    conn.commit()

    product1=('shoes',1000,1500)
    product2=('phone',1500,2000)

prd_data=insert_products()
print(prd_data)

# sales


def insert_sales(values):
    cur.execute("insert into ales (id,sales_quantity)values(%s,%s)", values)
conn.commit()

#  Routing: Connecting URLs to Python functions

# We import data from different files and work on them inside one python file

@app.route("/products")
def products():
    







