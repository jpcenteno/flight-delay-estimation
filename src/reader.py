'''
Provee funciones para leer los datasets.
'''

from timezonefinder import TimezoneFinder
from pytz import timezone, utc
import datetime as dt

from pathlib import Path

import pandas as pd
import numpy as np

# Path al directorio data/ del proyecto
DATADIR: Path = Path(__file__).parent.absolute() / '../data'

YEARS = list(range(1994, 2008 + 1))


def _parse_dates(df: pd.DataFrame):
    '''
    Devuelve el date para cada fila.
    '''

    dates = pd.to_datetime(df.Year*10000+df.Month*100+df.DayofMonth,format='%Y%m%d')
    return dates


def _parse_datetimes(dates, times):
    '''
    '''
    mins = times % 100.
    hours = np.floor(times / 100)

    day_time_delta = pd.to_timedelta(hours * 60 + mins)
    return dates + day_time_delta


def getpath(year: int) -> Path:
    '''
    Devuelve el Path al dataset especificado.
    '''

    if not ( 1994 <= year <= 2008 ):
        raise ValueError(f'year ({year}) not in range 1994...2008.')

    return DATADIR / f'{year}.csv.bz2'


def read_flights(year: int) -> pd.DataFrame:
    '''
    Lee un dataset del disco. Asume que esta en el directorio data/.
    '''

    # La idea es meter acá todo el pre-procesado que necesiten las columnas del
    # dataset.
    data = pd.read_csv(getpath(year),
                       compression='bz2',
                       encoding='latin1')

    # Fix dates
    data['date'] = _parse_dates(data)
    data.drop(['Year', 'Month', 'DayofMonth'], axis=1, inplace=True)

    return data
