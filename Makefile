# alvo: dependencias
#	comando

.PHONY: clean

results/: code/searching.py data/
	mkdir -p results/
	python code/searching.py > results/previo-br.txt 

figures/: code/analysis-graphics.py results/br-articles-open.txt results/br-articles-request.txt
	mkdir -p figures/
	python code/analysis-graphics.py

clean:
	rm -rf results/previo-*.txt figures/
