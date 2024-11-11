import openpyxl

# Pegar os dados da planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']
# Transferir para a imagem do certificado
