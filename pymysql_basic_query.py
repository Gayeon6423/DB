import pymysql
import pandas as pd

## CREATE : 테이블 생성
# MySQL 데이터 베이스 연결
with pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8') as connection:

    # cursor 생성(딕셔너리 옵션 부여)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    SQL = ''' 
        CREATE TABLE `test1` (
            `id`	BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
            `name`	VARCHAR(50)	NULL,
            `asset`	BIGINT	NULL
        )
    '''
    # cursor를 이용해서 SQL을 실행
    cursor.execute(SQL)

## INSERT : 데이터 삽입
with pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8') as connection:

    # cursor 생성(딕셔너리 옵션 부여)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    SQL = ''' 
        INSERT INTO data.`test1`
        (name, asset)
        VALUES
        ('가연', 500),
        ('지윤', 100),
        ('정현', 300),
        ('한비', 200)
    '''

    cursor.execute(SQL)
    # commit을 통해 DB에 작업 내용 저장
    connection.commit()

## SELECT : 테이블 조회
with pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8') as connection:

    # cursor 생성(딕셔너리 옵션 부여)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    SQL = '''
        SELECT *
        FROM data.test1
    '''
    cursor.execute(SQL)
    data_test = cursor.fetchall()

pd.DataFrame(data_test)


## UPDATE : 테이블 업데이트
with pymysql.connect(
host = '127.0.0.1',
user = 'root',
password = '0520',
database = 'data',
charset = 'utf8') as connection:

    # cursor 생성(딕셔너리 옵션 부여)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    SQL = '''
        UPDATE data.test1
        SET asset = asset + %s
        WHERE name = '가연'
    '''

    # SQL 내에서 변수 치환이 필요할 때
    # SQL 안에 변수가 필요한 부분을 %s로 변경
    # %s에 필요한 값들을 변수에 담아서 execute할 때 같이 매개변수로 전달
    parameter = 500

    # cursor를 이용해서 SQL 실행
    cursor.execute(SQL, parameter)
    connection.commit()
pd.DataFrame(data_test)

## DELETE : 데이터 삭제
with pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0520',
    database = 'data',
    charset = 'utf8') as connection:

    # cursor 생성(딕셔너리 옵션 부여)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    SQL = '''
        DELETE FROM data.test1
        WHERE name = %s
    '''

    # SQL 안에 변수가 필요한 부분을 %s로 변경
    # %s에 필요한 값들을 변수에 담아서 execute할 때 같이 매개변수로 전달
    parameter = '한비'

    # cursor를 이용해서 SQL실행
    cursor.execute(SQL, parameter)
    connection.commit()

