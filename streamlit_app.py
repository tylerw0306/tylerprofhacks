import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Fridge Display', page_icon='📊')
st.title('📊 Interactive Fridge Display')

st.subheader('What allergies do you have?')

# Input widgets
## Genres selection
allergy_list = ["Eggs", "Fish", "Milk", "Peanuts", "Pescatarian", "Shellfish", "Soy", "Tree nuts", "Vegan", "Vegatarian"]
genres_selection = st.multiselect('Select allergies', allergy_list, ["Eggs", "Fish", "Milk", "Peanuts", "Pescatarian", "Shellfish", "Soy", "Tree nuts", "Vegan", "Vegatarian"])
