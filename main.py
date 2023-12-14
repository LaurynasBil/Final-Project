import pandas as pd                         # įsikeliame pandas darbui su DataFrame
from scraping import scrape                 # įsikeliame mūsų sukurtą funkciją scrape iš scraping failo
from writesql import duomenu_irasymas_sql   # įsikeliame mūsų sukurtą funkciją duomenų_įrašymas_sql iš writesql failo
import matplotlib.pyplot as plt             # įsikeliame matplotlib.pyplot darbui su grafikais, pasivadiname jį 'plt'
import seaborn as sns                       # įsikeliame seaborn darbui su grafikais, pasivadiname jį 'sns'


# Vykdome duomenų nuskaitymą ir įrašymą per mūsų sukurtą scrape funkciją, kuri grąžina DataFrame
df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
# Apjungiame mūsų abu DataFrames į vieną, kad galėtume toliau vykdyti duomenų analizę
result = pd.concat([df1, df2])
# Duomenis įrašome į csv failą, kad nereikėtų kiekvieną kartą laukti, kol surinks duomenis iš svetainės
result.to_csv("result.csv", index = False)
df = pd.read_csv('result.csv')
# Taip pat duomenis įsirašome į savo duombazę per mūsų sukurtą funkciją 'duomenu_irasymas_sql'
# kur reikia nurodyti DataFrame, kurį naudosime įrašymui
duomenu_irasymas_sql(df)

##### Duomenu Analizė #####
avg_rating = df['Rating'].mean()      # - įvertinimų vidurkis
print(f'Vidutinis filmų įvertinimas yra: {avg_rating:.2f}')
min_rating = df['Rating'].min()   # - randam minimalią įvertinimų reikšmę
print(f'Minimalus filmų įvertinimas: {min_rating}')
max_rating = df['Rating'].max()  # - randam maksimalią įvertinimų reikšmę
print(f'Maksimalus filmų įvertinimas: {max_rating}')

avg_length = df['Length'].mean()    # - filmų trukmės vidurkis
print(f'Vidutinė filmų trukmė yra: {avg_length:.2f} min')
min_length = df['Length'].min()   # - randam minimalią trukmės reikšme
print(f'Minimali filmo trukmė: {min_length} min')
max_length = df['Length'].max()  # - randam maksimalią trukmės reikšmę
print(f'Maksimali filmo trukmė: {max_length} min')

year_groups = df.groupby('Year').size()    # - filmų pasiskirstymas pagal metus
print(year_groups)


##### Grafikas Įvertinimo vidurkis pagal sertifikatą #####
# Susigrupuojame duomenis pagal sertifikatą ir įvertinimo vidutines reikšmes surikiuojame nuo didžiausios iki mažiausios
popular_cert = df.groupby('Certificate')['Rating'].mean().sort_values(ascending=False)

# Pasirenkame grafiko dydį
plt.figure(figsize=(12, 9))
# Savo sugrupuotus duomenis pasirenkame atvaizduoti bar tipo grafike, pasikeičiam linijų spalvas bei dydį
popular_cert.plot(kind='bar', color='khaki', edgecolor='grey', linewidth=2.5)
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.title('Filmo įvertinimas pagal sertifikata')
plt.xlabel('Sertifikatas')
plt.ylabel('Filmo įvertinimas')
plt.xticks(rotation=45)  # - Pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito
plt.show()              # - Rodome grafiką
########################################################


##### Grafikas Įvertinimo vidurkis pagal žanrą #####
# Susirašome visus galimus unikalius žanrus
unique_genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy',
                   'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport',
                   'Thriller', 'War', 'Western']
# Susikuriame naują sąrašą, kuriame rinksime informacija apie kiekvieno unikalaus žanro įvertinimų vidurkį
average_ratings = []
# Pasileidžiame for ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]   # - Surandame kurie filmai turi nurodytą žanrą
    average = film_genre['Rating'].mean()             # - Atliekame vidutinio įvertinimo skaičiavimą su mean() funkcija
    average_ratings.append((genre, average))         # - Žanro pavadinimą bei įvertinimo vidurkį įsirašome į sąrašą
# Surikiuojame pagal vidutinį įvertinimą
average_ratings.sort(key=lambda x: x[1], reverse=True)
# Sukuriame diagramą
fig, ax = plt.subplots()
# Pridedame stulpelius vienas po kito eidami per visas sąrašo reikšmes
for genre, average_rate in average_ratings:
    plt.bar(genre, average_rate)
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.xlabel('Žanras')
plt.ylabel('Įvertinimo Vidurkis')
plt.title('Įvertinimo vidurkis pagal žanrą')
plt.xticks(rotation=45, ha='right')    # - Pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito
plt.tight_layout()                    # - Sumažiname baltą plotą aplink grįfiką
plt.show()                           # - Rodome grafiką
##################################################


##### Grafikas Filmų skaičius pagal žanrą #####
# Susikuriame naują sąrašą, kuriame rinksime informaciją apie kiekvieno unikalaus žanro išleistų filmų skaičių
count_films = []
# Pasileidžiame for ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]   # - Surandame kurie filmai turi nurodytą žanrą
    count = film_genre['Title'].count()               # - Atliekame filmų apskaičiavima pagal žanrą su count() funkcija
    count_films.append((genre, count))               # - Žanro pavadinimą bei filmų kiekį tam žanrui įsirašome i sąrašą
# Surikiuojame pagal filmų skaičių
count_films.sort(key=lambda x: x[1], reverse=True)
# Sukuriame diagramą
fig, ax = plt.subplots()
# Pridedame stulpelius vienas po kito eidami per visas sąrašo reikšmes
for genre, average_len in count_films:
    plt.bar(genre, average_len)
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.xlabel('Žanras')
plt.ylabel('Filmų skaičius')
plt.title('Filmu skaičius pagal žanrą')
plt.xticks(rotation=45, ha='right')    # - Pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito
plt.tight_layout()                    # - Sumažiname baltą plotą aplink grįfiką
plt.show()                           # - Rodome grafiką
##################################################


##### Grafikas Vidutinė filmo trukmė pagal žanrą #####
# Susikuriame naują sąrašą, kuriame rinksime informaciją apie kiekvieno unikalaus žanro filmų trukmės vidurkį
average_lengths = []
# Pasileidžiame for ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]   # - Surandame kurie filmai turi nurodyta žanrą
    average_len = film_genre['Length'].mean()         # - Atliekame vidutinės trukmės skaičiavima su mean() funkcija
    average_lengths.append((genre, average_len))     # - Žanro pavadinimą bei filmų trukmės vidurkį įsirašome į sąrašą
# Surikiuojame pagal filmų trukmės vidurkius
average_lengths.sort(key=lambda x: x[1], reverse=True)
# Sukuriame diagramą
fig, ax = plt.subplots()
# Pridedame stulpelius vienas po kito eidami per visas sąrašo reikšmes
for genre, average_len in average_lengths:
    plt.bar(genre, average_len)
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.xlabel('Žanras')
plt.ylabel('Trukmės Vidurkis')
plt.title('Trukmės vidurkis pagal žanrą')
plt.xticks(rotation=45, ha='right')    # - Pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito
plt.tight_layout()                    # - Sumažiname baltą plotą aplink grįfiką
plt.show()                           # - Rodome grafiką
#######################################################


##### Taškinė diagrama su filmų įvertinimais ######
# Pasirenkame grafiko dydį
plt.figure(figsize=(10,6))
# Sukuriame taškinio išsibarstymo grafiką, nurodydami savo x, y ašis, taip pat taškų pasiskirstymą pagal įvertinimą
# Nusistatome savo spalvų paletę, taip pat pasirenkame jog taškų dydis priklauso nuo įvertinimo
sns.scatterplot(data=df,x='Year', y='Rating', hue='Rating', palette='icefire', size='Rating', sizes=(20,200))
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.title('Diagrama su filmu reitingais')
plt.xlabel('Metai')
plt.ylabel('Reitingas')
plt.tight_layout()           # - Sumažiname baltą plotą aplink grįfiką
plt.show()                  # - Rodome grafiką
####################################################


##### Išleistų filmų pagal metus histograma #####
# Sukuriame histogramą pasirinkdami metus kaip mūsų x ašies parametrą, stulpelių skaičių bei grafiko spalvą
sns.histplot(data=df, x="Year", bins=15, color='r')
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.title('Išleistų filmų skaičius per metus')
plt.xlabel('Metai')
plt.ylabel('Filmų skaičius')
plt.show()                 # - Rodome grafiką
#################################################


##### Grafikas Įvertinimo vidurkis kas 10 metų intervalus #####
# Susikuriame naują stulpelį mūsų naudojamame DataFrame, kuriame nurodome kad imsim metus nuo 1910 kas 10 metu iki 2020 metų
df['Year_Inteval'] = pd.cut(df['Year'], bins=range(1910, 2030, 10), right=False)
# Susigrupuojame duomenis pagal metų intervalus ir skaičiuojame įvertinimo vidurkius kiekvienam intervalui
# Duomenis taip pat yra surikiuojami nuo didžiausio įvertinimo vidurkio iki mažiausio
sorted_data = df.groupby('Year_Inteval', observed=True)['Rating'].mean().reset_index().sort_values('Rating', ascending=False)

# Pasirenkame grafiko dydį
plt.figure(figsize=(10,8))
# Sukuriame bar tipo grafiką naudodami mūsų prieš tai sutvarkytus duomenis, pasirenkame stulpelių spalvas
plt.bar(sorted_data['Year_Inteval'].astype(str), sorted_data['Rating'], color='royalblue', edgecolor='black')
# Pridedame ašies pavadinimus ir grafiko pavadinimą
plt.xlabel('10 metų intervalai')
plt.ylabel('Įvertinimo vidurkis')
plt.title('Įvertinimo vidurkis pagal 10 metų intervalus')
plt.xticks(rotation=45, ha='right')    # - Pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito
plt.show()                            # - Rodome grafiką
######################################################