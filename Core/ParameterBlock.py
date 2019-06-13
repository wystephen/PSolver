import numpy as np
import scipy as sp


class ParameterBlockBase:
    def __init__(self, local_size: int,
                 global_size: int,
                 initial_value: np.ndarray = np.zeros(1)):
        self.local_size = local_size
        self.global_size = global_size
        self.value = initial_value


    def Plus(self, p_v: np.ndarray) -> np.ndarray:
        self.value += p_v

    def
