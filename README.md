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
- Toliau šioje funkcijoje atlikome kitą funkciją naudojant zip metodą. Sukūrėme for'ą išvardindami visų duomenų pavadinimus ir sukeldami juos į zip'ą, priskyrėme jiems išplėtimo reikšmes 'text' arba 'value', komandos 'int' pagalba nurodėme, kurie duomenys yra skaičiai, komandos 'replace' pagalba pakeitėme netinkamas reikšmes į tinkamas arba į tuščias vietas. Komandos 'movies_list.append({' pagalba duomenis ikėlėme.
- Komanda 'for movie in movies_list:
-              data.append(movie)'   - nuskaito duomenis po vieną filmų sąrašą, t.y. pirmiausia nuskaito pirmo puslapio duomenis, po to antro bei sukelia juos sąrašo apačioje, po to trečio ir t.t.
- Surinktus ir sutvarkytus duomenis sukelėme į Pandas DataFrame: 'df = pd.DataFrame(data)'.
- Nurodėme, kad panaikintų pasikartojančius filmus: 'df.drop_duplicates(['Title'])'.
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
- Atliekame duomenų analizę. Randam įvertinimų vidurkį:
- 'avg_rating = df['Rating'].mean()     
- print(f'Vidutinis filmu reitingas yra: {avg_rating:.2f}')'.
- Randam minimalią ir maximalią įvertinimų reikšmes:
- 'min_rating = df['Rating'].min()
- print(f'Minimalus filmu reitingas: {min_rating}')
- max_rating = df['Rating'].max()
- print(f'Maksimalus filmu reitingas: {max_rating}')'.
- Taip pat randam filmų laiko vidurkį, minimalią ir maximalią filmų laiko reikšmes:
- 'avg_length = df['Length'].mean()
- print(f'Vidutinis filmu laikas yra: {avg_length:.2f} min')
- min_length = df['Length'].min()
- print(f'Minimalus filmo laikas: {min_length} min')
- max_length = df['Length'].max()
- print(f'Maksimalus filmo laikas: {max_length} min')'.
- Apskaičiuojame filmų skaičiaus pasiskirstymą pagal metus:
- 'year_groups = df.groupby('Year').size()
-  print(year_groups)'.
- Atliekame duomenų vizualizaciją Matplotlib ir Seaborn bibliotekų pagalba. Sukuriame grafiką 'Įvertinimų vidurkis pagal sertifikatą'.
- Parašome naują sutrumpintą pavadinimą 'popular_cert', kurį naudosime šiame kode, ir nurodome jam komandas:
- 'popular_cert = df.groupby('Certificate')['Rating'].mean().sort_values(ascending=True)
- print(popular_cert)'.
- 'df' - tai DataFrame veiksmas, 'groupby' - grupuojame nurodytus duomenis, 'mean()' - randame vidurkį, 'sort_values' - rušiuojame reikšmes, 'ascending=True' - duomenys bus rodomi didėjimo tvarka.
- Nurodome grafiko dydį: 'plt.figure(figsize=(10,9))'.
- Nurodome grafiko pavadinimą: 'plt.title('Filmo reitingas pagal sertifikata')'.
- Nurodome grafiko x ir y ašių pavadinimus:
- 'plt.xlabel('Sertifikatas')
-  plt.ylabel('Filmo reitingas')'.



