import pandas as pd
import numpy as np


chat_id = 305011093 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    s = np.sum(x)
    estimate = 2 * s / (n * 4**2)
    return estimate
