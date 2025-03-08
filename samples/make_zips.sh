#!/bin/sh

zip sample_game.zip -du -x "**/*.pyc" -x "**/poetry.lock" -x "**/__pycache__/*" -x "**/.mypy_cache/*" -r ./sample_game
