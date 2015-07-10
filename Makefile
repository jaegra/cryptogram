PYTHON=python2

default: auden.crypt.pdf

%.crypt.txt: %.txt crypt.py
	$(PYTHON) crypt.py <$< >$@

%.crypt.ps: %.crypt.txt
	a2ps -1r -f 12 -o $@ $<

%.pdf: %.ps
	ps2pdf $<
