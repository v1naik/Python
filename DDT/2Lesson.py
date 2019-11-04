import openpyxl

# EXcel file is initially empty
path = "/Users/vsnaik/PycharmProjects/Selenium/Test2.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active # sheet = workbook.get_sheet_by_name("Sheet1")


for r in range(1, 6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value = "Welcome"


workbook.save(path)
