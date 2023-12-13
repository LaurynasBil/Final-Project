import psycopg2

def duomenu_irasymas_sql(df):
    db_host = 'localhost'
    db_name = 'filmai'
    db_user = 'postgres'
    db_password = 'psw'
    connection = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS film(
            id SERIAL PRIMARY KEY,
            pavadinimas varchar(255),
            metai integer,
            sertifikatas varchar,
            ilgis integer,
            zanrai text,
            raitingas decimal(10,2)
        )
    '''
    cursor.execute(create_table_query)
    print('lentele sukurta')

    for index, row in df.iterrows():
        insert_query = '''
            INSERT INTO film(pavadinimas, metai, sertifikatas, ilgis, zanrai, raitingas)values(%s, %s, %s, %s, %s, %s)
            '''
        cursor.execute(insert_query, (row['Title'], row['Year'], row['Certificate'], row['Length'], row['Genre'], row['Rating']))
        connection.commit()
    print('Duomenys įrašyti')

if __name__ == "__main__":
    print('This is the main program!')