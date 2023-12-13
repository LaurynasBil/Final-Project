import pandas as pd
from scraping import scrape

# df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
# df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
# result = pd.concat([df1, df2])
# result.to_csv("result.csv", index = False)
df = pd.read_csv('result.csv')


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
