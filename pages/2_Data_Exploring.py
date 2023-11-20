import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('./data/processed/clean_ARD.csv')

# Investigate yearly trend of crash
st.header("The number of Crashes over Years for Car Driver")
number_of_crashes_df = pd.DataFrame(
    df[["Year", "Month", "Road User"]].value_counts()
)
number_of_crashes_df.rename(columns={0: "Number of crash"}, inplace=True)
number_of_crashes_df.reset_index(inplace=True)
car_crashes = number_of_crashes_df[number_of_crashes_df["Road User"] == "Car driver"]
car_crashes = car_crashes.sort_values(
    by=["Year", "Month"]).reset_index(drop=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.bar_chart(car_crashes, x="Year", y="count")

with col2:
    st.dataframe(car_crashes)

# The relationship between the number of crashes and Driving experience
st.header("The Number of Crashes against Years of Driving Experience")
list_of_drivers = ["Car driver", "Motorcycle rider",
                   "Pedal cyclist", "Other vehicle driver"]

crashes_experience = df[df["Road User"].isin(list_of_drivers)]

crashes_experience = crashes_experience[["Driving experience"]].value_counts()
crashes_experience = pd.DataFrame(crashes_experience)
crashes_experience.sort_index(inplace=True)
crashes_experience.rename(columns={0: "Number of crashes"}, inplace=True)
crashes_experience.reset_index(inplace=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.dataframe(crashes_experience)

with col2:
    st.bar_chart(crashes_experience, x="Driving experience", y="count")

# The number of crashes over months for each years
states_crashes_over_years = pd.DataFrame(
    df[["Year", "State"]]
    .groupby(["Year", "State"])
    .value_counts()
).reset_index()

fig, ax = plt.subplots(figsize=(10, 10))
states = states_crashes_over_years['State'].unique()

for state in states:
    state_data = states_crashes_over_years[states_crashes_over_years['State'] == state]
    ax.plot(state_data['Year'], state_data['count'], label=state)
    
ax.set_title("Crashes at states over years (2014-2021)")
ax.set_xlabel("Years")
ax.set_ylabel("Number of Crashes")
ax.scatter(states_crashes_over_years["Year"], states_crashes_over_years["count"])
ax.legend()
st.pyplot(fig)
