import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014', autocommit=True);
cursor = conn.cursor();
# fill up all NULL
for x in range(1, 98):
     query = "UPDATE features_list_fillup SET F%s = 1 WHERE F%s = '';";
     cursor.execute(query, (x, x));
     conn.commit(); # very important for update sql server
# close DB
cursor.close();
del cursor;
conn.close();