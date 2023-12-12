from bs4 import BeautifulSoup
import pandas as pd
import requests

def scrape(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }

    data = []
    for i in range(1, 51):
        new_url = f'{url}{i}'

        response = requests.get(new_url, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h3', class_='lister-item-header')
        years = soup.find_all('span', class_='lister-item-year text-muted unbold')
        certificates = soup.find_all('span', class_='certificate')
        runtimes = soup.find_all('span', class_='runtime')
        genres = soup.find_all('span', class_='genre')
        ratings = soup.find_all('div', class_='ipl-rating-star small')

        movies_list = []
        for title, year, certificate, runtime, genre, rating in zip(titles, years, certificates, runtimes, genres, ratings):
            title_text = title.find('a').get_text().replace("'", "")
            year_value = int(year.get_text().replace('(', '').replace(')', '').replace('I ', '').replace('I', '').replace('V','').replace(' ideo', '').replace(' T Movie', '').replace('X', ''))
            certificate_text = certificate.get_text()
            run_value = int(runtime.get_text().replace(' min', ''))
            genre_text = genre.get_text().replace('\n', '')
            rating_value = float(rating.get_text().replace('\n', '').replace(' ', ''))
            movies_list.append({
                'Title': title_text,
                'Year': year_value,
                'Certificate': certificate_text,
                'Length': run_value,
                'Genre': genre_text,
                'Rating': rating_value,
            })
        for movie in movies_list:
            data.append(movie)

    df = pd.DataFrame(data)
    df.drop_duplicates(['Title'])
    return df

if __name__ == "__main__":
    # This code will only be executed
    # if the script is run as the main program

    df = scrape('https://www.imdb.com/list/ls063676189/?st_dt=&mode=detail&page=')