# dbms_mysql.py

import pymysql

# MySQL 서버에 연결하는 함수
conn = pymysql.connect(
    host="localhost",  # ip주소(같은 컴퓨터일 떈 localhost 또는 127.0.0.1 => mysql 서버 주소)
    # port=3306,             # 포트번호(기본값 3306)
    user="root",
    password="1234",
    database="exampledb",
    charset="utf8mb4",      # utf8 확장버전 인코딩
    cursorclass=pymysql.cursors.DictCursor  # 커서에 입력되는 내용들을 결과로 조회할때 딕셔너리 형태로 결과 반환, 기본값은 튜플 형태

)

# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한번 호출에 하나의 Row를 가져올때 사용
print("현재 데이터베이스: ", cursor.fetchone())
print("현재 데이터베이스: ", type(cursor.fetchone()))
# print("현재 데이터베이스: ", cursor.fetchall())
# print("현재 데이터베이스: ", cursor.fetchmany())

# 연결 해제 함수
conn.close()