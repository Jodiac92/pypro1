# 개인용 db : sqlite
import sqlite3
print(sqlite3.sqlite_version)

#conn = sqlite3.connect('exam.db')
conn = sqlite3.connect(':memory:') # ram에 자료가 존재(휘발성)

try:
    c = conn.cursor() # sql문 실행
    #c.execute("drop table friend")
    c.execute("create table if not exists friend(name text, phone text, addr text)")
    # text, integer, real, null, blob
    
    c.execute("insert into friend(name, phone, addr) values('한국인','111-1111','역삼1동')")
    c.execute("insert into friend values('홍길동','222-2222','서초1동')")
    c.execute("insert into friend values(?,?,?)",('고길동','111-3333','서초2동'))
    
    id_data = ('나길동','111-4444','서초3동')
    c.execute("insert into friend values(?,?,?)", id_data)
    
    conn.commit()
    
    # select
    c.execute("select * from friend")
    #print(c.fetchone())
    
    print(c.fetchall())
    
    print()
    c.execute("select name, phone, addr from friend") # print(c.fetchall()) 에서 커서가 마지막에 있기 때문에 다시 불러와야한다.
    for r in c:
        #print(r)
        print('이름 : ' + r[0] + ', 전화번호 : ' + r[1] + ' , 주소 : ' + r[2])
    
except Exception as e:
    print('err : ' + str(e))
    conn.rollback()
finally:
    conn.close()