
#presentation.pdf: presentation.html
#	wkhtmltopdf presentation.html presentation.pdf

SVGs := $(wildcard figures/*.svg)
PNGs := $(addsuffix .png, $(basename $(SVGs)))

all: presentation.html $(PNGs)

presentation.html: presentation.rst
	rst2s5.py $< > $@

$(PNGs): %.png: %.svg
	inkscape -e $@ $<
