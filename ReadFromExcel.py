import xlrd

file_path = 'Skrivbord/export.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0,0))