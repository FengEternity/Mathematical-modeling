import openpyxl


wb = openpyxl.load_workbook('公路最短路径2.xlsx')


sheet = wb.active


for row in sheet.iter_rows():
    for cell in row:

        if cell.value is not None and isinstance(cell.value, (int, float)):

            cell.value *= 0.1


wb.save('公路运输费用2.xlsx')
