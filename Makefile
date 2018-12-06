TARGETS = $(subst /,,$(subst ./,,$(dir $(shell find . -maxdepth 2 -name '*.tex'))))
OUTPUT = _build
TARGETS_OUTPUT = _output
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
