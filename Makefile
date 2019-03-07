# Search for .tex files to be compiled
TARGETS = $(shell find . -maxdepth 3 -name '*.tex')
# Name of the directory that will be created and will store the final PDFs
OUTPUT_DIR = _output
# LaTeX compiler (we will use latexmk for simplicity)
LATEX_COMPILER = latexmk
# Flags for latexmk. Must specify abspath of outdir when using -cd option.
LATEX_FLAGS = -pdf -cd -halt-on-error -outdir=$(CURDIR)/$(OUTPUT_DIR)


all:
	$(LATEX_COMPILER) $(LATEX_FLAGS) $(TARGETS)

clean:
	rm -r $(OUTPUT_DIR)
