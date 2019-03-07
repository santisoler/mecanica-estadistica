# Search for .tex files to be compiled
TARGETS = $(shell find . -name '*.tex')
# Name of the directory that will be created and will store the final PDFs
OUTPUT = _output
# Name of the subdirectories inside TARGETS that store each PDF file
TARGETS_OUTPUT = _output


all: build

build: $(OUTPUT)
	@ ( $(foreach TEX,$(TARGETS),make -C $(shell dirname $(TEX)) all;) )
	@ ( $(foreach TEX,$(TARGETS),mv $(shell dirname $(TEX))/$(TARGETS_OUTPUT)/*.pdf $<;) )

clean:
	rm -r $(OUTPUT)

$(OUTPUT):
	mkdir $(OUTPUT)

