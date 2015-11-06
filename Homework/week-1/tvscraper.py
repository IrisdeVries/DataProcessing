#!/usr/bin/env python
# Name: Iris de Vries
# Student number: 10367675
'''
This script scrapes IMDB and outputs a CSV file with highest ranking tv series.
'''
# IF YOU WANT TO TEST YOUR ATTEMPT, RUN THE test-tvscraper.py SCRIPT.
import csv

from pattern.web import URL, DOM

TARGET_URL = "http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating,desc&start=1&title_type=tv_series"
BACKUP_HTML = 'tvseries.html'
OUTPUT_CSV = 'tvseries.csv'


def extract_tvseries(dom):
    '''
    Extract a list of highest ranking TV series from DOM (of IMDB page).

    Each TV series entry should contain the following fields:
    - TV Title
    - Ranking
    - Genres (comma separated if more than one)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    '''
    series = []
    # extract data from IMDB
    for movie in dom.by_tag('td.title'): 
        Title = movie.by_tag('a')[0].content.encode('ascii', 'ignore')
        Ranking = movie.by_tag('span.value')[0].content.encode('ascii', 'ignore')
        Genre = movie.by_tag('span.genre')[0].by_tag('a')
        Genre = [g.content.encode('ascii', 'ignore') for g in Genre]
        Actors = movie.by_tag('span.credit')[0].by_tag('a')
        Actors = [a.content.encode('ascii', 'ignore') for a in Actors]
        Runtime = movie.by_tag('span.runtime')[0].content.split(' ')[0]

        # put data into a row each loop and add to the list "series" 
        row = [Title, Ranking, Genre, Actors, Runtime]
        series.append(row)
        # return the list "series" with all of the data
    return series

def save_csv(f, tvseries):
    '''
    Output a CSV file containing highest ranking TV-series.
    '''
    writer = csv.writer(f)
    writer.writerow(['Title', 'Ranking', 'Genre', 'Actors', 'Runtime'])
    for series in tvseries:
        writer.writerow(series)
        
if __name__ == '__main__':
    # Download the HTML file
    url = URL(TARGET_URL)
    html = url.download()

    # Save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in testing / grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # Parse the HTML file into a DOM representation
    dom = DOM(html)

    # Extract the tv series (using the function you implemented)
    tvseries = extract_tvseries(dom)

    # Write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'wb') as output_file:
        save_csv(output_file, tvseries)
