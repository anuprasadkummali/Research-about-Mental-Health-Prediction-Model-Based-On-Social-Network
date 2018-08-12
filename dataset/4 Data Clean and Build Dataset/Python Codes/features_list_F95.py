#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`, `COL 6`, `COL 7`, `COL 8`, `COL 9` FROM `OCQ`;';
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
vote = 0;
for i in range(1, size):
    if data2[i][1] == '3' or data2[i][1] == '4' or data2[i][1] == '#NULL!':
        if data2[i][2] == '77777' or data2[i][2] == '99999' or data2[i][2] == '#NULL!':
            vote = vote + 1;
        if data2[i][4] == '77' or data2[i][4] == '99' or data2[i][4] == '#NULL!':
            vote = vote + 1;
        if data2[i][5] == '77777' or data2[i][5] == '99999' or data2[i][5] == '#NULL!':
            vote = vote + 1;
        if data2[i][6] != '2' and data2[i][6] != '3' and data2[i][6] != '5':
            vote = vote + 1;
        if vote == 4:
            data2[i][1] = 0;
        else:
            data2[i][1] = 0.5;
        vote = 0;
    else:
        data2[i][1] = 1;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F95` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F95` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();