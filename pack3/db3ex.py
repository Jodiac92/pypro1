import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

num = input('부서 번호를 입력하시오 : ')
try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    sql = '''
    select jikwon_no, jikwon_name, buser_name, jikwon_jik 
    from buser,jikwon 
    where buser.buser_no = jikwon.buser_num and buser.buser_no = {0}
    '''.format(num)
    
    cur.execute(sql)
    
    print("직원번호 \t이름\t부서명\t직급")
    for r in cur:
        print("%s\t%s\t%s\t%s"%r)
        
    sql = "select count(*) from jikwon where buser_num={0}".format(num)
    cur.execute(sql)
    print("인원수 : {0}명".format(cur.fetchone()[0]))
except Exception as e:
    print('err : ',e)
finally:
    cur.close()
    conn.close()
