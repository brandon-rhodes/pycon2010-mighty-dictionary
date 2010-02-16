
#presentation.pdf: presentation.html
#	wkhtmltopdf presentation.html presentation.pdf

PYTHON := PYTHONPATH=/home/brandon/dictvis /usr/bin/python
SVGS := $(wildcard figures/*.svg)
PNGS := $(addsuffix .png, $(basename $(SVGS)))

all: presentation.html $(PNGS) all_figures

test:
	bin/test

presentation.html: presentation.rst bin/wrap_slides.py
	rst2s5.py $< > $@
	bin/wrap_slides.py $@

$(PNGs): %.png: %.svg
	inkscape -e $@ $<

# Both figures and data files are built by corresponding Python scripts
# of the same name.

FIGURE_SCRIPTS := $(filter-out figures/_dictdraw.py, $(wildcard figures/*.py))
FIGURES := $(addsuffix .png, $(basename $(FIGURE_SCRIPTS)))

all_figures: $(FIGURES)
$(FIGURES): %.png: %.py
	$(PYTHON) $*.py $*.png

$(filter figures/insert% figures/collide% figures/words%, $(FIGURES)): \
  figures/_dictdraw.py

DATA_SCRIPTS := $(wildcard data/*.py)
DATA_FILES := $(addsuffix .txt, $(basename $(DATA_SCRIPTS)))

$(DATA_FILES): %.txt: %.py
	$(PYTHON) $< $@

# Dependencies of figures on their data files.

figures/average_probes.png: data/average_probes.txt
figures/average_time.png: data/average_probes.txt
