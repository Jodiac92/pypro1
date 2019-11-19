import sqlite3

def dbFunc(dbName):
    try:
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        
#         try:
#             cur.execute("select * from jikwon")
#         except Exception as e2:
#             cur.execute("create table jikwon(id integer primary key, name text)")

        cur.execute("drop table if exists jikwon")
        cur.execute("create table if not exists jikwon(id integer primary key, name text)")
        # insert
        cur.execute("insert into jikwon values(1,'홍길동')")
        tdata = (2,'고길동') # tuple
        cur.execute("insert into jikwon values(?, ?)", tdata)
        
        tdata2 = 3,'한송이' # tuple
        cur.execute("insert into jikwon values(?, ?)", tdata2)
        
        ldata = [4,'신기해'] # list
        cur.execute("insert into jikwon values(?, ?)", ldata)

        manydata = [(5,'신기루'),(6, '밀가루')] # list
        cur.executemany("insert into jikwon values(?, ?)", manydata) # 여러개 집어 넣을 때
        
        # set 타입은 불가능
        
        dicdata1 = {'id' : 7, 'name' : '김밥' } # dict
        cur.execute("insert into jikwon values(:id, :name)", dicdata1)

        dicdata2 = {'sabun' : 8, 'irum' : '주먹밥' } # dict
        cur.execute("insert into jikwon values(:sabun, :irum)", dicdata2)
        
        # update
        updata = ('박치기', 8)
        cur.execute("update jikwon set name = ? where id = ?", updata)
        
        # delete
        delete = (8,)
        cur.execute("delete from jikwon where id = ?",delete)
        # select
        print('출력  1')
        cur.execute("select * from jikwon")
        #cur.execute("select * from jikwon where id <= 2")
        #cur.execute("select * from jikwon where id <= %d"%2)
        #cur.execute("select * from jikwon where name = '%s'"%'홍길동')
        for r in cur:
            print(str(r[0]) + ' ' + r[1])
        
        print('\n출력  2')
        cur.execute("select * from jikwon")
        for r in cur.fetchall():
            print(str(r[0]) + ' ' + r[1])
            
        print('\n출력  3')
        cur.execute("select count(*) from jikwon")
        print("건수 : "+ str(cur.fetchone()[0]))
    except Exception as e:
        print('err : ' + str(e))
    finally:
        conn.close()
if __name__ == '__main__':
    dbFunc('test.db')