#!/bin/sh

cp /app/start.ipynb $SCRATCH/start.ipynb
jupyter notebook --browser=/ff/bin/firefox/firefox $SCRATCH/start.ipynb
