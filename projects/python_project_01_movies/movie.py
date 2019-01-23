import csv
import requests
import json
import os

def result_save(result):
    with open('movie.csv', 'w', newline='', encoding='UTF-8') as f:
        fieldnames = ('Movie_code', 'Movie_name', 'Movie_name_En', 'Movie_name_Og', 'Open_date', 'Show_time', 'Genres', 'Directors', 'Watch_grade', 'Actor1', 'Actor2', 'Actor3' )
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for key,value in result.items():
            writer.writerow({'Movie_code': key, 'Movie_name': value["Movie_name"], 'Movie_name_En': value["Movie_name_En"], 
                            'Movie_name_Og': value["Movie_name_Og"], 'Open_date': value["Open_date"], 'Show_time': value["Show_time"], 
                            'Genres': value["Genres"], 'Directors': value["Directors"], 'Watch_grade': value["Watch_grade"], 
                            'Actor1': value["Actors"][0], 'Actor2': value["Actors"][1], 'Actor3': value["Actors"][2]})
            
def movie_info(res, result):
    info = {}
    info["Movie_name"] = res["movieInfoResult"]["movieInfo"]["movieNm"]
    info["Movie_name_En"] = res["movieInfoResult"]["movieInfo"]["movieNmEn"]
    info["Movie_name_Og"] = res["movieInfoResult"]["movieInfo"]["movieNmOg"]
    info["Open_date"] = res["movieInfoResult"]["movieInfo"]["openDt"][:4]
    info["Show_time"] = res["movieInfoResult"]["movieInfo"]["showTm"]
    info["Genres"] = '/'.join([genre["genreNm"] for genre in res["movieInfoResult"]["movieInfo"]["genres"]])
    info["Directors"] = '/'.join([director["peopleNm"] for director in res["movieInfoResult"]["movieInfo"]["directors"]])
    info["Watch_grade"] = res["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]
    info["Actors"] = [actor["peopleNm"] for i, actor in enumerate(res["movieInfoResult"]["movieInfo"]["actors"]) if i < 3]
    while len(info["Actors"]) < 3:
        info["Actors"] += [""]
    return info
        

#boxoffice.csv파일에서 영화 코드를 가져온 후 movieCds리스트에 저장
movieCds = []
with open('boxoffice.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movieCds += [row['movie_code']]

key = os.getenv("project01_key")
result = {}

for movieCd in movieCds:
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
    res = requests.get(url).json()
    result[movieCd] = movie_info(res, result)
result_save(result)



