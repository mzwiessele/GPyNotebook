'''
Created on Mar 27, 2015

@author: maxz
'''
from IPython.html.widgets import HTML
import matplotlib.pyplot as plt, numpy as np
from IPython.core.pylabtools import print_figure
from matplotlib.axis import Axis

class Plot(HTML):
    def __init__(self, figsize=None, figtype=None, *args, **kwargs):
        """
        A simple plot, holding a figure and an axis, freely adjustable.
        
        Properties:
            ax: the axis object to draw in
            fig: the figure corresponding to the axis
            draw(): render the figure in its current state
        """
        super(Plot, self).__init__(*args, **kwargs)
        fig, ax = plt.subplots(figsize=figsize)
        self.figsize=figsize
        self.ax = ax
        self.fig = ax.figure
        plt.close(fig)
        self.figtype = figtype or 'svg'
        
    def draw(self):
        """
        Render the updated plot to the HTML output.
        """
        self.value = print_figure(self.fig, self.figtype)
        
        
class LabelDictPlot(Plot):
    def __init__(self, lab_dict, figsize=None, figtype=None, *a, **k):
        """
        A plot with label support, if lab_dict is a collection with labels, we will only use the one. 
        """
        super(LabelDictPlot, self).__init__(figsize, figtype, *a, **k)
        if not isinstance(lab_dict, dict):
            lab_dict = dict(default=lab_dict)
        self._lab_dict = lab_dict
        self._update_to_name(lab_dict.keys()[0])
        
    def _update_to_name(self, new):
        self.labels = self.lab_dict[new]
        self.ulabels = np.unique(self.labels)
    
    def labels_updated(self):
        """
        This function needs to be overwritten by inheriting classes. 
        It makes sure the plot gets updated, and calls self.draw() when finished updating the plot.
        """
        raise NotImplementedError('Abstract super class.')
        
    def change_labels(self, name, old, new):
        """
        trait update function, to be called with the dictionary key of which the labels should be updated to.
        """
        self._update_to_name(new)
        self.labels_updated()