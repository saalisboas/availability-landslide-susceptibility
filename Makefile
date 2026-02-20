# alvo: dependencias
#	comando

.PHONY: clean all show

all: paper/parcial.pdf

show: paper/parcial.pdf
	open paper/parcial.pdf

results/: code/searching.py data/
	mkdir -p results/
	python code/searching.py > results/previo-br.txt 

figures/: code/analysis-graphics.py results/br-articles-open.txt results/br-articles-request.txt
	mkdir -p figures/
	python code/analysis-graphics.py

paper/parcial.pdf: paper/parcial.tex paper/fluxograma.png paper/intro-refs.bib figures/
	tectonic -X compile paper/parcial.tex

clean:
	rm -rf results/previo-*.txt figures/ paper/parcial.pdf
