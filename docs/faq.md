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

## Spellchecker

### Disabling cSpell

The dev container installs the Code Spell Checker extension (streetsidesoftware.code-spell-checker),
which is also known as CSpell, see `.devcontainer\devcontainer.json`.
But it doesn't configure this extension in any way.

This means that the extension uses default settings, which enables
spell checkings for file types like Markdown and Python and display warnings inline.

You can disable the checking of the Python code easily:

Open VS Code’s Command Palette `Command Palette... (Ctrl+Shift+P)`,
then run run `^Spell: Open Spell Checker Settings`.
Or click the `{}` icon in the bottom status bar of VSCode.

In settings, find `@ext:streetsidesoftware.code-spell-checker enabledFileTypes`
and remove "Python" from the list or set it to false.

That should clear up any spellchecker warning.

This is also covered in the official extension documentation:
https://streetsidesoftware.com/vscode-spell-checker/#enable--disable-file-types

Of course, you could disable the whole extension by setting `cSpell.enabled` to false.

### Configuring cSpell

Of course, you can configure this extension to fit your needs.
To get started, you could add a `cspell.json` to the project root.
Then configure which files to include or exclude, add words to ignore
list and you can also setup custom dictionaries for domain-specific vocab,
like science/tech/math terms.

