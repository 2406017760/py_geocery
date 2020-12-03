import xlrd
import matplotlib

workbook=xlrd.open_workbook('C:\\Users\\admin\\Desktop\\py.xls')
sheet=workbook.sheets()[0]
score=sheet.col(3)

