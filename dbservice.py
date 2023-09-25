# import psycopg2
# products=0
# def get_data(p):
#     conn = psycopg2.connect(
#      database="myduka_cls", user='postgres', password='admin', host='127.0.0.1', port= '5432' )
    
#     cursor = conn.cursor()

#     cursor.execute('''SELECT * from products''')

#     result = cursor.fetchall()
#     return result
# data=get_data(products)
# print(data)

import psycopg2
conn = psycopg2.connect(
    database="myduka_cls", user='postgres', password='admin', host='127.0.0.1', port= '5432')
def get_data(p):
    

    cursor = conn.cursor()
    s="select * from" +" "+ p

    cursor.execute(s)


    data = cursor.fetchall()
    
    
    return data



prod=get_data("products")
print(prod)
sales=get_data("sales")
print(sales)