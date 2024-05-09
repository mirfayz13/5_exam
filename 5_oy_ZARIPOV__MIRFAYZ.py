####### 1 SAVOL ############

import psycopg2

host = 'localhost'
user = 'postgres'
password = 'Bukhara04'
port = 5433

conn = psycopg2.connect(
                        host = host,
                        user = user,
                        password = password,
                        port = 5433
)

cur = conn.cursor()
create_product_table = """
      create_table_product(
            id serial primary key,
            name varchar(30),
            price int,
            color varchar(30),
            image varchar(30));

"""
#cur.execute(create_product_table)
#conn.commit()

insert_product = """
      insert into
product(name,price,color,image)
values('milk',300,'white','black');
"""
#cur.execute(insert_product)
#conn.commit()

#############  2 savol  #####################
#insert product,select all products,update product,delete product

def insert_product(cur,table_name, column, values):
    try:
        cur.execute(F"INSERT INTO {table_name} ({column}) VALUES ({values});")
        print("Data Entered ")
    except Exception as e:
        print(f"Error: {e}")


def update_product(cur,table_name, column):
    try:
        cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column};")
        print(f"Column '{column}' is added ")
    except Exception as e:
        print(f"Error : {e}")

def delete_product(cur,table_name):
    try:
        cur.execute(f" TABLE {table_name};")
        print("Deleted Table!")
    except Exception as e:
        print(f"Error: {e}")

def select_from(cur,table_name):
    try:
        select_car_query = f'''select * from {table_name} ;'''
        cur.execute(select_car_query)
        for user in cur.fetchall():
              print(user)
    except Exception as e:
              print(f"Error in the name of table: {e}")


 ############# 3 SAVOL ####################

class Alphabet:
    def __init__(self):
        self.letters = 'qwertyuiopasdfghjklzxcvbnm'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.letters):
            current_letter = self.letters[self.index]
            self.index += 1
            return current_letter
        else:
            raise StopIteration
        
alphabet = Alphabet()
for letter in alphabet:
    print(letter)


########### 4 SAVOL ##############
import threading
import time

def print_numbers(start, end):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)

def print_letters():
    letters = 'ABCDE'
    for letter in letters:
        print(letter)
        time.sleep(1)

number_thread = threading.Thread(target=print_numbers, args=(1, 5))
letter_thread = threading.Thread(target=print_letters)

number_thread.start()
letter_thread.start()

number_thread.join()
letter_thread.join()

print("The End")


######### 5 SAVOL ##############
#(id,name,price, color,image) 

class Product:
    def __init__(self, id, name, price, color,image):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):

        print("saving product to the database:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Color:", self.color)
        print("Image",self.image)


product1 = Product(12,'Milk',300,'white','black')
product1.save()

product2 = Product(13,'Chocolate',400,'white','black')
product2.save()


######## 6 SAVOL ##########
import psycopg2

class DbConnect:
    def __init__(self, dbname, user, password, host='localhost', port=5433):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
            return self.conn, self.cur
        except psycopg2.Error as e:
            print('Not connected to the database')

