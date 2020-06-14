import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Sheet1')
sheet2 = book.add_sheet('Sheet2')

sheet1.write(1,1,'世界，你好')
sheet1.write(2,2,'用Python操作Excel文件')
sheet2.write(2,2,'Hello World')

book.save('demo.xls')

