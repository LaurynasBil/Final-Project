from bs4 import BeautifulSoup               # įsikeliame BeutifulSoup darbui su svetaine
import pandas as pd                         # įsikeliame pandas darbui su DataFrame
import requests                             # įsikeliame requests darbui su svetaine


# Apsirašome savo duomenų gavimą ir tvarkymą kaip funkciją 'scrape' pateikdami vieną kintamąjį svetainės url adresą
def scrape(url):
# Apsirašome headers, kad nekiltų problemų norint pasiekti svetainės duomenis
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }

    data = []      # Susikuriame savo data sąrašą, kuris bus naudojamas duomenų įrašymui į DataFrame
# Naudojame for ciklą, kad eitume per svetainės puslapius, šiuo atveju einame per puslapius nuo 1 iki 50
    for i in range(1, 51):
        new_url = f'{url}{i}'  # sukuriame naują url adresą su mūsų funkcijos nurodytu kintamuoju bei puslapio skaičiumi

        # Naudodami requests biblioteką gauname puslapio turinį
        response = requests.get(new_url, headers=headers)

        # Naudodami BeautifulSoup biblioteką išanalizuojame HTML turinį
        soup = BeautifulSoup(response.content, 'html.parser')

# Naudodami find_all funkciją surandame pavadinimo elementus, kurie atitinka nurodytą kriterijų ir klasės pavadinimą
        titles = soup.find_all('h3', class_='lister-item-header')
# Naudodami find_all funkciją surandame metų elementus, kurie atitinka nurodytą kriterijų ir klasės pavadinimą
        years = soup.find_all('span', class_='lister-item-year text-muted unbold')
# Naudodami find_all funkciją surandame sertifikatų elementus, kurie atitinka nurodytą kriterijų ir klasės pavadinimą
        certificates = soup.find_all('span', class_='certificate')
# Naudodami find_all funkciją surandame filmų trukmės elementus, kurie atitinka nurodytą kriteriju ir klasės pavadinimą
        runtimes = soup.find_all('span', class_='runtime')
# Naudodami find_all funkciją surandame žanrų elementus, kurie atitinka nurodytą kriteriju ir klasės pavadinimą
        genres = soup.find_all('span', class_='genre')
# Naudodami find_all funkciją surandame įvertinimų elementus, kurie atitinka nurodytą kriterijų ir klasės pavadinimą
        ratings = soup.find_all('div', class_='ipl-rating-star small')

        movies_list = []  # Susikuriame naują sąrašą skirta duomenims apie filmus saugoti
        # Einame per apjungto for ciklo visų atributų reikšmes po vieną ir susitvarkome duomenis įrašymui į sąrašą
        for title, year, certificate, runtime, genre, rating in zip(titles, years, certificates, runtimes, genres,
                                                                    ratings):
            # Surandame filmo pavadinimą pagal nuorodą, išrenkame tiktais tekstą ir panaikiname nepageidaujamus simbolius
            title_text = title.find('a').get_text().replace("'", "")
    # Gauname metų tekstinę reikšmę, pasinaikiname nepageidaujamus simbolius ir visa tai pasiverčiam į sveikajį skaičių
            year_value = int(year.get_text().replace(
                '(','').replace(')', '').replace('I ', '').replace('I', '').replace('V','').replace(
                ' ideo', '').replace(' T Movie', '').replace('X', ''))
            # Gauname sertifikato tekstinę reikšmę
            certificate_text = certificate.get_text()
            # Gauname filmo trukmės tekstinę reikšmę, pasinaikiname 'min' tekstą ir pasiverčiame į sveikajį skaičių
            run_value = int(runtime.get_text().replace(' min', ''))
            # Gauname žanro tekstinę reikšmę ir pasinaikiname papildomas tuščias eilutes
            genre_text = genre.get_text().replace('\n', '')
        # Gauname įvertinimo tekstinę reikšmę, pasinaikiname tuščias eilutes ir tarpus ir pasiverčiame į dešimtainį skaičiu
            rating_value = float(rating.get_text().replace('\n', '').replace(' ', ''))
            # Prieš tai gautas reikšmes sudedame į sąrašą
            movies_list.append({
                'Title': title_text,
                'Year': year_value,
                'Certificate': certificate_text,
                'Length': run_value,
                'Genre': genre_text,
                'Rating': rating_value,
            })
        # Naudojame for ciklą, kad vieno puslapio surinktus duomenis įrašytume į mūsų pagrindini data sąrašą
        for movie in movies_list:
            data.append(movie)

    # Naudodami Pandas biblioteką sukuriame naują DataFrame su mūsų nuskaitytais duomenimis
    df = pd.DataFrame(data)
    # Pašaliname dublikatus jeigu tokių yra
    df.drop_duplicates(['Title'])
    # Funkcija gražina jau sukurtą DataFrame
    return df

if __name__ == "__main__":
    # Šis kodas bus vydomas
    # jeigu kodas bus vykdomas kaip pagrindinė programa

    print('This is the main program!')