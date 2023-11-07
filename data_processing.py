import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def importDataFromFile():
    df = pd.read_csv('goodreads_library_export.csv')
    df[['ISBN', 'ISBN13']] = df[['ISBN', 'ISBN13']].applymap(lambda x: re.sub(r'\D', '', str(x)))
    df['Author'] = df['Author'].str.split().str.join(' ')
    df[['Date Read', 'Date Added']] = df[['Date Read', 'Date Added']].apply(lambda x: pd.to_datetime(x, format='%Y/%m/%d'))
    get_genres(df)
    save_to_file(df)

def get_genre_for_book(book_url):
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    book_genres = [a.text for a in soup.select('a[href*="/genres/"]')]
    print('Im in get_genre_for_books', book_url)
    return ', '.join(book_genres)

def get_genres(df):
    book_ids = df['Book Id'].tolist()
    book_urls = [f'https://www.goodreads.com/book/show/{book_id}' for book_id in book_ids]

    with ThreadPoolExecutor(max_workers=8) as executor:  # Anpassa max_workers efter dina behov
        genres = list(executor.map(get_genre_for_book, book_urls))

    df['Genres'] = genres

def save_to_file(df):
    df.to_csv('goodreads_export_with_genres.csv', index=False)

