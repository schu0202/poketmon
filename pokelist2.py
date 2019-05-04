import requests
from bs4 import BeautifulSoup
import pymysql
conn = pymysql.connect(host='', user='', password='', db='', charset='utf8')
curs = conn.cursor()
 # 214 ~ 241 사이에 자료가 없기 때문에 for문을 2번 사용
pokemon = {}
pokemonall ={}
typeall = [] # 중복되는 타입이 있을경우
charaall= [] # 중복되는 특성이 있을 경우
for i in range(164, 215):
    if(i == 194) : #같은 번호 제외(ex 메가진화)
        pass
    else :
        URL = 'https://pokemonkorea.co.kr/pokedex/single/'+str(i) # 포켓몬 사이트

    res = requests.get(URL) #get방식으로 저장

    bsObject = BeautifulSoup(res.text, 'html.parser')
    nums = bsObject.find("div", class_="single_header_wrap") # 이름
    nums1 = bsObject.find("div", class_="type") # 타입
    nums2 = bsObject.find("div", class_="col-xs-6 nopd") # 키와 몸무게
    nums3 = bsObject.find_all("div", class_="col-xs-6 nopd")  # 특성과 분류

    name = nums.find('h1').text
    name1 = name.split(' ')
    type1 = nums3[1].find('b').text # 분류
    charact = nums3[1].find_all("b", class_="mgr5")  # 특성

    for ty in nums1.find_all('span'):  # 하나의 변수
        typeall.append(ty.text)
    typeallF = ", ".join(typeall)  # 리스트를 하나의 변수로 합침
    del typeall[:] #리스트가 중복출력되지 않게 초기화

    for ch in nums3[1].find_all("b", class_="mgr5") :
        charaall.append(ch.text)
    charaallF="".join(charaall)
    del charaall[:]

    for weight in nums2.find_all('b'): # 몸무게
        pass
    height = nums2.find('b').text # 키

    pokemon = {'type': typeallF, 'type1' : type1, 'characteristic' : charaallF, 'height': height, 'weight': weight.text}
    pokemonall[name1[0]] = pokemon

sql = 'INSERT INTO pokemon2 (NAME, type, type1, chara, height, weight) VALUES (%s, %s, %s, %s, %s, %s)' #필드명
    # 파이썬 딕셔너리 반복문

for n, na in pokemonall.items():
    curs.execute(sql, (n, na['type'], na['type1'], na['characteristic'], na['height'], na['weight']))

conn.commit()  # 영구저장

sql = "select * from pokemon1"
curs.execute(sql)
    # 데이타 Fetch

rows = curs.fetchall()

pokemon.clear() # 위 번호와 중복 제거를 위한 초기화
pokemonall.clear() # 중복 제거를 위한 초기화

for j in range(242, 296):
    if(j == 272 or j == 253 or j == 256 or j == 292) : #같은 번호 제외(ex 메가진화)
        pass
    else :
        URL = 'https://pokemonkorea.co.kr/pokedex/single/'+str(j) # 포켓몬 사이트

    res = requests.get(URL) #get방식으로 저장

    bsObject = BeautifulSoup(res.text, 'html.parser')
    nums = bsObject.find("div", class_="single_header_wrap") # 이름
    nums1 = bsObject.find("div", class_="type") # 타입
    nums2 = bsObject.find("div", class_="col-xs-6 nopd") # 키와 몸무게
    nums3 = bsObject.find_all("div", class_="col-xs-6 nopd")  # 특성과 분류

    name = nums.find('h1').text
    name1 = name.split(' ')
    type1 = nums3[1].find('b').text # 분류
    charact = nums3[1].find_all("b", class_="mgr5")  # 특성

    for ty in nums1.find_all('span'):  # 하나의 변수
        typeall.append(ty.text)
    typeallF = ", ".join(typeall)  # 리스트를 하나의 변수로 합침
    del typeall[:] #리스트가 중복출력되지 않게 초기화

    for ch in nums3[1].find_all("b", class_="mgr5") :
        charaall.append(ch.text)
    charaallF="".join(charaall)
    del charaall[:]

    for weight in nums2.find_all('b'): # 몸무게
        pass
    height = nums2.find('b').text # 키

    pokemon = {'type': typeallF, 'type1' : type1, 'characteristic' : charaallF, 'height': height, 'weight': weight.text}
    pokemonall[name1[0]] = pokemon

sql = 'INSERT INTO pokemon2 (NAME, type, type1, chara, height, weight) VALUES (%s, %s, %s, %s, %s, %s)' #필드명
    # 파이썬 딕셔너리 반복문

for n, na in pokemonall.items():
    curs.execute(sql, (n, na['type'], na['type1'], na['characteristic'], na['height'], na['weight']))

conn.commit()  # 영구저장

sql = "select * from pokemon1"
curs.execute(sql)
    # 데이타 Fetch

rows = curs.fetchall()

conn.close()





