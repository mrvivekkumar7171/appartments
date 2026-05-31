from scipy.stats import gaussian_kde
import plotly.figure_factory as ff
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import pickle

st.set_page_config(
    page_title="Apartment Analytics Report",
    page_icon="👋"
    )
# st.title('Analytics')
new_df = pd.read_csv('A:/CODES/PROJECTS/appartments/models/data_viz1.csv')
feature_text = pickle.load(open('A:/CODES/PROJECTS/appartments/models/feature_text.pkl','rb'))


st.header('Scatter Plot on Geo Map')
group_df = new_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]
fig = px.scatter_map(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
    zoom=10, color_continuous_scale=px.colors.cyclical.IceFire, map_style="open-street-map", width=1200, height=700,
    hover_name=group_df.index, title='Price per Sq ft Sector-wise', labels={"price_per_sqft": "Price Per Sqft"}
)

st.plotly_chart(fig, width='stretch')


st.header('Word Cloud')
wordcloud = WordCloud(width = 800, height = 800, background_color ='black', stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text) # Feature Word Cloud
fig_wc = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig_wc)


st.header('Scatter Plot')
property_type = st.selectbox('Select Property Type', ['All', 'Flat', 'House'])
if property_type == 'All':
    fig1 = px.scatter(new_df, x="built_up_area", y="price", color="bedRoom", title="Area Vs Price",
    labels={"built_up_area": "Built Up Area", "price": "Price", "bedRoom": "Bed Room"})
    st.plotly_chart(fig1, width='stretch')
elif property_type == 'House':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price",
    labels={"built_up_area": "Built Up Area", "price": "Price", "bedRoom": "Bed Room"})
    st.plotly_chart(fig1, width='stretch')
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price",
    labels={"built_up_area": "Built Up Area", "price": "Price", "bedRoom": "Bed Room"})
    st.plotly_chart(fig1, width='stretch')


st.header('Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')
selected_sector = st.selectbox('Select Sector', sector_options)
if selected_sector == 'Overall':
    fig2 = px.pie(new_df, names='bedRoom', title='BHK Distribution in Overall Sectors')
    st.plotly_chart(fig2, width='stretch')
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom', title=f'BHK Distribution in {selected_sector} Sector')
    st.plotly_chart(fig2, width='stretch')


st.header('Box Plot')
fig3 = px.box(new_df[new_df['bedRoom'] <= 4],
    x='bedRoom',
    y='price',
    title='BHK Price Range',
    labels={"bedRoom": "Bed Room", "price": "Price"}
)
st.plotly_chart(fig3, width='stretch')


st.header('Distplot with KDE')
flat_data = new_df[new_df['property_type'] == 'flat']['price'].dropna()
house_data = new_df[new_df['property_type'] == 'house']['price'].dropna()
x_range = np.linspace(-5, 35, 500)
kde_flat = gaussian_kde(flat_data)
kde_house = gaussian_kde(house_data)

fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=flat_data, histnorm='probability density', name='Flat', opacity=0.6, marker_color='#636EFA', xbins=dict(size=0.5)))
fig3.add_trace(go.Scatter(x=x_range, y=kde_flat(x_range), mode='lines', name='Flat KDE', line=dict(color='#636EFA', width=2), showlegend=False))
fig3.add_trace(go.Histogram(x=house_data, histnorm='probability density', name='House', opacity=0.6, marker_color='#EF553B', xbins=dict(size=0.5)))
fig3.add_trace(go.Scatter(x=x_range, y=kde_house(x_range), mode='lines', name='House KDE', line=dict(color='#EF553B', width=2), showlegend=False))
fig3.update_layout(
    barmode='overlay',
    title_text='Price Distribution: Flats vs Houses',
    xaxis_title="Price",
    yaxis_title="Density",
    xaxis_range=[-5, 35],
    legend=dict(
        title="Property Type"
    )
)
st.plotly_chart(fig3, width='stretch')