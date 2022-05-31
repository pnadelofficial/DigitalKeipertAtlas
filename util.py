import plotly.graph_objects as go
import json
import pandas as pd
import numpy as np

def openJSON(file_path):
  with open(file_path) as f:
    poly = json.load(f)
  return poly

def plotlyPlot(poly):
  avg_points = []
  for feature in poly['features']:
    if feature['geometry']['type'] == 'MultiPolygon':
      avg_points.append(pd.Series(feature['geometry']['coordinates']).apply(lambda x: np.mean(np.array(x[0]), axis = 0)).mean())
    else:
      avg_points.append(pd.Series(feature['geometry']['coordinates']).apply(lambda x: np.mean(np.array(x), axis = 0)).mean())
  avg_points = np.array(avg_points)
  avg_point = np.mean(avg_points, axis=0)

  fig = go.Figure(go.Scattermapbox(
    mode = "markers",
    marker = {'size': 20, 'color': ["cyan"]}))

  fig.update_layout(
      mapbox = {
          'style': "stamen-terrain",
          'center': { 'lon': float(avg_point[0]), 'lat': float(avg_point[1])},
          'zoom': 3, 'layers': [{
              'source':
                  poly,
              'type': "fill", 'below': "traces", 'color': "royalblue"}]},
      margin = {'l':0, 'r':0, 'b':0, 't':0})
  
  return fig