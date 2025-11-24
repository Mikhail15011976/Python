import psycopg2
from pprint import pprint

# 1. Функция, создающая структуру БД(таблицы)

def create_db(cur):
    cur.execute("""
                        CREATE TABLE IF NOT EXISTS Client(
                            id_client SERIAL PRIMARY KEY,
                            first_name VARCHAR(40) NOT NULL UNIQUE,
                            last_name VARCHAR(40) NOT NULL UNIQUE,
                            email VARCHAR(100) NOT NULL UNIQUE                            
                        );

                        CREATE TABLE IF NOT EXISTS Phone(
                            id_phone SERIAL PRIMARY KEY,                                                       
                            phone BIGINT UNIQUE,
                            id_client INTEGER NOT NULL REFERENCES Client(id_client)
                        );
                        """)


# 2. Функция, позволяющая добавить нового клиента

def add_client(cur, id_client, first_name, last_name, email):
    cur.execute("""
                        INSERT INTO Client(id_client, first_name, last_name, email)
                        VALUES(%s, %s, %s, %s);                           
                        """, (id_client, first_name, last_name, email))


# 3. Функция, позволяющая добавить телефон для существующего клиента

def add_phone(cur, id_phone, id_client, phone):
    cur.execute("""
                        INSERT INTO Phone(id_phone, id_client, phone)
                            VALUES(%s, %s, %s);                            
                        """, (id_phone, id_client, phone))


# 7. Извлечение данных существующего клиента по имени

def find_client_first_name(cur, first_name):
    cur.execute("""
                       SELECT * FROM Client
                       WHERE first_name=%s; 
                       """, (first_name,))
    return cur.fetchone()


# 7. Извлечение данных существующего клиента по фамилии

def find_client_last_name(cur, last_name):
    cur.execute("""
                       SELECT * FROM Client
                       WHERE last_name=%s;                                              
                       """, (last_name,))
    return cur.fetchone()



# 7. Извлечение данных существующего клиента по емэйл

def find_client_email(cur, email):
    cur.execute("""
                        SELECT * FROM Client
                        WHERE email=%s;                                                  
                        """, (email,))
    return cur.fetchone()


# 7. Извлечение данных существующего клиента по двум данным

def find_client_two(cur, first_name, last_name):
    cur.execute("""
                        SELECT * FROM Client
                        WHERE first_name=%s and last_name=%s;                       
                        """, (first_name, last_name,))
    return cur.fetchone()


# 4. Функция, позволяющая изменить данные о клиенте

def change_client(cur, first_name, id_client):
    cur.execute("""
                       UPDATE Client SET first_name=%s
                       WHERE id_client=%s;
                       """, (first_name, id_client,))
    cur.execute("""
                       SELECT * FROM Client
                       WHERE id_client=%s;
                       """, (id_client,))
    return cur.fetchall()


# 4. Функция, позволяющая изменить данные о клиенте (метод cur.rowcount)

def change_client2(cur, first_name, id_client):
    cur.execute("""
                       UPDATE Client SET first_name=%s 
                       WHERE id_client=%s;
                       """, (first_name, id_client,))
    return cur.rowcount


# 5. Функция, позволяющая удалить телефон для существующего клиента

def delete_phone(cur, id_phone):
    cur.execute("""
                        DELETE FROM Phone
                        WHERE id_phone=%s; 
                        """, (id_phone,))
    cur.execute("""
                        SELECT id_phone, id_client, phone from Phone;                                          
                        """)
    return cur.fetchall()


# 6. Функция, позволяющая удалить существующего клиента

def delete_client(cur, id_client):
    cur.execute("""
                        DELETE FROM Phone
                        WHERE id_client=%s; 
                        """, (id_client,))
    cur.execute("""
                       DELETE FROM Client
                       WHERE id_client=%s; 
                       """, (id_client,))
    cur.execute("""
                       SELECT * FROM Client;                       
                       """)
    return cur.fetchall()
    #print('Проверка удаления клиента', cur.fetchall())


if __name__ == "__main__":
    with psycopg2.connect(database="PyBase", user="postgres", password="0404") as conn:
        with conn.cursor() as cur:
            def delete_table(cursor):
                cur.execute("""
                            drop table Phone;
                            drop table Client;
                            """)
                conn.commit()
            delete_table(cur)

            create_db(cur)
            conn.commit()

            client1 = add_client(cur, 1, 'Михаил', 'Бабков', 'Mikhail.babkov@gmail.com')
            client2 = add_client(cur, 2, 'Сергей', 'Безруков', 'Sergei.bezrukov@gmail.com')
            client3 = add_client(cur, 3, 'Евгений', 'Евстигнеев', 'Evgenii.evstigneev@yandex.ru')
            phone1 = add_phone(cur, 1, 1, 75449103322)
            phone2 = add_phone(cur, 2, 1, 76463728234)
            phone3 = add_phone(cur, 3, 2, 79489384436)
            phone4 = add_phone(cur, 4, 3, phone=None)
            conn.commit()


            name_client = find_client_first_name(cur, "Евгений")
            print('Личные данные клиента', name_client)
            last_name_client = find_client_last_name(cur, "Безруков")
            print('Личные данные клиента', last_name_client)
            email_client = find_client_email(cur, 'Mikhail.babkov@gmail.com')
            print('Личные данные клиента', email_client)
            two_client = find_client_two(cur, 'Сергей', 'Безруков',)
            print('Личные данные клиента', two_client)
            change_client = change_client(cur, "Иван", 1)
            print('Измененные личные данные клиента', change_client)
            change_client2 = change_client2(cur, "Анатолий", 1)
            print('Количество измененных строк', change_client2)
            delete_phone = delete_phone(cur, 4)
            print('Проверка удаления номера клиента', delete_phone)
            delete_client = delete_client(cur, 1)
            print('Проверка удаления клиента', delete_client)



    conn.close()








