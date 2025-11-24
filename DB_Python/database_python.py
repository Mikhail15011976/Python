import psycopg2

conn = psycopg2.connect(database="PyBase", user="postgres", password="0404")
with conn.cursor() as cur:
    def delete_table(conn):
        cur.execute("""
                        drop table Phone;
                        drop table Client;
                        """)
        conn.commit()
    delete_table(conn)

# 1. Функция, создающая структуру БД(таблицы)

    def create_db(conn):
        cur.execute("""
                        CREATE TABLE IF NOT EXISTS Client(
                            id_client SERIAL PRIMARY KEY,
                            first_name VARCHAR(40) NOT NULL UNIQUE,
                            last_name VARCHAR(40) NOT NULL UNIQUE,
                            email VARCHAR(80) NOT NULL UNIQUE                            
                        );

                        CREATE TABLE IF NOT EXISTS Phone(
                            id_phone SERIAL PRIMARY KEY,                                                       
                            phone BIGINT UNIQUE,
                            id_client INTEGER NOT NULL REFERENCES Client(id_client)
                        );
                        """)

        conn.commit()
    create_db(conn)

# 2. Функция, позволяющая добавить нового клиента

    def add_client(conn):
        cur.execute("""
                        INSERT INTO Client(id_client, first_name, last_name, email)
                            VALUES(1, 'Михаил', 'Бабков', 'Mikhail.babkov@gmail.com'),                            
                                  (2, 'Сергей', 'Безруков', 'Sergei.bezrukov@gmail.com'),
                                  (3, 'Евгений', 'Евстигнеев', 'Evgenii.evstigneev@yandex.ru');                            
                        """)

        conn.commit()
    add_client(conn)

# 3. Функция, позволяющая добавить телефон для существующего клиента

    def add_phone(conn):
        cur.execute("""
                        INSERT INTO Phone(id_phone, id_client, phone)
                            VALUES(1, 1, 75449103322),
                                  (2, 1, 76463728234),
                                  (3, 2, 79489384436),
                                  (4, 3, NULL);
                        """)

        conn.commit()
    add_phone(conn)



# 7. Извлечение данных существующего клиента по имени

    def find_client_first_name(conn):

        cur.execute("""
                       SELECT id_client, first_name, last_name, email FROM Client
                       WHERE first_name=%s; 
                       """, ("Сергей",))
        return cur.fetchone()

    client = find_client_first_name(conn)
    print('Личные данные клиента', client)


# 7. Извлечение данных существующего клиента по фамилии

    def find_client_last_name(conn):

        cur.execute("""
                       SELECT id_client, first_name, last_name, email FROM Client
                       WHERE last_name=%s;                                              
                       """, ("Евстигнеев",))
        return cur.fetchone()


    client = find_client_last_name(conn)
    print('Личные данные клиента', client)


# 7. Извлечение данных существующего клиента по емэйл

    def find_client_email(conn):
        cur.execute("""
                        SELECT id_client, first_name, last_name, email FROM Client
                        WHERE email=%s;                                                  
                        """, ("Mikhail.babkov@gmail.com",))
        return cur.fetchone()


    client = find_client_email(conn)
    print('Личные данные клиента', client)


# 7. Извлечение данных существующего клиента по двум данным

    def find_client_two(conn):
        cur.execute("""
                        SELECT id_client, first_name, last_name, email FROM Client
                        WHERE first_name=%s and last_name=%s;                       
                        """, ("Сергей", "Безруков",))
        return cur.fetchone()


    client = find_client_two(conn)
    print('Личные данные клиента', client)

# 4. Функция, позволяющая изменить данные о клиенте

    def change_client(conn):
        cur.execute("""
                       UPDATE Client SET first_name=%s
                       WHERE id_client=%s;
                       """, ("Иван", 1))
        cur.execute("""
                       SELECT id_client, first_name, last_name, email FROM Client
                       WHERE id_client=%s;
                       """, (1,))
        return cur.fetchall()
    change_client(conn)

    client = change_client(conn)
    print('Измененные личные данные клиента', client)

# 4. Функция, позволяющая изменить данные о клиенте (метод cur.rowcount)

    def change_client(conn):
        cur.execute("""
                       UPDATE Client SET first_name=%s 
                       WHERE id_client=%s;
                       """, ("Иван", 1))
        conn.commit()
        return cur.rowcount
    change_client(conn)

    count_string = change_client(conn)
    print('Количество измененных строк', count_string)

# 5. Функция, позволяющая удалить телефон для существующего клиента

    def delete_phone(conn):
        cur.execute("""
                        DELETE FROM Phone
                        WHERE id_phone=%s; 
                        """, (4,))
        cur.execute("""
                        SELECT id_phone, id_client, phone from Phone;                                          
                        """)
        print('Проверка удаления номера клиента', cur.fetchall())
    delete_phone(conn)

# 6. Функция, позволяющая удалить существующего клиента

    def delete_client(conn):
        cur.execute("""
                        DELETE FROM Phone
                        WHERE id_client=%s; 
                        """, (1,))
        cur.execute("""
                       DELETE FROM Client
                       WHERE id_client=%s; 
                       """, (1,))
        cur.execute("""
                       SELECT id_client, first_name, last_name, email FROM Client;                       
                       """)
        print('Проверка удаления клиента', cur.fetchall())
    delete_client(conn)




conn.close()








