#!/bin/bash

pdflatex informe.tex
bibtex informe
pdflatex informe.tex
