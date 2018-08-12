import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 9`, `COL 10`, `COL 11`, `COL 12`, `COL 13`, `COL 14`, `COL 15`, `COL 16`, `COL 17`, `COL 18`, `COL 19`, `COL 20`, `COL 21`, `COL 22`, `COL 23`, `COL 24`, `COL 25`, `COL 26`, `COL 27`, `COL 28`, `COL 29` FROM `WHQ`;';
cursor.execute(sql);

# store into variable 'data'
data = cursor.fetchall();
size = len(data);

print(data);

# convert into numpy str array
data2 = [];
data2 = numpy.array(data);
data2.flatten();

# test and valid values after first line
print(data2);

# calculate and normalise
for i in range(1, size):
    if data2[i][1]=='10':
        data2[i][1]= 1;
    else:
        data2[i][1]= 0;


    if data2[i][2]=='11':
        data2[i][2]= 1;
    else:
        data2[i][2]= 0;

    if data2[i][3]=='12':
        data2[i][3]= 1;
    else:
        data2[i][3]= 0;

    if data2[i][4]=='13':
        data2[i][4]= 1;
    else:
        data2[i][4]= 0;

    if data2[i][5]=='14':
        data2[i][5]= 1;
    else:
        data2[i][5]= 0;

    if data2[i][6]=='15':
        data2[i][6]= 1;
    else:
        data2[i][6]= 0;

    if data2[i][7]=='16':
        data2[i][7]= 1;
    else:
        data2[i][7]= 0;

    if data2[i][8]=='17':
        data2[i][8]= 1;
    else:
        data2[i][8]= 0;

    if data2[i][9]=='31':
        data2[i][9]= -1;
    else:
        data2[i][9]= 0;

    if data2[i][10]=='32':
        data2[i][10]= -1;
    else:
        data2[i][10]= 0;

    if data2[i][11]=='33':
        data2[i][11]= -1;
    else:
        data2[i][11]= 0;

    if data2[i][12]=='34':
        data2[i][12]= -1;
    else:
        data2[i][12]= 0;

    if data2[i][13]=='30':
        data2[i][13]= -1;
    else:
        data2[i][13]= 0;

    if data2[i][14]=='41':
        data2[i][14]= 1;
    else:
        data2[i][14]= 0;

    if data2[i][15]=='42':
        data2[i][15]= -1;
    else:
        data2[i][15]= 0;

    if data2[i][16]=='43':
        data2[i][16]= 1;
    else:
        data2[i][16]= 0;

    if data2[i][17]=='44':
        data2[i][17]= 1;
    else:
        data2[i][17]= 0;

    if data2[i][18]=='45':
        data2[i][18]= 1;
    else:
        data2[i][18]= 0;

    if data2[i][19]=='46':
        data2[i][19]= 1;
    else:
        data2[i][19]= 0;

    if data2[i][20]=='35':
        data2[i][20]= -1;
    else:
        data2[i][20]= 0;

    if data2[i][21]=='40':
        data2[i][21]= -1;
    else:
        data2[i][21]= 0;

    data2[i][1] = float(data2[i][1]) + float(data2[i][2]) + float(data2[i][3])  + float(data2[i][4]) + float(data2[i][5]) + float(data2[i][6]) + float(data2[i][7]) + float(data2[i][8]) + float(data2[i][9]) + float(data2[i][10]) + float(data2[i][11]) + float(data2[i][12]) + float(data2[i][13]) + float(data2[i][14]) + float(data2[i][15]) + float(data2[i][16]) + float(data2[i][17]) + float(data2[i][18]) + float(data2[i][19]) + float(data2[i][20]) + float(data2[i][21]);
    if float(data2[i][1])>=1:
        data2[i][1] = 1;
    elif float(data2[i][1])==0:
        data2[i][1] = 0.5;
    else:
        data2[i][1] = 0;
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F16` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F16` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();