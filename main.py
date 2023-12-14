import pandas as pd
from scraping import scrape
from writesql import duomenu_irasymas_sql
import matplotlib.pyplot as plt
import seaborn as sns

# df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
# df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
# result = pd.concat([df1, df2])
# Duomenis įrašome i csv failą kad butu galima lengviau su jais dirbti
# ir nereikėtu scrapinti kiekviena karta kazka pakeitus
# result.to_csv("result.csv", index = False)
df = pd.read_csv('result.csv')
# Savo duomenis irasome i SQl lentele naudodami sukurta funkcija kitame faile
# duomenu_irasymas_sql(df)

##### Duomenu Analizė #####
avg_rating = df['Rating'].mean()      # - reitingu vidurkis
print(f'Vidutinis filmu įvertinimas yra: {avg_rating:.2f}')
min_rating = df['Rating'].min()   # - randam minimalia ir maximalia reiksme
print(f'Minimalus filmu įvertinimas: {min_rating}')
max_rating = df['Rating'].max()
print(f'Maksimalus filmu įvertinimas: {max_rating}')

avg_length = df['Length'].mean()    # - filmu laiko vidurkis
print(f'Vidutinė filmų trukmė yra: {avg_length:.2f} min')
min_length = df['Length'].min()   # - randam minimalia ir maximalia reiksme
print(f'Minimali filmo trukmė: {min_length} min')
max_length = df['Length'].max()
print(f'Maksimali filmo trukmė: {max_length} min')

year_groups = df.groupby('Year').size()    # - filmu pasiskirstymas pagal metus
# print(year_groups)


##### Grafikas Reitingo vidurkis pagal sertifikatą #####
popular_cert = df.groupby('Certificate')['Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 9))
popular_cert.plot(kind='bar', color='khaki', edgecolor='grey', linewidth=2.5)
plt.title('Filmo reitingas pagal sertifikata')
plt.xlabel('Sertifikatas')
plt.ylabel('Filmo reitingas')
plt.xticks(rotation=45, ha='right')
plt.show()
########################################################


##### Grafikas Reitingo vidurkis pagal žanrą #####
# Susirašome visus galimus žanrus
unique_genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy',
                   'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport',
                   'Thriller', 'War', 'Western']
# Sukurkime grafiką su stulpeliais kiekvienam žanrui
average_ratings = []
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]
    average = film_genre['Rating'].mean()
    average_ratings.append((genre, average))
# Surikiuojame pagal vidutinį įvertinimą
average_ratings.sort(key=lambda x: x[1], reverse=True)
# Sukuriame diagramą
fig, ax = plt.subplots()
# Pridedame stulpelius vienas po kito
for genre, average_len in average_ratings:
    plt.bar(genre, average_len)
# Pridedame ašies pavadinimus ir kitus grafiko elementus
plt.xlabel('Žanras')
plt.ylabel('Įvertinimo Vidurkis')
plt.title('Įvertinimo vidurkis pagal žanrą')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
##################################################


##### Grafikas Filmų skaičius pagal žanrą #####
# Sukurkime grafiką su stulpeliais kiekvienam žanrui
count_films = []
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]
    count = film_genre['Title'].count()
    count_films.append((genre, count))
    # Surikiuojame pagal vidutinį įvertinimą
count_films.sort(key=lambda x: x[1], reverse=True)
    # Sukuriame diagramą
fig, ax = plt.subplots()
    # Pridedame stulpelius vienas po kito
for genre, average_len in count_films:
    plt.bar(genre, average_len)
# Pridedame ašies pavadinimus ir kitus grafiko pavadinimą
plt.xlabel('Žanras')
plt.ylabel('Filmų skaičius')
plt.title('Filmu skaičius pagal žanrą')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
##################################################


##### Grafikas Vidutinė filmo trukme pagal žanrą #####
average_lengths = []
for genre in unique_genres:
    film_genre = df[df['Genre'].str.contains(genre)]
    average_len = film_genre['Length'].mean()
    average_lengths.append((genre, average_len))
#
average_lengths.sort(key=lambda x: x[1], reverse=True)
# Sukuriame diagramą
fig, ax = plt.subplots()
# Pridedame stulpelius vienas po kito
for genre, average_len in average_lengths:
    plt.bar(genre, average_len)
# Pridedame ašies pavadinimus ir kitus grafiko pavadinimą
plt.xlabel('Žanras')
plt.ylabel('Trukmės Vidurkis')
plt.title('Trukmės vidurkis pagal žanrą')
# x - ašies reikšmes pasukame 45 kampu kad tilptu viskas ir grafika laikome arčiau dešnės pusės
plt.xticks(rotation=45, ha='right')
# Pasirenkame kad butu maziau baltos erdves aplink grafiką
plt.tight_layout()
plt.show() # Rodome grafiką
#######################################################


##### Diagrama su filmu reitingais ######
plt.figure(figsize=(10,6))
sns.scatterplot(data=df,x='Year', y='Rating', hue='Rating', palette='icefire', size='Rating', sizes=(20,200))
plt.title('Diagrama su filmu reitingais')
plt.xlabel('Metai')
plt.ylabel('Reitingas')
plt.tight_layout()
plt.show()
##########################################


##### Išleistų filmų pagal metus histograma #####
sns.histplot(data=df, x="Year", bins=15, color='r')
plt.title('Išleistų filmų skaičius per metus')
plt.xlabel('Metai')
plt.ylabel('Filmų skaičius')
plt.show()
#################################################


##### Įvertinimo vidurkis kas 10 metų intervalus #####
df['Year_Inteval'] = pd.cut(df['Year'], bins=range(1910, 2030, 10), right=False)
sorted_data = df.groupby('Year_Inteval', observed=True)['Rating'].mean().reset_index().sort_values('Rating', ascending=False)

plt.figure(figsize=(10,8))
plt.bar(sorted_data['Year_Inteval'].astype(str), sorted_data['Rating'], color='royalblue', edgecolor='black')
plt.xlabel('10 metų intervalai')
plt.ylabel('Įvertinimo vidurkis')
plt.title('Įvertinimo vidurkis pagal 10 metų intervalus')
plt.xticks(rotation=45, ha='right')
plt.show()
######################################################