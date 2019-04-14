import xlrd

file_path = 'C:\\Users\\Johan\\PycharmProjects\\export.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)

for rows in range(sheet.nrows):
    cell = sheet.cell_value(rows, 1)
    if 'Swish' in cell:
        print(cell)
