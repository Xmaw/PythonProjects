import xlrd

file_path = 'C:\\Users\\Johan\\PycharmProjects\\export.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)

lena = 0
for rows in range(sheet.nrows):
    cell = sheet.cell_value(rows, 1).lower()
    if 'swish' in cell and 'lena' in cell:
        amount = sheet.cell_value(rows, 3)
        print(cell, 'amount:', sheet.cell_value(rows, 3))
        amount = amount.replace('.', '')
        amount = amount.replace(',', '.')
        lena += float(amount)
print('Total lena:', lena)
