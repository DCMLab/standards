## RestructuredText to LaTeX

The file `reference.rst` is written so that it can be included in my dissertation. Currently,
this is achieved using the command

```bash
pandoc -t latex --pdf-engine lualatex -o /home/laser/git/diss/22_standards/reference.tex --extract-media /home/laser/git/diss/22_standards/img  reference.rst
```