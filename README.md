Projekto Pavadinimas: Kino Filmų Reitingų Analizė

Atliekant projektą naudojomės interneto svetaine www.imdb.com, kuri yra laisvai prieinama ir kuriais gali naudotis vartotojai. Pasirinkome pavadinimus, metus, serifikatus, filmo 
laiką, žanrus ir įvertinimus, išrinkome jų klases ir BeautifulSoup 4 (bs4) bibliotekos pagalba nuskaitėme duomenis iš svetainės. 
- Projekto pradžioje nurodėme funkciją: def scrape(url): , kuri apima visus duomenis iki funkcijos pabaigos:
- df = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=').
- Ši funkcija apima visus joje esančius duomenis ir kitoje vietoje juos įkelia, kai tai nurodoma.
- Toliau šioje funkcijoje atlikome kitą funkciją naudojant zip metodą. Joje komandos 'int' pagalba nurodėme, kurie duomenys yra skaičiai, komandos 'replace' pagalba pakeitėme netinkamas reikšmes į tinkamas arba į tuščias vietas.
- for movie in movies_list:
- data.append(movie)   - ši komanda nuskaito duomenis po vieną filmų sąrašą, t.y. pirmiausia nuskaito pirmo puslapio duomenis, po to antro ir sukelia juos sąrašo apačioje ir t.t.
- Surinktus ir sutvarkytus duomenis sukelėme į Pandas DataFrame:  df = pd.DataFrame(data). 


