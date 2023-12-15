**Projekto Pavadinimas: Kino Filmų Reitingų Analizė**

**Projekto tikslas:** Surinkti duomenis apie kino filmus iš interneto svetainės www.imdb.com, juos išanalizuoti ir vizualizuoti. Išmokti dirbti su realiais duomenimis, taikyti duomenų valymo ir analizės metodus bei pateikti įžvalgas per įvairias vizualizacijas.

**Projekto vykdymo eiga:**
Atliekant projektą naudojomės interneto svetaine www.imdb.com, kuri yra laisvai prieinama ir kurios duomenimis gali naudotis vartotojai. Pasirinkome šiuos duomenis: pavadinimus, metus, serifikatus, filmo laiką, žanrus ir įvertinimus, išrinkome jų klases ir BeautifulSoup 4 (bs4) bibliotekos pagalba nuskaitėme duomenis iš svetainės. 
- Projekto pirmą failą pavadinome `scraping.py` ir jame vykdėme duomenų įkėlimą ir jų tvarkymą.
- Projekto pradžioje importavome reikalingas bibliotekas:
  ```
  from bs4 import BeautifulSoup
  import pandas
  import requests
  ```
- Po to nurodėme funkciją: `def scrape(url):`, kuri apima ir nuskaito visus duomenis iki funkcijos pabaigos:
- `df = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')`
- Ši funkcija apima visus joje esančius duomenis ir kitoje vietoje juos įkelia, kai tai nurodoma.
- Toliau šioje funkcijoje atlikome kitą funkciją naudojant `zip` metodą. Sukūrėme 'for'ą' išvardindami visų duomenų pavadinimus ir sukeldami juos į 'zip'ą', priskyrėme jiems išplėtimo reikšmes 'text' arba 'value'; komandos `int` ir `float` pagalba nurodėme, kurie duomenys yra skaičiai, komandos `replace` pagalba pakeitėme netinkamas reikšmes į tinkamas arba į tuščias vietas. Komandos `movies_list.append()` pagalba duomenis ikėlėme.
- Komanda `for movie in movies_list: data.append(movie)` - nuskaito duomenis po vieną filmų sąrašą, t.y. pirmiausia nuskaito pirmo puslapio duomenis, po to antro bei sukelia juos sąrašo apačioje, po to trečio ir t.t.
- Surinktus ir sutvarkytus duomenis sukėlėme į Pandas DataFrame: `df = pd.DataFrame(data)`.
- Nurodėme, kad panaikintų pasikartojančius filmus: `df.drop_duplicates(['Title'])`.
- Komanda `if __name__ == "__main__":` nurodo, kad šis kodas bus vykdomas tik jei tekstas paleistas kaip pagrindinė (main) programa.
- Sukūrėme antrą projekto failą, kurį pavadinome `main.py`. Pradžioje vėl importavome reikalingas bibliotekas:
  ```
  import pandas as pd
  from scraping import scrape
  from writesql import duomenu_irasymas_sql
  import matplotlib.pyplot as plt
  import seaborn as sns
  ```
- Vykdome duomenų nuskaitymą ir įrašymą per mūsų sukurtą `scrape` funkciją, kuri grąžina DataFrame:
  ```
  df1 = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')
  df2 = scrape('https://www.imdb.com/list/ls063676660/?st_dt=&mode=detail&page=')
  result = pd.concat([df1, df2])
  ```
- Duomenis įrašome i csv failą, kad nereikėtų kiekvieną karta laukti kol surinks duomenis iš svetainės:
- `result.to_csv("result.csv", index = False)`
- `df = pd.read_csv('result.csv')`
- Savo duomenis įrašome į SQl lentelę naudodami sukurtą funkciją 'scraping.py' faile:
- `duomenu_irasymas_sql(df)`.
- 
- Atliekame duomenų analizę.
- Randam įvertinimų vidurkį, minimalią ir maximalią įvertinimų reikšmes:
  ```
  avg_rating = df['Rating'].mean()     
  print(f'Vidutinis filmu įvertinimas yra: {avg_rating:.2f}')'.
  min_rating = df['Rating'].min()
  print(f'Minimalus filmų įvertinimas: {min_rating}')
  max_rating = df['Rating'].max()
  print(f'Maksimalus filmų įvertinimas: {max_rating}')
  ```
- Gauname rezultatą:
  ```
  Vidutinis filmų įvertinimas yra: 6.56
  Minimalus filmų įvertinimas: 1.2
  Maksimalus filmų įvertinimas: 9.3
  ```
- Taip pat randam filmų laiko vidurkį, minimalią ir maximalią filmų laiko reikšmes:
  ```
  Vidutinė filmų trukmė yra: 108.18 min
  Minimali filmo trukmė: 43 min
  Maksimali filmo trukmė: 439 min
  ```
- Apskaičiuojame filmų skaičiaus pasiskirstymą pagal metus:
- `year_groups = df.groupby('Year').size()`
- `print(year_groups)`
- Apskaičiuojame, kiek filmų buvo išleista XX amžiuje ir kiek XXI amžiuje iki 2017 metų, t.y. iki nagrinėjamo laikotarpio pabaigos.
  ```
  rows_with_year_bellow_2000 = df.loc[df['Year'] < 2000]   # - vykdo salyga iki 2000
  rows_with_year_bellow_2000_count = rows_with_year_bellow_2000['Title'].count()   # - suskaičiuoja reikšmes
  print(f'Filmų skaičius išleistų prieš 2000 metus: {rows_with_year_bellow_2000_count}')
  rows_with_year_above_2000 = df.loc[df['Year'] >= 2000]   # - vykdo salyga 2000 ir daugiau
  rows_with_year_above_2000_count = rows_with_year_above_2000['Title'].count()   # - suskaičiuoja reikšmes
  print(f'Filmų skaičius išleistų 2000 metais ir po jų: {rows_with_year_above_2000_count}')
  ```
- Gauname rezultatus:
  ```
  Filmų skaičius išleistų prieš 2000 metus: 4155
  Filmų skaičius išleistų 2000 metais ir po jų: 5500
  ```
- Atliekame duomenų vizualizaciją Matplotlib ir Seaborn bibliotekų pagalba.
- Sukuriame grafiką `Įvertinimų vidurkis pagal sertifikatą`:
- Susigrupuojame duomenis pagal sertifikatą ir įvertinimo vidutines reikšmes surikiuojame nuo didžiausios iki mažiausios.
- `popular_cert = df.groupby('Certificate')['Rating'].mean().sort_values(ascending=True)`
- Nurodome grafiko dydį: `plt.figure(figsize=(10,9))`.
- Nurodome grafiko rūšį: `popular_cert.plot(kind='bar')`.
- Nurodome grafiko pavadinimą, grafiko x bei y ašių pavadinimus ir grafiko x ašies pasvirimo kampo dydį, t.y. pasukame x ašį 45 kampu, kad tekstas nekristų vienas ant kito, rodome grafiką.
 ![fig1](https://github.com/LaurynasBil/Final-Project/blob/main/fig1.png) 
- Sukuriame grafiką `Įvertinimo vidurkis pagal žanrą`:
- Susirašome visus galimus unikalius žanrus, susikuriame naują sąrašą, kuriame rinksime informaciją apie kiekvieno unikalaus žanro įvertinimų vidurkį.
- Pasileidžiame `for` ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus, surandame, kurie filmai turi nurodytą žanrą, atliekame vidutinio įvertinimo skaičiavimą su 'mean()' funkcija, žanro pavadinimą bei įvertinimo vidurkį įsirašome i sąrašą. Surikiuojame pagal vidutinį įvertinimą.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig2](https://github.com/LaurynasBil/Final-Project/blob/main/fig2.png) 
- Sukuriame grafiką `Filmų skaičius pagal žanrą`:
- Susikuriame naują sąrašą, kuriame rinksime informaciją apie kiekvieno unikalaus žanro išleistų filmų skaičių.
- Pasileidžiame `for` ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus, surandame kurie filmai turi nurodyta žanrą, atliekame filmų apskaičiavimą pagal žanrą su 'count()' funkcija, žanro pavadinimą bei filmų kiekį tam žanrui - įsirašome į sąrašą. Surikiuojame pagal filmų skaičių.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig3](https://github.com/LaurynasBil/Final-Project/blob/main/fig3.png)
- Sukuriame grafiką `Vidutinė filmo trukmė pagal žanrą`.
- Susikuriame naują sąrašą, kuriame rinksime informaciją apie kiekvieno unikalaus žanro filmų trukmės vidurkį.
- Pasileidžiame 'for' ciklą, kad eitume per visus unikalius žanrus po vieną ir kiekvienam jam atliktume skaičiavimus, surandame kurie filmai turi nurodytą žanrą, atliekame vidutinės trukmės skaičiavimą su 'mean()' funkcija, žanro pavadinimą bei filmų trukmės vidurkį įsirašome į sąrašą. Surikiuojame pagal filmų trukmės vidurkius.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig4](https://github.com/LaurynasBil/Final-Project/blob/main/fig4.png)
- Sukuriame grafiką `Taškinė diagrama su filmu įvertinimais`.
- Pasirenkame grafiko dydį, sukuriame taškinio išsibarstymo grafiką, nurodydami savo x, y ašis, taip pat taškų pisiskirstyma pagal įvertinimą, nusistatome savo spalvų paletę, taip pat pasirenkame jog taškų dydis priklauso nuo įvertinimo.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig5](https://github.com/LaurynasBil/Final-Project/blob/main/fig5.png)
- Sukuriame grafiką `Išleistų filmų pagal metus histograma`.
- Sukuriame histogramą pasirinkdami metus kaip mūsų x ašies parametrą, stulpelių skaičių bei grafiko spalvą.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig6](https://github.com/LaurynasBil/Final-Project/blob/main/fig6.png)
- Sukuriame grafiką `Įvertinimo vidurkis kas 10 metų intervalus`.
- Susikuriame naują stulpelį mūsų naudojamame DataFrame, kuriame nurodome, kad imsim metus nuo 1910 kas 10 metu iki 2020 metų.
-  Susigrupuojame duomenis pagal metų intervalus ir skaičiuojame įvertinimo vidurkius kiekvienam intervalui, duomenis taip pat yra surikiuojami nuo didžiausio įvertinimo vidurkio iki mažiausio. Sukuriame 'bar' tipo grafiką naudodami mūsų prieš tai sutvarkytus duomenis, pasirenkame stulpelių spalvas.
- Atliekame kitas reikiamas komandas grafiko sutvarkymui ir rodome grafiką.
 ![fig7](https://github.com/LaurynasBil/Final-Project/blob/main/fig7.png)

**Išvados:**
1. Išanalizavus sukeltus duomenis ir atlikus duomenų analizę nustatėme, kad: 
  Vidutinis filmų įvertinimas yra: 6.56
  Minimalus filmo įvertinimas: 1.2
  Maksimalus filmo įvertinimas: 9.3
  Vidutinė filmų trukmė yra: 108.18 min
  Minimali filmo trukmė: 43 min
  Maksimali filmo trukmė: 739 min
  Apskaičiuojame filmų skaičiaus pasiskirstymą pagal metus.
  Apskaičiuojame, kiek filmų buvo išleista XX amžiuje ir kiek XXI amžiuje iki 2017 metų, t.y. iki nagrinėjamo laikotarpio pabaigos.
3. Atliekant duomenų vizualizaciją sukurėme grafiką `Įvertinimų vidurkis pagal sertifikatą`, jame susigrupavome duomenis pagal sertifikatą ir įvertinimo vidutines reikšmes surikiavome nuo didžiausios iki mažiausios. Iš grafiko matyti, kad didžiausias filmų įvertinimas yra grupėje 18+, toliau seka 13+, M/PG ir t.t., mažiausi įvertinami grupėje TV-Y7-FV, TV-Y7, AO ir t.t.
4. Sukurus grafiką `Įvertinimų vidurkis pagal žanrą` matyti, kad geriausias įvertinimų vidurkis yra nespalvotų, karo, biografinių, vesternų, istorinių filmų, mažiausias siaubo, mokslinės fantastikos, šeimos, fantastikos, veiksmo ir t.t.
5. Sukurus grafiką `Filmų skaičius pagal žanrą` matyti, kad daugiausiai yra filmų, kurių žanrai yra drama, komedija, veiksmas, detektyvai, romantiniai ir t.t., mažiausiai yra siaubo filmų, vesternų, muzikinių, sporto, karinių ir t.t.
6. Sukurus grafiką 'Vidutinė filmo trukmė pagal žanrą` matyti, kad ilgiausi filmai yra istoriniai, muzikiniai, kariniai, biografiniai, vesterno ir t.t, trumpiausi yra animaciniai, siaubo, nespalvoti, komedijų, šeimos ir .t.t
7. Sukurus grafiką 'Taškinė diagrama su filmu įvertinimais` matyti, kad senesnių filmų įvertinimai daugiausiai buvo aukšti. Kuo vėlesniais metais daugiau buvo išleidžiama filmų, tuo jų pasiskirstymas įvertinimo skalėje darėsi įvairesnis, daugėjo blogiau vertinamų filmų. Grafiko legendoje pateikta informacija, kokios spalvos ir kokio dydžio rutuliukai ką nurodo. Kuo didesni rutuliukai, tuo didesni įvertinimai, spalvos parodo vertinimo skalę.
8. Sukurus grafiką 'Išleistų filmų pagal metus histograma` matyti, kad mažiausiai buvo išleista filmų XX amžiaus pradžioje, jų nelabai daug daugiau daugėjo iki maždaug 1970 metų ir labai žymiai daugiau išleisdavo maždaug nuo 1990 metų. Daugiausiai išleido apie 2010 metai, po to truputį sumažėjo.
9. Sukurus grafiką 'Įvertinimo vidurkis kas 10 metų intervalus` matyti, kad aukščiausias įvertinamo vidurkis yra tų filmų, kurie buvo išleisti 1920-1930 metais, po to įvertinimo vidurkis mažėja ir pats mažiausias 2010-2020 metais išleistų filmų vidurkis. Taip yra todėl, kad seniausiai išleistų filmų buvo nedaug ir jų vertinimai nedaug skiriasi, o vėlesniais laikotarpiais daugėjant išleidžiamų filmų skaičiui tarp gerų filmų yra daug blogos kokybės filmų ir bendras įvertinimo vidurkis yra žemesnis.
