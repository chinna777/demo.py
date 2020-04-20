import cx_Oracle as ora
import csv
import logging
con = ora.connect('system/1234@localhost')
print('connected')
cur=con.cursor()
print('cursor is in our hand')
logging.basicConfig(filename='myfile3.log',level=logging.DEBUG)
try:
    with open('Csv1.csv', 'r') as f:
        logging.info("reading the csv file into reader object")
        reader=csv.reader(f)
        lines=[]
        for i in reader:
            lines.append(i)
    print(lines)
    logging.info("inserting the list data into oracle db")
    cur.executemany("insert into  data(first_name,last_name,company_name,address,city,county,state,zip,phone1,phone2,email,web) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",lines)
    print('data inserted')
    logging.info("fetching the inserted data ")
    cur.execute("select * from data")
    data1=cur.fetchall()
    print('data fetched')
    print(data1)
except:
    logging.critical('something went wrong')
finally:
    con.commit()
    cur.close()
    con.close()
 