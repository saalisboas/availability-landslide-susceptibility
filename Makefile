# alvo: dependencias
#	comando

results/: code/searching.py data/
	mkdir -p results/
	python code/searching.py > results/previo-PAIS?.txt 
