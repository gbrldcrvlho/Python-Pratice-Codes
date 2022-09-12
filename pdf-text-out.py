import PyPDF

# Carrega o arquivo PDF
pdfFileObj = open('meupdf.pdf', 'rb')

# Faz a leitura do arquivo PDF
pdfReader = PyPDF2.PdfFIleReader(pdfFileObj)

# Captura primeira pagina do PDF
pageObj = pdfReader.getPage(0)

# Extrai texto do PDF e passa para variavel
text = pageObj.extractText()

# Mostra texto do PDF
print(text)



