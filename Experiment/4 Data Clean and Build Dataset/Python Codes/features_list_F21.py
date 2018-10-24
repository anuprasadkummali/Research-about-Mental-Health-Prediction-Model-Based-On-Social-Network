import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 6`, `COL 9`, `COL 10` FROM `ALQ`;';
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

average1 = 0;#130
average2 = float(736/4476);#151
average3 = 0;#160
num1 = 0;
num3 = 0;

for i in range(1, size):
    if data2[i][1]!='#NULL!' and float(data2[i][1])>= 0 and float(data2[i][1])<400:
        average1 = average1 + float(data2[i][1]);
        num1 = num1 + 1;
    if data2[i][3]!='#NULL!' and float(data2[i][3])>= 0 and float(data2[i][3])<400:
        average3 = average3 + float(data2[i][3]);
        num3 = num3 + 1;
# end of loop

average1 = average1/num1;
average3 = average3/num3;
average1 = round(average1, 8);
average2 = round(average2, 8);
average3 = round(average3, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    #130
    if data2[i][1] == '777':
            data2[i][1] = average1;
    elif data2[i][1] == '999':
            data2[i][1] = average1;
    elif data2[i][1] == '#NULL!':
            data2[i][1] = average1;
    else:
        # deal with first line and null
        data2[i][1] =  data2[i][1];

    # 151
    if data2[i][2] == '1':
        data2[i][2] = 1;
    elif data2[i][2] == '2':
        data2[i][2] = 0;
    else:
        # deal with first line and null
        data2[i][2] = average2;

    # 160
    if data2[i][3] == '777':
            data2[i][3] = average3;
    elif data2[i][3] == '999':
            data2[i][3] = average3;
    elif data2[i][3] == '#NULL!':
            data2[i][3] = average3;
    else:
        # deal with first line and null
        data2[i][3] =  data2[i][3];

    data2[i][1] = float(data2[i][1])/25;
    data2[i][3] = float(data2[i][3])/30;
    data2[i][1] = 1 - max(float(data2[i][1]),float(data2[i][2]),float(data2[i][3])) ;
    # end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F21` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F21` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();