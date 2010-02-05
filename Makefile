
#presentation.pdf: presentation.html
#	wkhtmltopdf presentation.html presentation.pdf

PYTHON := PYTHONPATH=/home/brandon/dictvis python
SVGS := $(wildcard figures/*.svg)
PNGS := $(addsuffix .png, $(basename $(SVGS)))

all: presentation.html $(PNGS) figures

presentation.html: presentation.rst bin/wrap_slides.py
	rst2s5.py $< > $@
	bin/wrap_slides.py $@

$(PNGs): %.png: %.svg
	inkscape -e $@ $<

FIGURE_SCRIPTS := $(wildcard figures/*.py)
FIGURES := $(addsuffix .png, $(basename $(FIGURE_SCRIPTS)))

figures: $(FIGURES)
$(FIGURES): %.png: %.py
	/usr/bin/python $*.py $*.png

figures/average_probes.png: figures/average_probes_data.txt
figures/average_time.png: figures/average_probes_data.txt
figures/average_probes_data.txt: figures/average_probes_data.py
	$(PYTHON) $< $@
