Projekto Pavadinimas: Kino Filmų Reitingų Analizė

Atliekant projektą naudojomės interneto svetaine www.imdb.com, kuri yra laisvai prieinama ir kurios duomenimis gali naudotis vartotojai. Pasirinkome šiuos duomenis: pavadinimus, metus, serifikatus, filmo laiką, žanrus ir įvertinimus, išrinkome jų klases ir BeautifulSoup 4 (bs4) bibliotekos pagalba nuskaitėme duomenis iš svetainės. 
- Projekto pirmą failą pavadinome 'scraping.py' ir jame vykdėme duomenų įkėlimą ir jų tvarkymą.
- Projekto pradžioje importavome reikalingas bibliotekas:
- 'from bs4 import BeautifulSoup
- import pandas as pd
- import requests'.
- Po to nurodėme funkciją: 'def scrape(url):', kuri apima visus duomenis iki funkcijos pabaigos:
- 'df = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')'.
- Ši funkcija apima visus joje esančius duomenis ir kitoje vietoje juos įkelia, kai tai nurodoma.
- Toliau šioje funkcijoje atlikome kitą funkciją naudojant zip metodą. Joje komandos 'int' pagalba nurodėme, kurie duomenys yra skaičiai, komandos 'replace' pagalba pakeitėme netinkamas reikšmes į tinkamas arba į tuščias vietas.
- 'for movie in movies_list:
- data.append(movie)'   - ši komanda nuskaito duomenis po vieną filmų sąrašą, t.y. pirmiausia nuskaito pirmo puslapio duomenis, po to antro bei sukelia juos sąrašo apačioje ir t.t.
- Surinktus ir sutvarkytus duomenis sukelėme į Pandas DataFrame: 'df = pd.DataFrame(data)'.
- Nurodėme, kad panaikintų pasikartojančius filmus: 'df.drop_duplicates(['Title'])' ir kartotų df: 'return df'.
- Komanda 'if __name__ == "__main__":' nurodo, kad šis kodas bus vykdomas tik jei tekstas paleistas kaip pagrindinė (main) programa.
- Sukūrėme antrą projekto failą, kurį pavadinome 'main.py'. Pradžioje vėl importavome reikalingas bibliotekas:
- 'import pandas as pd
- from scraping import scrape
- from writesql import duomenu_irasymas_sql
- import matplotlib.pyplot as plt
- import seaborn as sns'.
- Nurodėme komandą, kad sukeliame duomenis iš faile 'scrapint.py' įkeltų duomenų. Šis veiksmas atliekamas tam, kad nereikėtų kiekvieną kartą kreiptis į interneto svetainę ir tam skirti labai daug laiko:
'df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
result = pd.concat([df1, df2])'.
- Duomenis įrašome i csv failą, kad būtų galima lengviau su jais dirbti ir nereikėtu kreiptis į 'scraping.py' failą kiekvieną kartą kažką pakeitus:
- 'result.to_csv("result.csv", index = False)
- df = pd.read_csv('result.csv')'.
- Savo duomenis irašome į SQl lentelę naudodami sukurtą funkciją kitame 'scraping.py' faile:
- 'duomenu_irasymas_sql(df)'.



