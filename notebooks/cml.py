from cml_cpp import *

from functools import partial # This convenience func preserves name and docstring

import numpy as np
import pandas as pd

import math

from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, make_scorer

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


class Predictor:
    def fit(self, X_train, y_train, **fit_params):
        A = np.stack(X_train)
        self.coefs = np.linalg.solve(A.T@A, A.T@y_train)

    def predict(self, pred_set):
        arrays = self.get_x_vals(pred_set)
        full_A = np.stack(arrays)
        return full_A@self.coefs

class LinealRegression(Predictor):
    def get_x_vals(self, x):
        x_vals = []
        for i in range(len(x)):
            row = np.array([i, 1])
            x_vals.append(row)
        return x_vals

class lsqPredictor(Predictor):
    def __init__(self, phases, freqs, max_grade):
        self.phases = phases
        self.freqs = freqs
        self.max_grade = max_grade

    def get_params(self, deep=True):
        """función necesaria para que sklearn lo trate como un estimador. Se puede usar en cross validations & shit"""
        pars={}
        pars["phases"] = self.phases
        pars["freqs"] = self.freqs
        pars["max_grade"] = self.max_grade
        return pars

    def set_params(self, pars):
        """función necesaria para que sklearn lo trate como un estimador. Se puede usar en cross validations & shit"""
        self.phases =    pars["phases"]
        self.freqs =     pars["freqs"]
        self.max_grade = pars["max_grade"]

    def trig_vals(self, t):
        return  [math.sin(2 * math.pi / f * t + p) for f in self.freqs for p in self.phases]

    def get_x_vals(self, x):
        x_vals = []
        for i in range(len(x)):
            row = np.array([i**p for p in range(self.max_grade+1)] + self.trig_vals(i), dtype='float')
            x_vals.append(row)
        return x_vals


def cross_val_timeline_scores_with_splits(lsq, data, splits):
    """Corre un cross validation, tomando varios cortes y prediciendo
    siempre el futuro (i.e los datos de training siempre son
    anteriores a los de tests. Cubre todo el dominio de data.
    Para más info ver:

    https://scikit-learn.org/stable/modules/cross_validation.html
    https://scikit-learn.org/stable/modules/model_evaluation.html

    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html

    https://hub.packtpub.com/cross-validation-strategies-for-time-series-forecasting-tutorial/"""

    tscv = TimeSeriesSplit(n_splits=splits)
    scores = cross_val_score(lsq, lsq.get_x_vals(data), data, \
                             cv = tscv, scoring=make_scorer(mean_squared_error))
    return scores
