TARGETS = $(shell find . -maxdepth 3 -name '*.tex')

# Name of the directory that will be created and will store the final PDFs
OUTPUT_DIR = _output
LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -cd -halt-on-error -outdir=$(CURDIR)/$(OUTPUT_DIR)


all:
	$(LATEX_COMPILER) $(LATEX_FLAGS) $(TARGETS)

clean:
	rm -r $(OUTPUT_DIR)
