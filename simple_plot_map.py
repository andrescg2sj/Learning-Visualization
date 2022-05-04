#
# Andrés González SJ
# https://github.com/andrescg2sj
#

import plotly.graph_objs as go
from plotly.offline import plot


state_codes = ["AL", "AK", "AZ", "AR", "CA",
               "CO", "CT", "DE", "DC", "FL",
               "GA", "HI", "ID", "IL", "IN",
               "IA", "KS", "KY", "LA", "ME",
               "MD", "MA", "MI", "MN", "MS",
               "MO", "MT", "NE", "NV", "NH",
               "NJ", "NM", "NY", "NC", "ND",
               "OH", "OK", "OR", "PA", "RI",
               "SC", "SD", "TN", "TX", "UT",
               "VT", "VA", "WA", "WV", "WI", "WY"]
values = [3, 5, 2, 4, 9,
          10, 0, 3, 5, 7,
          3, 6, 5, 5, 5,
          6, 1, 4, 3, 9,
          8, 3, 9, 2, 7,
          5, 9, 4, 9, 2,
          6, 6, 6, 5, 8,
          7, 3, 10, 1, 8,
          8, 6, 8, 4, 10,
          4, 0, 7, 2, 2, 6]

data = dict(type='choropleth',
    locations=state_codes,
    locationmode='USA-states',
    text=state_codes,
    z=values,
    colorscale="Plasma"
)
#For other color scales, see:
# https://plotly.com/python/builtin-colorscales/#builtin-sequential-color-scales


layout = dict(geo = dict(scope='usa',
                        showlakes= False),
                  title="Some measure"
            )

choromap = go.Figure(data=[data], layout=layout)


#This should launch a web browser and show the map on it.
plot(choromap)

#Write the map to disk    
choromap.write_html("example_map.htm")
    


