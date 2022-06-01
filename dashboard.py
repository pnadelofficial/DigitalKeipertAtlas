import streamlit as st
import glob
from util import *

geojson_list = []
for file in list(glob.glob('data/*.geojson')):
  geojson_list.append(file)

geo_select = st.radio(
     "Select map",
     geojson_list)

if geo_select == geojson_list[0]:
  poly = openJSON(geojson_list[0])
  fig = plotlyPlot(poly)
  st.plotly_chart(fig, use_container_width=True)
elif: geo_select == geojson_list[1]:
  poly = openJSON(geojson_list[1])
  fig = plotlyPlot(poly)
  st.plotly_chart(fig, use_container_width=True)
elif: geo_select == geojson_list[2]:
  poly = openJSON(geojson_list[2])
  fig = plotlyPlot(poly)
  st.plotly_chart(fig, use_container_width=True)
else:
  poly = openJSON(geojson_list[3])
  fig = plotlyPlot(poly)
  st.plotly_chart(fig, use_container_width=True)