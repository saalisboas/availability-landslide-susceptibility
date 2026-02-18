import fitz as pdf
import pathlib
import numpy as np
from difflib import SequenceMatcher as sm


sheet = np.loadtxt(
    'data/br/articles-br.csv',
    dtype='U',
    delimiter=',',
    quotechar='"',
) #from Scopus search
sheet_title_column = sheet[:, 3] #used for search in sheet
#select the info column. 
sheet_doi_column = sheet[:, 7] 

directory_with_pdfs = 'data/br'
archives = pathlib.Path(directory_with_pdfs)
pdf_all = list(archives.glob('*.pdf'))

list = [['github', 'zenodo'], ['data availability statement', 'reasonable request', 'available on request', 'available upon request'], ['data availability', 'code availability']]
for words in list:
	for pdf_n in pdf_all:
	    doc = pdf.open(pdf_n)
	    found = False
	    for n in range(doc.page_count):
	        page = doc.load_page(n) #text extraction is only for pages
	        page_text = page.get_text().lower() #lower for comparison with words
	        for word in words:
	            if word in page_text:
	                article_title = doc.metadata['title'] #extracted for search in sheet
	                print(f'ARQUIVO: {pdf_n}') 
	                title_similarity = []
	                for title in sheet_title_column:
	                    title_similarity.append(sm(None, title, article_title).ratio() > 0.85) #0.85 is a quality estimation
	                for indice, trues in enumerate(title_similarity):
	                    if trues:
	                        print(f'Informações: Linha: {indice}, DOI: {sheet_doi_column[indice]}')
	                found = True
	                break 
	        if found:
	            break
	print('PROXIMA FILTRAGEM ...')
