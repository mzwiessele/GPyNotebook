'''
Created on Mar 27, 2015

@author: maxz
'''
from GPyNotebook.plotting.plot import Plot, LabelDictPlot

class Legend(Plot):
    def __init__(self, plot, figsize=None, figtype=None, *args, **kwargs):
        assert isinstance(plot, LabelDictPlot)
        if figsize is None:
            figsize = (1, plot.figsize[1])
        super(Legend, self).__init__(figsize, figtype, *args, **kwargs)
        self.plot = plot
        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)
        self._redraw()
    
    def update_legend(self, name, old, new):
        self._redraw()
    
    def _redraw(self):
        self.value = """
<p>Loading...</p>
"""
        c=r=1
        while c*r < self.plot.ulabels.size:
            if c==r or r==(c+1):
                r+=1
            elif r==(c+2):
                c+=1
                r-=1
        self.ax.legend(*self.plot.ax.get_legend_handles_labels(), 
                       frameon=False,
                       #mode='expand',
                       ncol=c,
                      handletextpad=0,
                      bbox_to_anchor=(0,.5),loc='center')
        self.draw()