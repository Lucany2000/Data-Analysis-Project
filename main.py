import os
from openpyxl import load_workbook, Workbook
import pandas as pd

data = os.listdir("analysis_project")
if os.path.exists('/analysis_project.xlsx') == False:
    wb = Workbook()
    del wb['Sheet'] 
else:    
    wb = load_workbook('analysis_project.xlsx')
    
writer = pd.ExcelWriter('analysis_project.xlsx', engine = 'openpyxl')
writer.book = wb

for d in data:
    df = pd.read_csv(f'analysis_project\{d}', sep='\t')
    fname = d.replace(".pooled.tsv","")
    print(fname)
    df.to_excel(writer, sheet_name=fname)

wb.save('analysis_project.xlsx')
writer.close()