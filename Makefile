# alvo: dependencias
#	comando

.PHONY: clean all show

all: paper/relatorio-2.pdf

show: paper/relatorio-2.pdf
	open paper/relatorio-2.pdf

results/previo-br.txt: code/searching.py data/
	mkdir -p results/
	python code/searching.py > results/previo-br.txt 

figures/: code/analysis-graphics.py results/br-articles-open.txt results/br-articles-request.txt
	mkdir -p figures/
	python code/analysis-graphics.py

paper/relatorio-2.pdf: paper/relatorio-2.tex paper/fluxograma.png paper/intro-refs.bib figures/
	tectonic -X compile paper/relatorio-2.tex

clean:
	rm -rf results/previo-*.txt figures/ paper/relatorio-2.pdf
