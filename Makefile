# List directories that have tex files inside
TARGETS = $(subst /,,$(subst ./,,$(dir $(shell find . -maxdepth 2 -name '*.tex'))))
# Name of the directory that will be created and will store the final PDFs
OUTPUT = _output
# Name of the subdirectories inside TARGETS that store each PDF file
TARGETS_OUTPUT = _output
# List all final PDFs files
PDFS = $(addprefix $(OUTPUT)/, $(addsuffix .pdf, $(TARGETS)))

all: $(PDFS)

$(OUTPUT)/%.pdf: % | $(OUTPUT)/
	make -C $<
	mv $</$(TARGETS_OUTPUT)/$<.pdf $(OUTPUT)

$(OUTPUT)/:
	mkdir $(OUTPUT)

clean:
	$(foreach target, $(TARGETS), make -C $(target) clean;)
	rm -r $(OUTPUT)
