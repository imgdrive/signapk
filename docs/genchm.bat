@echo off
REM Generate .hhp/.hhc/.hhk
genchm.py

REM Call hhc (html help compiler) to generate .chm
hhc main.hhp