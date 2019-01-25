import requests
import os
import urllib.request
import csv

# movieimgs = [(img링크, 영화코드), ().....] 생성
movieimgs = []
with open('movie_naver.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movieimgs += [(row['Movie_img'], row['Movie_code'])]        

#images폴더 생성
os.mkdir('C:\\Users\\student\\Desktop\\python_project_01\\images')

#image 저장하기
for movieimg in movieimgs:
    #image 경로 및 영화 코드로 파일 이름 설정 
    name = f'C:\\Users\\student\\Desktop\\python_project_01\\images\\{movieimg[1]}.jpg'   
    req = requests.get(movieimg[0], stream=True)
    #wb모드로 이미지 저장
    with open(name, 'wb') as f:
        for img in req.iter_content():
            f.write(img)