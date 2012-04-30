#!/bin/zsh

pandoc --standalone \
    --smart \
    --write=dzslides \
    --output=presentation.html \
    --template=template.html \
    --css=style.css \
    slides/*