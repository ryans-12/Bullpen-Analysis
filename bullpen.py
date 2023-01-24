import pandas as pd
import math
import streamlit as st
import plotly_express as px

df = pd.read_csv('psu-pitching.csv')




def pitcher_change():
    #adds column to show true if pitcher id changes
    df["PitcherChanged"] = df["PitcherId"].shift() != df["PitcherId"]

#gets list of pitchers who did not start game
def get_relievers():
    #relievers = dataframe of pitchers who are new but didnt start
    relievers = df.loc[(df["PitcherChanged"] == True) & (df["PitchNo"] != 1)]
    relievers_list = relievers["PitcherId"].unique()
    return relievers_list

def pitchdata_by_day():
    #gets sub-dataframe
    #selected_data = all pitches with selected pitcherId
    selected_data = df[df["PitcherId"] == selected_pitcher]
    #########
    st.dataframe(selected_data)
    ########
    dates = selected_data["Date"].unique()
    data_by_date = {}   #dict to store dataframes
    for date in dates:
        indexed_data = selected_data[selected_data["Date"] == date]
        dict_key = str(selected_pitcher)+"_"+str(date)
        data_by_date[dict_key] = indexed_data
    #returns dictionary of dataframes for selected pitcher and date
    return data_by_date



pitcher_change()

st.title("PSU Baseball Bullpen Analysis")
st.sidebar.markdown("### Dataset Filters")
selected_pitcher = st.sidebar.selectbox('Select PitcherID: ', get_relievers())





dicttest = pitchdata_by_day()

st.markdown(dicttest.keys())

for key in dicttest:
    st.dataframe(dicttest[key])
