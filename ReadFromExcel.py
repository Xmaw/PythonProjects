import xlrd

amount = 0
name = 'alexander'
for n in range(0, 22):
    file_path = 'C:\\Users\\Johan\\Livet\\Utdrag\\'
    if n == 0:
        file_name = 'export.xls'
    else:
        file_name = 'export (' + str(n) + ').xls'

    file_path = file_path + file_name
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    for rows in range(sheet.nrows):
        cell = sheet.cell_value(rows, 1).lower()
        if 'swish' in cell and name in cell:
            temp = sheet.cell_value(rows, 3)
            print(cell, 'amount:', sheet.cell_value(rows, 3))
            temp = temp.replace('.', '')
            temp = temp.replace(',', '.')
            amount += float(temp)
print('Total ', name, ':', amount, 'kr')
