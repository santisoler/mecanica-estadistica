PROJECT = practica1
LATEX_FLAGS  = -halt-on-error -output-directory $(OUTPUT)/
OUTPUT = output
PDFVIEWER = evince


all: $(PROJECT).tex

clean:
	rm -rf $(OUTPUT)

show: all
	@ ( $(PDFVIEWER) $(OUTPUT)/$(PROJECT).pdf > /dev/null 2>&1 & )


$(PROJECT).tex: $(PROJECT).aux
	pdflatex $(LATEX_FLAGS) $(PROJECT).tex

$(PROJECT).aux: $(OUTPUT)/
	pdflatex $(LATEX_FLAGS) $(PROJECT).tex

$(OUTPUT)/:
	mkdir $(OUTPUT)
