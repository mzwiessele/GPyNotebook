'''
Created on Mar 27, 2015

@author: maxz
'''
from GPyNotebook.plotting.plot import Plot, LabelDictPlot

class Legend(Plot):
    def __init__(self, plot, figsize=None, figtype=None, *args, **kwargs):
        super(Legend, self).__init__(*args, **kwargs)
        assert isinstance(plot, LabelDictPlot)
        self.plot = plot
    
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