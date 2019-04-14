import xlrd

file_path = 'C:\\Users\\Johan\\PycharmProjects\\export.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)

for x in range(4):
    for rows in range(sheet.nrows):
        print(sheet.cell_value(rows, x))
