import csv
import requests
import json
import datetime
import os

#파일 저장 함수
def result_save(result):
    with open('boxoffice.csv', 'w', newline='', encoding='UTF-8') as f:
        fieldnames = ('movie_code', 'movie_name', 'audience', 'date')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        for key,value in result.items():
            writer.writerow({'movie_code': key, 'movie_name': value["movieNm"], 'audience': value["audiAcc"], 'date': value["date"]})

#결과값 가져오는 함수 , 원하는 값을 추출해 결과값들을 저장하는 result 딕셔너리에 업데이트     
def make_movie_dict(res, result, date):
    for movie in res["boxOfficeResult"]["weeklyBoxOfficeList"]:
        movieCd = movie["movieCd"]
        movieNm = movie["movieNm"]
        audiAcc = movie["audiAcc"]
        result.update({movieCd: {"movieNm": movieNm, "audiAcc": audiAcc, "date": date}})
    return result

#기준일(2019년 1월 13)의 11주 전을 계산
date = datetime.datetime(2019,1,13) - datetime.timedelta(days=70)
key = os.getenv("project01_key")
result = {}

#기준일의 10주 전부터 기준일까지 7일 간격으로 총 10번 추출
for i in range(10):
    date += datetime.timedelta(days=7)  #다음주로 날짜 조정
    targetDt = date.strftime('%Y%m%d')  #날짜를 스트링값으로 저장
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
    res = requests.get(url).json()
    make_movie_dict(res, result, targetDt)
    
result_save(result)
            

