PROJECT = practica2
LATEX_FLAGS  = -halt-on-error -output-directory $(OUTPUT)/
OUTPUT = output


all: $(PROJECT).tex

clean:
	rm -rf $(OUTPUT)	


$(PROJECT).tex: $(PROJECT).aux
	pdflatex $(LATEX_FLAGS) $(PROJECT).tex

$(PROJECT).aux: $(OUTPUT)/
	pdflatex $(LATEX_FLAGS) $(PROJECT).tex

$(OUTPUT)/:
	mkdir $(OUTPUT)
