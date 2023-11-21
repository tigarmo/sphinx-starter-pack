from pathlib import Path


def setup(app):
    app.add_html_theme("canonical_sphinx_theme", Path(__file__).parent)
