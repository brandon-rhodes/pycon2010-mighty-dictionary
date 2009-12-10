
#presentation.pdf: presentation.html
#	wkhtmltopdf presentation.html presentation.pdf

presentation.html: presentation.rst
	rst2s5.py $< > $@
