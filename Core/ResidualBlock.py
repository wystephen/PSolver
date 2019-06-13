
import numpy as np
import scipy as sp

from Core.ParameterBlock import *

class ResidualBlock:
    def __init__(self, func_dim:int =0,
                 para_name_list:list = list()):
        self.func_dim:int = func_dim
        self.func_index:int = -1

        self.para_name_list = para_name_list #type List[str]

    def cal_func(self,
                 val_list:list())->np.ndarray:
        return NotImplementedError

    def cal_jac(self,
                val_list:list)->np.ndarray:
        return NotImplementedError


