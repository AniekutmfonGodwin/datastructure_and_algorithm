start:
	python main.py


shell:
	python -i main.py


run-doc:
	pdoc --http localhost:8080 binary_tree.py