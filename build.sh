#!/bin/zsh

pandoc --standalone \
    --smart \
    --write=dzslides \
    --output=presentation.html \
    --template=template.html \
    --css=style.css \
    00_about.md \
    01_rest.md \
    02_whyDRF.md \
    03_basic_start.md \
    04_specify_resources.md \
    05_nested_resources.md \
    06_mixins.md