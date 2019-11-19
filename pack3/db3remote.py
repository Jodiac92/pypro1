# 원격 DB와 접속

import MySQLdb

'''
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='kic1234', database='test')
print(conn)
conn.close
'''

# sangdata CRUD
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    # insert
    '''
    sql = "insert into sangdata values(%s, %s, %s, %s)"
    sql_data = ('10','볼펜', 10, 3000)
    cursor.execute(sql, sql_data)
    
    conn.commit()
    '''
    # updata
    '''
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
    sql_data = ('지우개', 10, 2500,10)
    cursor.execute(sql, sql_data)
    
    conn.commit()
    '''
    
    # delete

    code = '10'
    
    # 1 : 보안 문제가 있음
    #sql = "delete from sangdata where code" + code
    #cursor.execute(sql)
    
    # 2
    #sql = "delete from sangdata where code=%s"
    #cursor.execute(sql, (code,))
    
    # 3
    sql = "delete from sangdata where code={0}".format(code)
    cursor.execute(sql)
    
    conn.commit()
    
    # select
    sql = "select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    # 1
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
        
    print()
    
    # 2
    for r in cursor:
        #print(r)
        print(r[0], r[1], r[2], r[3])
    
    print() 
    # 3
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
    
    print()
     # 4
    for (a, b, kbs, mbc) in cursor:
        print(a, b, kbs, mbc)   
    
except Exception as e:
    print('err : ',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()