import openpyxl
from openpyxl import workbook
workbook = openpyxl.Workbook()
data = [
    ["name", "age"],
    ["ahmed",25]
]

for row in data :
    workbook.active.append(row)
workbook.save("test.xlsx")    