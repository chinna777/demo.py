import cx_Oracle as ora
import xlsxwriter
con = ora.connect('system/1234@localhost')
print('connected')
cur=con.cursor()
print('cursor is in our hand')
try:
    cur.execute('select * from Employee')
    rows= cur.fetchall()
    print('data fetched')
    print("hi")
    print(rows)
    print(rows[1])
    
    with xlsxwriter.Workbook('test2.xlsx') as workbook:
            worksheet = workbook.add_worksheet()
            for rownumber, values in enumerate(rows):
                 worksheet.write_row(rownumber, 0, values)
                 print('row added')
                 con.commit()
except :
    print('something went wrong check thoroughly')
    con.rollback()
finally:
    
    cur.close()
    con.close()
    