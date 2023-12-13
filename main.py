import pandas as pd
from scraping import scrape
from writesql import duomenu_irasymas_sql

# df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
# df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
# result = pd.concat([df1, df2])
# Duomenis įrašome i csv failą kad butu galima lengviau su jais dirbti
# ir nereikėtu scrapinti kiekviena karta kazka pakeitus
# result.to_csv("result.csv", index = False)
df = pd.read_csv('result.csv')
# Savo duomenis irasome i SQl lentele naudodami sukurta funkcija kitame faile
duomenu_irasymas_sql(df)

avg_rating = df['Rating'].mean()      # - reitingu vidurkis
print(f'Vidutinis filmu reitingas yra: {avg_rating:.2f}')

min_rating = df['Rating'].min()   # - randam minimalia ir maximalia reiksme
print(f'Minimalus filmu reitingas: {min_rating}')
max_rating = df['Rating'].max()
print(f'Maksimalus filmu reitingas: {max_rating}')

avg_length = df['Length'].mean()    # - filmu laiko vidurkis
print(f'Vidutinis filmu laikas yra: {avg_length:.2f} min')

min_length = df['Length'].min()   # - randam minimalia ir maximalia reiksme
print(f'Minimalus filmo laikas: {min_length} min')
max_length = df['Length'].max()
print(f'Maksimalus filmo laikas: {max_length} min')


##### Grafikas Reitingo vidurkis pagal sertifikatą #####
popular_cert = df.groupby('Certificate')['Rating'].mean().sort_values(ascending=True)
print(popular_cert)

plt.figure(figsize=(10,9))
popular_cert.plot(kind='bar')
plt.title('Filmo reitingas pagal sertifikata')
plt.xlabel('Sertifikatas')
plt.ylabel('Filmo reitingas')
plt.xticks(rotation=45)
plt.show()
########################################################