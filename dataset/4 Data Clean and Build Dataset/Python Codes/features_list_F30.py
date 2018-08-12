import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 9`, `COL 10` FROM `MCQ`;';
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

average1 = 6296/6458; #MCQ070
average1 = round(average1, 8);
average2 = 88/160; #075
average2 = round(average2, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    #010
    if data2[i][1] == '1':
            if data2[i][2] == '1':
                data2[i][1] = 0.75;
            elif data2[i][2] == '2':
                data2[i][1] = 0.5;
            elif data2[i][2] == '3':
                data2[i][1] = 0.25;
            elif data2[i][2] == '4':
                data2[i][1] = 0;
            elif data2[i][2] == '9':
                data2[i][1] = average2;
            else:
                data2[i][1] = average2;
    elif data2[i][1] == '2':
            data2[i][1] = 1;
    elif data2[i][1] == '7':
            data2[i][1] = average1;
    elif data2[i][1] == '9':
            data2[i][1] = average1;
    else:
        # deal with first line and null
        data2[i][1] =  average1;
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F30` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F30` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();