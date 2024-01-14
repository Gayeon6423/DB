## pymysql 기본 사용법1
import pymysql
import pandas as pd

# MySQL 데이터 베이스 연결
# host, user, password, db에는 접속 정보 입력
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8')

# cursor(DB와 상호작용 할 때 사용되는 위치 지시자) 생성
# cursor에 데이터 딕셔너리 옵션 부여(결과를 데이터 딕셔너리로 자동으로 변경)
cursor = connection.cursor(pymysql.cursors.DictCursor)

# SQL 생성(DB에 존재하는 테이블)
SQL = '''
SELECT * 
FROM `서울시 상권분석서비스(상권-소득소비)`
'''
# cursor를 이용해서 SQL실행
cursor.execute(SQL)

# 모든 데이터를 가져옴
datas = cursor.fetchall()

# insert, update, delete의 경우 자원 닫아주기 전에 commit을 해야 DB에 작업 내용 저장
# connection.commit()

# 사용했던 DB 관련 자원들을 닫아줌
cursor.close()
connection.close()

# 가져온 데이터 확인
pd.DataFrame(datas)


## pymysql 기본 사용법2
# MySQL 데이터 베이스 연결
# host,user,password, db에는 접속 정보 입력
with pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8') as connection:

    # cursor 생성
    # cursor에 데이터 딕셔너리 옵션 부여
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # SQL 생성(DB에 존재하는 테이블)
    SQL = '''
    SELECT * 
    FROM `서울시 상권분석서비스(상권-소득소비)`
    '''
    # cursor를 이용해서 SQL실행
    cursor.execute(SQL)

    # 모든 데이터를 가져옴
    datas = cursor.fetchall()

# 가져온 데이터 확인
pd.DataFrame(datas)
