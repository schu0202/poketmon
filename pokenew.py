import requests
from bs4 import BeautifulSoup
import pymysql
import schedule
def job():
    conn = pymysql.connect(host=, user=, password=, db=, charset='utf8')
    curs = conn.cursor()

    news = {}
    new = []

    URL = 'https://pokemonkorea.co.kr/main_v2'
    res = requests.get(URL) #get방식으로 저장

    bsObject = BeautifulSoup(res.text, 'html.parser')
    for name in bsObject.find_all("div", class_="post-info"):
            new.append(name.text)

    sql1 = 'DELETE FROM news' # 기존 정보 제거
    sql = 'INSERT INTO news (new, num) VALUES (%s, %s)' # 새로운 정보 추가

    curs.execute(sql1)
    for i in range(0,13):
        curs.execute(sql, (new[i], i+1))

    conn.commit()  # 영구저장

    sql = "select * from pokemon1"
    curs.execute(sql)
    # 데이타 Fetch

    rows = curs.fetchall()
    conn.close()


schedule.every(1).seconds.do(job) # 이 스케줄을 1초에 한번씩 체크

while True:
    schedule.run_pending() # 무한루프를 돌면서 스케줄 유지





