# Architecture

`main.py` is the whole program. It takes one argument, a CSV file or a directory of them, and defaults to `./trips/`.

For each CSV it prints four tables with `tabulate`:

- Counts of base, worn and food items.
- Weight in pounds, converted from the grams in the file.
- Cost.
- A per-category breakdown of count, weight and cost.

Rows missing a quantity or a weight or price are left out of the totals, and the script prints how many.

`trips/` holds example exports in the LighterPack CSV format. The README documents the columns.

The Dockerfile starts from a pinned `python` image, installs `tabulate`, copies `main.py` and `trips/`, and runs `python main.py`.
