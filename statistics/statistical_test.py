from typing import List
from scipy.stats import rayleigh, kstest

def get_params(data:List):
    params = rayleigh.fit(data)
    return params

def get_ks_statistic(data:List,params:List):
    stat, p_value = kstest(data, 'rayleigh', args=params)
    return stat, p_value