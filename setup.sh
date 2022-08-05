#! /usr/bin/bash

export $(grep -v '^#' .env | xargs)
python3 -c "import runner; runner._buildadhocvars()"