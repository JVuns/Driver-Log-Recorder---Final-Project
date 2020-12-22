import os
import os.path
import openpyxl
import json
data = []
diksi= {}
datamax = int(10 + int(input("banyak baris data: ")))
class Karyawan():
    
    def __init__(self, tanggal, pit, spec, namaOperator):
        self.tanggal = tanggal
        self.pit = pit
        self.spec = spec
        self.namaOperator = namaOperator
        
wb = openpyxl.load_workbook(filename="C:/Users/jevon/Documents/GitHub/Coal Proj/Data2", data_only = True)
sheet = wb.active
sheet.title = "Sheet2"
for row in sheet.iter_rows(min_row=1,max_row=datamax,min_col=1,max_col=23,values_only=True):
    if row[0] is not None:
        subdata = [f"{row[2]}",f"{row[6]}",f"{row[13]}",f"{row[22]}"]
        data.append(subdata)
print(data)
# def split():
#     for subdata in data:
#         print(subdata)
#         if subdata[3] not in diksi:
#             diksi[subdata[3]] = []
#     for subdata in data:
#         diksi[subdata[3]].append([subdata[0]])
#         diksi[subdata[3]][0].append(subdata[1])
            

# split()
# print(diksi["Andriansyah"])



