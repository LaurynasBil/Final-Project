import pandas as pd
from scraping import scrape

# df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
# df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
# result = pd.concat([df1, df2])
# result.to_csv("result.csv", index = False)
df = pd.read_csv('result.csv')


avg_rating = df['Rating'].mean()                                # - reitingu vidurkis
# print(f'Vidutinis filmu reitingas yra: {avg_rating:.2f}')
