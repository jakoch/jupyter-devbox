# FAQ

## How to reference a Jupyter notebook cell from an external markdown file?

Here are two examples of how to reference a notebook cell from an external markdown file.
The referenced notebook cells are in markdown format and include level 2 headings.

[List Python Packages (check_devbox.ipynb)](../notebooks/check_devbox.ipynb#list-python-packages)

[Get time-series data for USA Gross Domestic Product (FRED/GDP) (finance.ipynb)](../notebooks/finance.ipynb#get-times-series-data-for-usa-gross-domestic-product-fredgdp)

Feel free to explore these examples and let us know if you have any questions!

## Why is my Jupyter Notebook code cell not formatted using Black?

VS Code and Black don’t handle Jupyter notebook cells the same way they handle .py scripts.
Notebook cells sometimes include IPython magic commands (like `%matplotlib inline`),
which are complicated Python syntax. A cell will not be formatted if it
contains code that Black cannot safely interpret as valid, standalone Python.

Black operates without access to a live IPython kernel.
To avoid corrupting notebooks or misformatting code,
it skips cells that may rely on IPython-specific transformations or ambiguous syntax.

If a notebook cell contains IPython magics or syntax that isn’t
guaranteed to be valid Python, Black will leave it untouched by design.

See: https://github.com/psf/black/blob/main/docs/faq.md#why-is-my-jupyter-notebook-cell-not-formatted
