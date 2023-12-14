import psycopg2               # įsikeliame psycopg2 darbui su SQL

# Susikuriame funkciją, kuri mūsų duomenis įrašys į sql lentelę paėmus kintamajį df - DataFrame
def duomenu_irasymas_sql(df):
    # Apsirašome savo duomenų bazės informaciją
    db_host = 'localhost'
    db_name = 'filmai'
    db_user = 'postgres'
    db_password = 'psw'
    # Naudodamiesi duombazės informacija prisijungiame prie jos
    connection = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    # Sukuriame SQl komandinę eilutę, kuri mums sukurs nauja lentelę, jeigu tokios dar nėra su mūsų nurodytais atributais
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
    # Vykdome savo SQL komandinę eilutę
    cursor.execute(create_table_query)
    # Leidžiame vartotojui žinoti jog lentelė sukurta
    print('lentele sukurta')

    # Naudodami for ciklą einame per visas mūsų DataFrame reikšmes ir po vieną jas įrašome į duombazę
    for index, row in df.iterrows():
        # Sukuriame komandinę eilutę duomenų įrašymui į duombazę
        insert_query = '''
            INSERT INTO film(pavadinimas, metai, sertifikatas, ilgis, zanrai, raitingas)values(%s, %s, %s, %s, %s, %s)
            '''
        # Vykdome prieš tai sukurtą komandinę eilutę ir nurodome kokias reikšmes įrašinėsime
        cursor.execute(insert_query, (row['Title'], row['Year'], row['Certificate'], row['Length'], row['Genre'], row['Rating']))
        connection.commit()
    # Pranešame vartotojui jog duomenys yra įrašyti
    print('Duomenys įrašyti')

if __name__ == "__main__":
    # Šis kodas bus vydomas
    # jeigu kodas bus vykdomas kaip pagrindinė programa
    print('This is the main program!')