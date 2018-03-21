TARGETS = practica1 practica2 practica3 repaso-termodinamica

all: _build/$(TARGETS)

_build/$(TARGETS): _build
		$(foreach target, $(TARGETS), make -C $(target);)
		$(foreach target, $(TARGETS), mv $(target)/output/*.pdf _build;)

_build:
		mkdir _build

clean:
		$(foreach target, $(TARGETS), make -C $(target) clean;)
		rm -r _build
