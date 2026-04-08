# Docstrings

Der erste (im allgemeinen mehrzeilige) String innerhalb eines Moduls, einer Klasse, einer Methode oder einer Funktion hat eine spezielle Bedeutung: er ist ein **Docstring** (documentation string), der das Modul/die Klasse/etc. dokumentiert.

Grundsätzlich sehen diese so aus:

```python
"""Zusammenfassung
(Leerzeile)
Optional längerer Beschreibungstext
.
.
.
"""
```

Außerdem gibt es verschiedene Konventionen, die wie immer nicht verpflichtend sind:

## Google Style

```python
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b
```

## NumPy style

```python
def add(a: int, b: int) -> int:
    """Add two numbers.

    Parameters
    ----------
    a : int
        First number.
    b : int
        Second number.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b
```