'''
Created on Mar 27, 2015

@author: maxz
'''
from IPython.html.widgets.widget_selection import Dropdown
from collections import OrderedDict

class DimSelect(Dropdown):
    def __init__(self, input_dim, *args, **kwargs):
        _r = range(input_dim)
        if 'options' in kwargs:
            raise ValueError("options are being created automaticalle, use Dropdown if you want to create your own Dropdown")
        super(DimSelect, self).__init__(options=OrderedDict(((str(_), _) for _ in _r)), *args, **kwargs)