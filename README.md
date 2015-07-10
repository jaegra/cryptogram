# Cryptogram

This is a simple Python script to generate random single-substitution
cryptograms from text files. I use it to generate exercises for a CS0 course,
in a unit about crypto. We work through one in class, and then each student
gets their own puzzle to solve as part of an assignment.

I've included a sample poem, *Stop all the clocks,* by W.H. Auden. I have
collected ten or so others of similar length, but I don't want a repository of
the solutions to be found easily. :)

## Usage

If you have the right tools, you can generate `auden.crypt.pdf` by typing
`make`. The script currently assumes Python 2, so if you don't have it
installed as `python2` like I do, try:

```
make PYTHON=python
```

The Makefile also assumes `a2ps` to convert the text to Postscript, and then
`ps2pdf` for PDF.

Here's an example of the output for the Auden poem -- but each time you run, it
selects a different cipher.

```
CKYL VQQ KSB ZQYZOC, ZIK YDD KSB KBQBLSYAB,

LHBRBAK KSB WYM DHYG XVHOEAM FEKS V UIEZT XYAB,

CEQBAZB KSB LEVAYC VAW FEKS GIDDQBW WHIG

XHEAM YIK KSB ZYDDEA, QBK KSB GYIHABHC ZYGB. 
````
