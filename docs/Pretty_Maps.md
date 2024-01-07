# Pretty Maps

I came across this on September 1st 2021. Probably from Hacker News.

As the title implies it allows you to make a pretty map of location from Open StreetMaps data. I'm not sure how the colours work yet.

```python
#!/usr/local/bin/python3

import pprint
import sys

pprint.pprint(sys.path)

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

palette = ['#FFC857', '#E9724C', '#C5283D']


# Init matplotlib figure
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

drawing_kwargs_celtic = {
    #'background':   {'fc': 'palegreen', 'ec': 'white', 'hatch': 'ooo...', 'zorder': -1},
    'perimeter':    {'ec': 'green', 'fill': False, 'lw': 0},
    'park':         {'fc': 'darkgreen', 'ec': 'white', 'lw': 0, 'zorder': 1, 'hatch': 'ooo...'},
    'grass':        {'fc': 'lawngreen', 'ec': 'white', 'lw': 0, 'zorder': 1, 'hatch': 'ooo...'},
    'wetland':      {'fc': 'lightgreen', 'ec': 'white', 'lw': 0, 'zorder': 3, 'hatch': 'ooo...'},
    'water':        {'fc': 'darkblue', 'ec': 'blue', 'lw': 0, 'zorder': 2, 'hatch': 'ooo...'},
    'beach':        {'fc': 'orange', 'ec': 'white', 'lw': 0, 'zorder': 2, 'hatch': 'ooo...'},
    'pedestrian':   {'fc': 'white', 'ec': 'white', 'lw': 0, 'zorder': 2, 'hatch': 'ooo...'},
    'streets':      {'fc': 'darkgrey', 'ec': 'grey', 'zorder': 3, 'lw': 0, 'hatch': 'ooo...'},
    'building':     {'fc': 'green', 'ec': 'white', 'lw': 0, 'zorder': 0},
},



address='Kurihama Station',
address="nissan stadium, japan"
address="Building #378180100"
address="celtic park"
address="mitsuzawa stadium"

backup = plot(
    # Address:
    # 'Praca Ferreira do Amaral, Macau',
    address,
    # Plot geometries in a circle of radius:
    radius = 1100,
    # Matplotlib axis
    ax = ax,
    # Which OpenStreetMap layers to plot and their parameters:
    layers = {
            # Perimeter (in this case, a circle)
            'perimeter': {},
            # Streets and their widths
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                }
            },
            # Other layers:
            #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
        },
        # drawing_kwargs:
        #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
        drawing_kwargs = {
            'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        }
        #drawing_kwargs = {
        #    'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
        #    'park': {'fc': '#AABD8C', 'ec': '#87996b', 'lw': 1, 'zorder': 1},
        #    'forest': {'fc': '#78A58D', 'ec': '#658a76', 'lw': 1, 'zorder': 1},
        #    'garden': {'fc': '#a9d1a9', 'ec': '#8ab58a', 'lw': 1, 'zorder': 1},
        #            'water': {'fc': '#92D5F2', 'ec': '#6da8c2', 'lw': 1, 'zorder': 2},
        #     'streets': {'fc': '#F1E6D0', 'ec': '#2F3737', 'lw': 1.5, 'zorder': 3},
        #     'building': {'palette': palette, 'ec': '#2F3737', 'lw': 1, 'zorder': 4},
        # },

)

fig.savefig(address)

```
