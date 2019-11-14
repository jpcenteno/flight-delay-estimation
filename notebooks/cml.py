from cml_cpp import *

from functools import partial # This convenience func preserves name and docstring

import pandas as pd

def wrap_method(cls):
    """Falopa: para wrappear métodos a una clase con un annotation en vez
    de usar setattr directamente. En lisp (al menos elisp) esto se
    hace a menudo, aunque sin clases. Se llaman advices. En otros
    lenguajes creo que se llama aspect programming... está bueno,
    quien carajo quiere definir clases si podés modificar los métodos
    en runtime XD
    """
    def wrapper(func):
        wrapped=getattr(cls, func.__name__)
        setattr(cls, func.__name__, partial(func, wrapped))

    return wrapper


for clazz in [normal_equations_solver, svd_solver, qr_solver, qr_col_pivot_solver, qr_full_pivot_solver]:
    @wrap_method(clazz)
    def lstsq(f, A, b):
        if isinstance(b, pd.DataFrame):
            return f(A, b.value)
        else:
            return f(A, b)
