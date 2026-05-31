import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(page_title="Recommend Appartments")
location_df = pickle.load(open('A:/CODES/PROJECTS/appartments/models/location_distance.pkl','rb'))
cosine_sim1 = pickle.load(open('A:/CODES/PROJECTS/appartments/models/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('A:/CODES/PROJECTS/appartments/models/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('A:/CODES/PROJECTS/appartments/models/cosine_sim3.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


st.title('Select Location and Radius')
selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    result_df = location_df[location_df[selected_location] < radius*1000][[selected_location]].sort_values(by=selected_location)
    if result_df.empty:
        st.warning(f"No properties found within {radius} km of {selected_location}. Try increasing the radius!")
    else:
        result_df[selected_location] = result_df[selected_location].apply(lambda x: round(x/1000, 2))
        st.dataframe(result_df)


st.title('Recommend Appartments')
selected_appartment = st.selectbox('Select an appartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    # We can take selected_appartment as input from above search result
    recommendation_df = recommend_properties_with_scores(selected_appartment)
    st.dataframe(recommendation_df)