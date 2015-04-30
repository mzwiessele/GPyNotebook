'''
Created on Mar 27, 2015

@author: maxz
'''
from GPyNotebook.plotting.legend import Legend
from GPyNotebook.plotting.scatter import Scatter
from IPython.html.widgets.widget_box import Box, HBox, FlexBox
from GPyNotebook.controls.select import DimSelect
from IPython.html.widgets.widget_selection import Dropdown

class LatentView(Box):
    def __init__(self, X, lab_dict, dim_names=None, colors=None, markers=None, figsize=None, figtype=None, *a, **kw):
        self.scatter = Scatter(X, lab_dict, colors, markers, figsize, figtype)
        self.legend = Legend(self.scatter)
        self.input_dim = X.shape[1]
        self.lab_dict = lab_dict
        
        dx, dy, dl = cntrls = self._controls(dim_names)
        
        kw['children'] = [
                          HBox(children=cntrls), 
                          FlexBox(children = [self.scatter, self.legend], margin=0, orientation='horizontal')
                          ]
        
        kw['orientation'] = 'vertical'

        dx.on_trait_change(self.scatter.change_x_dim, 'value')
        dy.on_trait_change(self.scatter.change_y_dim, 'value')
        dl.on_trait_change(self.scatter.change_labels, 'value')
        #dl.on_trait_change(lab_up_html(html_show, labs, cs, ''), 'value')
        dl.on_trait_change(self.legend.update_legend, 'value')

        super(LatentView, self).__init__(*a, **kw)
        
    def _controls(self, names=None):
        if names is not None:
            v1, v2 = names[:2]
        else:
            v1, v2 = 0, 1
        return (DimSelect(self.input_dim, names, value=v1, description='x'),
                DimSelect(self.input_dim, names, value=v2, description='y'),
                Dropdown(options=self.lab_dict.keys(), description='labels')
                )
        