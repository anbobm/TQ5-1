# Dokumentations-Webseite mit sphinx erstellen

1. `pip install sphinx`
1. `/docs` Ordner anlegen und in Konsole öffnen
1. `sphinx-quickstart` ausführen
1. `conf.py` am Anfang mit folgendem ergänzen:
    ```
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    ```
    Außerdem extensions ergänzen:
    ```
    extensions = [
    'sphinx.ext.autodoc',      # pull docstrings
    'sphinx.ext.napoleon',     # Google/NumPy style support
    'sphinx.ext.viewcode',     # add source code links
    ]
    ```
1. Übergeordneten Ordner öffnen und `sphinx-apidoc -o .\docs\ .` ausführen
1. `docs\index.rst` ändern zu:
    ```
    Welcome to My Project
    ====================
    
    .. toctree::
       :maxdepth: 2
    
       modules
    ```
1. `sphinx-build -b html docs .\docs\_build\html` ausführen
1. `\docs\_build\html` öffnen und `python -m http.server 8080` ausführen und Webseite `localhost:8080` aufrufen