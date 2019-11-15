'''
Provee funciones para la evaluación de modelos.
'''

def nrmse(y_true, y_pred):
    '''
    Devuelve el _Normalized Root Mean Square Error_ (NRMSE) entre `y_true` y
    `y_pred`.
    '''

    y_min = y_true.min()
    y_max = y_true.max()
    y_span = y_max - y_min

    mse = mean_squared_error(y_true, y_pred)

    return np.sqrt( mse / y_span**2 )
