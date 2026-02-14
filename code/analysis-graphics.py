# Data availability in landslide susceptibility
# Creating graphics for analysis

import numpy as np
import matplotlib.pyplot as plt

sheet_with_articles_info= np.loadtxt(
    '/home/saalisboas/pub/mex/articles-mex-ensaio.csv',
    dtype='U',
    delimiter=',',
    quotechar='"',
    skiprows=1,
)

# with the indices obtained in searching.py
total_artigos = 52
articles_open = [2, 9, 10, 11, 12, 19, 34, 48, 1, 22] 
articles_request = [18, 6, 4, 27, 24, 16, 14, 5, 44, 45, 46, 49, 51, 13]
articles_mentioned = [2, 9, 10, 11, 12, 19, 34, 48, 1, 22, 18, 6, 4, 27, 24, 16, 14, 5, 44, 45, 46, 49, 51, 13]

# standardize colors
cmap = plt.colormaps['tab20']
cmapa = plt.colormaps['tab20b']

# Geral pie
frequencias = [total_artigos, len(articles_open), len(articles_request)]
legenda = ['Não menciona disponibilidade', 'Disponibiliza os dados', 'Disponível mediante solicitação']
plt.figure()
plt.suptitle('Proporção da disponibilidade')
plt.pie(frequencias,
    labels=legenda,
    colors=cmap([0, 4, 10]),
    autopct='%1i%%',
)
plt.show()
# Year pie
year_column = sheet_with_articles_info[:, 4]

anos, frequencias = np.unique(year_column, return_counts=True)

anos_mentioned, frequencias_mentioned = np.unique(year_column[articles_mentioned], return_counts=True)

fig, axes = plt.subplots(1, 2, layout='constrained')
fig.suptitle('Proporção de artigos por ano')
axes[0].pie(frequencias, 
        labels=anos,
        colors=cmapa(np.arange(0, 20)),
        autopct='%1i%%',
        pctdistance=0.9,
        labeldistance=1.05,
)
axes[0].set_title('Todos', loc='left')
axes[1].pie(frequencias_mentioned, 
        labels=anos_mentioned,
        colors=cmapa([1, 4, 5, 6, 7, 8, 9]), #corresponding
        autopct='%1i%%',
        pctdistance=0.9,
        labeldistance=1.05,
)
axes[1].set_title('Mencionam disponibilidade', loc='right')

plt.show()

# Journal bars
journal_column = sheet_with_articles_info[:, 5]

revistas, frequencias = np.unique(journal_column, return_counts=True)

revistas_open, frequencias_open = np.unique(journal_column[articles_open], return_counts=True)

revistas_request, frequencias_request = np.unique(journal_column[articles_request], return_counts=True)

plt.figure(layout='constrained')
plt.suptitle('Disponibilização por revista')
plt.barh(revistas, 
    frequencias, 
    color=cmap([0]),
    label='Não menciona disponibilidade',
)
plt.barh(revistas_open, 
        frequencias_open, 
        color=cmap([4]),
        label='Disponibiliza os dados',
)
plt.barh(revistas_request, 
         frequencias_request, 
         color=cmap([10]), 
         left=[0, 0, 0, 0, 0, 1, 1, 2, 0, 1],
         label='Disponível mediante solicitação',
) #left numbers are to position after open
plt.xlabel('Número de artigos')
plt.legend()
plt.show()


# Citations histogram
citations_column = sheet_with_articles_info[:, 6]
citations_numbers = citations_column.astype(int)

citados = citations_numbers

citados_open = citations_numbers[articles_open]

citados_request = citations_numbers[articles_request]

plt.suptitle('Número de citações')
plt.hist(citados, 
         bins=[0, 25, 50, 75, 100, 125, 150, 175, 200], #to stacker
         color=cmap([0]),
         label='Não menciona disponibilidade',
)
plt.hist(citados_open, 
         bins=[0, 25, 50, 75, 100, 125, 150, 175, 200],
         color=cmap([4]),
         label='Disponibiliza os dados',
)
plt.hist(citados_request, 
         bins=[0, 25, 50, 75, 100, 125, 150, 175, 200], 
         bottom=[8, 1, 0, 1, 1, 0, 0, 0], #after open
         color=cmap([10]),
         label='Disponível mediante solicitação',
)
plt.xlabel('Quantidade de citações')
plt.ylabel('Número de artigos')
plt.legend()
plt.show()
