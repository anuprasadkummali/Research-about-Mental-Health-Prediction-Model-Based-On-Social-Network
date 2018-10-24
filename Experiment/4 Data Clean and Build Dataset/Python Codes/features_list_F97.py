#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `HUQ`.`COL 1`, `HUQ`.`COL 2`, `HSQ`.`COL 2`, `HSQ`.`COL 1` FROM `HSQ` RIGHT JOIN `HUQ` ON `HUQ`.`COL 1` = `HSQ`.`COL 1`; ';
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

average1 = (2615+2716*0.75+3235*0.5+1330*0.25)/10170; #huq010
average1 = round(average1, 8);
average2 = (641+1826*0.75+2605*0.5+1186*0.25)/6466; #hsd010
average2 = round(average2, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
            data2[i][1] = 1;
    elif data2[i][1] == '2':
            data2[i][1] = 0.75;
    elif data2[i][1] == '3':
            data2[i][1] = 0.5;
    elif data2[i][1] == '4':
            data2[i][1] = 0.25;
    elif data2[i][1] == '5':
            data2[i][1] = 0;
    else:
        data2[i][1] = average1;


    if data2[i][2] == '1':
            data2[i][2] = 1;
    elif data2[i][2] == '2':
            data2[i][2] = 0.75;
    elif data2[i][2] == '3':
        data2[i][2] = 0.5;
    elif data2[i][2] == '4':
        data2[i][2] = 0.25;
    elif data2[i][2] == '5':
        data2[i][2] = 0;
    else:
        data2[i][2] = average2;

    if data2[i][0] != data2[i][3]:
        if data2[i][0] is None:
            data2[i][0] = data2[i][3];
            data2[i][1] = data2[i][2];
    else:
        x = (float(data2[i][1])+float(data2[i][2]))/2;
        data2[i][1] = round(x, 8);
        x = 0;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F97` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F97` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();