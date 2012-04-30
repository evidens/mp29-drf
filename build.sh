#!/bin/zsh

pandoc -s -i \
    -t dzslides \
    -o presentation.html \
    00_about.md \
    01_rest.md \
    02_whyDRF.md \
    03_basic_start.md \
    04_specify_resources.md \
    05_nested_resources.md \
    06_mixins.md