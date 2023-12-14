import psycopg2               # įsikeliame psycopg2 darbui su SQL

# Susikuriame funkcija kuri mūsų duomenis įrašys į sql lentele paemus kintamajį df - DataFrame
def duomenu_irasymas_sql(df):
    # Apsirašome savo duomenų bazės informaciją
    db_host = 'localhost'
    db_name = 'filmai'
    db_user = 'postgres'
    db_password = 'psw'
    # Naudodamieji duombazes informacija prisijungiame prie jos
    connection = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    # Sukuriame SQl komandine eilute kuri mums sukurs nauja lentele jeigu tokios dar nėra su mūsų nurodytais atributais
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
    # Vykdome savo SQL komandine eilute
    cursor.execute(create_table_query)
    # Leidžiame vartotojui žinoti jog lentele sukurta
    print('lentele sukurta')

    # Naudodami for ciklą einame per visas mūsų DataFrame reikšmes ir po vieną jas įrašome į duombazę
    for index, row in df.iterrows():
        # Sukuriam komandine eilute duomenų įrašymui į duombazę
        insert_query = '''
            INSERT INTO film(pavadinimas, metai, sertifikatas, ilgis, zanrai, raitingas)values(%s, %s, %s, %s, %s, %s)
            '''
        # Vykdome pries tai sukurta komandine eilute ir nurodome kokias reikšmes įrašinėsime
        cursor.execute(insert_query, (row['Title'], row['Year'], row['Certificate'], row['Length'], row['Genre'], row['Rating']))
        connection.commit()
    # Pranešame vartotojui jog duomenys yra įrašyti
    print('Duomenys įrašyti')

if __name__ == "__main__":
    # Šis kodas bus vydomas
    # jeigu kodas bus vykdomas kaip pagrindinė programa
    print('This is the main program!')