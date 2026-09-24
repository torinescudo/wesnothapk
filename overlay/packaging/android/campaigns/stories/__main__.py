"""Run the story checks: `python -m stories [--strict]`."""
import sys

from . import main

sys.exit(main(sys.argv[1:]))
