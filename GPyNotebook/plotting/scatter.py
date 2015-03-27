'''
Created on Mar 27, 2015

@author: maxz
'''
import seaborn as sns
import itertools
from GPyNotebook.util import lim
from GPyNotebook.plotting.plot import LabelDictPlot


class Scatter(LabelDictPlot):
    def __init__(self, X, lab_dict, colors=None, markers=None, figsize=(4,3), figtype=None, *args, **kwargs):
        """
        if colors is a string, we call sns.color_palette(colors, size(labels)) as the colors.
        """
        super(Scatter, self).__init__(lab_dict, figsize, figtype, *args, **kwargs)

        self.X = X
        self.xdim, self.ydim = 0, 1

        if colors is None:
            colors = sns.color_palette()
        self.colors = colors
        if markers is None:
            markers = '<>sdo'
        self.markers = markers

        self.ax.set_xlabel('Dimension {}'.format(self.xdim))
        self.ax.set_ylabel('Dimension {}'.format(self.ydim))
        self.labels_updated()
        self.redraw()
        
    def redraw(self):
        #self.value='Loading...'
        x, y = self.X[:, self.xdim], self.X[:, self.ydim]
        for l, s in zip(self.ulabels, self.scatters):
            f = self.labels==l
            s.set_data(x[f], y[f])
        
        self.ax.set_xlim(lim(x))
        self.ax.set_ylim(lim(y))
        self.draw()
    
    def labels_updated(self):
        #self.value = 'Loading...'
        for _ in range(len(self.ax.lines)):
            self.ax.lines[0].remove()
        self.scatters = []
        
        if isinstance(self.colors, str):
            c = iter(sns.color_palette(self.colors, self.ulabels.size))
        else:
            c = itertools.cycle(self.colors)
        
        m = itertools.cycle(self.markers)
        for l in self.ulabels:
            self.scatters.extend(self.ax.plot([], [], marker=m.next(), markeredgecolor='none', ls='', markerfacecolor=c.next(), alpha=.7, label=l))
        self.redraw()
                
    def change_x_dim(self, name, old, new):
        self.xdim = new
        self.ax.set_xlabel('Dimension {}'.format(self.xdim))
        self.redraw()    

    def change_y_dim(self, name, old, new):
        self.ydim = new
        self.ax.set_ylabel('Dimension {}'.format(self.ydim))
        self.redraw()
