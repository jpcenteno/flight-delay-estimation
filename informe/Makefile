
# Comandos sacados de los consejos del template.
# usar latex -> dvips -> ps2pdf
# en vez de pdflatex

#.PHONY: clean

#all: clean
all: informe.pdf clean

#%.dvi: %.tex
#	latex $<
#	bibtex informe
#	latex $< # dos veces para las referencias

#%.ps: %.dvi
#	dvips $<

%.pdf: %.tex
	@echo "Suele fallar, si no anda correr a mano"
	@echo "pdflatex $<"
	@echo "bibtex informe"
	@echo "pdflatex $<"
	pdflatex $<
	bibtex informe
	pdflatex $<

clean:
	-rm *.blg
	-rm *.bbl
	-rm *.log
	-rm *.out
	-rm *.aux
	-rm *.dvi

clean-all: clean
	-rm *.pdf
