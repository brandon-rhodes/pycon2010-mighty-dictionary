
#presentation.pdf: presentation.html
#	wkhtmltopdf presentation.html presentation.pdf

PYTHON := PYTHONPATH=/home/brandon/dictvis python
SVGs := $(wildcard figures/*.svg)
PNGs := $(addsuffix .png, $(basename $(SVGs)))

all: presentation.html $(PNGs) figures

presentation.html: presentation.rst bin/wrap_slides.py
	rst2s5.py $< > $@
	bin/wrap_slides.py $@

$(PNGs): %.png: %.svg
	inkscape -e $@ $<

figures: figures/average_probes.png
figures/average_probes.png: figures/average_probes.py figures/average_probes_data.txt
	/usr/bin/python figures/average_probes.py figures/average_probes.png

figures/average_probes_data.txt: figures/average_probes_data.py
	$(PYTHON) $< $@
