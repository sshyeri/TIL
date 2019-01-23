import csv
import requests
import json
import os

def result_save(result):
    with open('movie_naver.csv', 'w', newline='', encoding='UTF-8') as f:
        fieldnames = ('Movie_code', 'Movie_img', 'Movie_link', 'Movie_rating')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for key,value in result.items():
            writer.writerow({'Movie_code': key, 'Movie_img': value["img"], 'Movie_link': value["link"], 'Movie_rating': value["rating"]})
            
def movie_rating(res, result):
    rating = {}
    item = 'item'
    if res.get('items'):
        item = 'items'
    rating["img"] = res[item][0]["image"]
    rating["link"] = res[item][0]["link"]
    rating["rating"] = res[item][0]["userRating"]
    return rating      


movieNms = []
with open('movie.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movieNms += [(row['Movie_name'], row['Movie_code'])]

NID = os.getenv("ID")
NSC = os.getenv("SECRET")
KEY_DICT = { "X-Naver-Client-Id": NID,
            "X-Naver-Client-Secret": NSC}
result = {}

for movieNm in movieNms:
    url = f'https://openapi.naver.com/v1/search/movie?query={movieNm[0]}'
    res = requests.get(url, headers=KEY_DICT).json()
    result[movieNm[1]] = movie_rating(res, result)
result_save(result)



