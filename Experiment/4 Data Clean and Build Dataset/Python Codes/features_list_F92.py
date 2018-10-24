#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 5`, `COL 6`, `COL 28` FROM `SMQ`;';
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

average2 = 600/1261; #670
average2 = round(average2, 8);

num = 0;
avg = 0;
for i in range(1, size):
    if data2[i][1]!= '#NULL!' and float(data2[i][1])>0 and float(data2[i][1])<100:
        if data2[i][2] == '1':
            avg = avg + float(data2[i][1])*1;
            num = num + 1;
            data2[i][1] = float(data2[i][1]) * 1;
        elif data2[i][2] == '2':
            avg = avg + float(data2[i][1])*7;
            num = num + 1;
            data2[i][1] = float(data2[i][1]) * 7;
        elif data2[i][2] == '3':
            avg = avg + float(data2[i][1])*12*30;
            num = num + 1;
            data2[i][1] = float(data2[i][1])*12*30;
        elif data2[i][2] == '4':
            avg = avg + float(data2[i][1])*365;
            num = num + 1;
            data2[i][1] = float(data2[i][1]) * 365;
        else:
            avg =avg;
    elif data2[i][1] == '66666':
        avg = avg + 50*365;
        num = num + 1;
        data2[i][1] = 50*365;
    else:
        avg = avg;
# end of loop
average1 = avg/num;
average1 = round(average1,6);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '#NULL!':
            data2[i][1] = average1;
    elif data2[i][1] == '99999':
            data2[i][1] = average1;
    else:
        data2[i][1] = float(data2[i][1]);

    if data2[i][2] == '1':
            data2[i][2] = 1;
    elif data2[i][2] == '2':
            data2[i][2] = 0;
    elif data2[i][2] == '7':
        data2[i][2] = average2;
    elif data2[i][2] == '9':
        data2[i][2] = average2;
    else:
        data2[i][2] = average2;


    x = (float(data2[i][1])/365/50+float(data2[i][2]))/2;
    data2[i][1] = round(x, 8);
    x = 0;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F92` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F92` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();