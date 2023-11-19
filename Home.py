import streamlit as st

st.set_page_config(
  page_title="ARDs",
  layout="centered",
  page_icon="🧊"
)

st.title("Exploring Australian Road Deaths (ARD) Dataset")
st.markdown("""
The Australian Road Deaths (ARD) dataset provides basic details of road transport crash fatalities in Australia as reported by the police each month to the State and Territory road safety authorities. It is published by the Bureau of Infrastructure, Transport and Regional Economics.

- The ARD dataset (Australian_Road_Deaths.csv file) contains basic demographic and
crash details of people who have died in an Australian road crash.
- The data is collected from the year 2014 to 2021.
- The dataset contains the following information:
The Australian Road Deaths (ARD) dataset provides basic details of road transport crash fatalities in Australia as reported by the police each month to the State and Territory road safety authorities. It is published by the Bureau of Infrastructure, Transport and Regional Economics.

- The ARD dataset (Australian_Road_Deaths.csv file) contains basic demographic and crash details of people who have died in an Australian road crash.
- The data is collected from the year 2014 to 2021.
- The dataset contains the following information:

| Column                        | Description                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Crash ID                      | National crash identifying number                                                                                                                   |
| State                         | State of crash                                                                                                                                      |
| YYYYMM                        | Year and Month of crash                                                                                                                             |
| Day of week                   | Day of week of crash                                                                                                                                |
| Time                          | Time of crash                                                                                                                                       |
| Crash Type                    | The number of vehicles involved in the crash                                                                                                        |
| Bus Involvement               | Indicates involvement of a bus in the crash                                                                                                         |
| Heavy Rigid Truck Involvement | Indicates involvement of a heavy rigid truck in the crash                                                                                           |
| Articulated Truck Involvement | Indicates involvement of an articulated truck in the crash                                                                                          |
| Road User                     | Road user type of a killed person                                                                                                                   |
| Gender                        | Gender of a killed person                                                                                                                           |
| Age                           | Age of a killed person (years)                                                                                                                      |
| Speed                         | Speed of a vehicle in the crash (km/h)                                                                                                              |
| Driving Experience            | Driving experience of a killed person (years)                                                                                                       |
| National Remoteness Areas     | [ABS Remoteness Structure](https://www.abs.gov.au/statistics/statistical-geography/remoteness-structure)                                            |
| SA4 Name 2016                 | [Australian Statistical Geography Standard](https://www.abs.gov.au/statistics/statistical-geography/australian-statistical-geography-standard-asgs) |
| National LGA Name 2017        | [Australian Statistical Geography Standard](https://www.abs.gov.au/statistics/statistical-geography/australian-statistical-geography-standard-asgs) |
| National Road Type            | National Road Type                                                                                                                                  |
| Christmas Period              | Indicates if crash occurred during the 12 days commencing on December 23rd                                                                          |
| Easter Period                 | Indicates if crash occurred during the 5 days commencing on the Thursday before Good Friday                                                         |
| Age Group                     | Standard age groupings                                                                                                                              |
| Time of day                   | Indicates if crash occurred during the day or night                                                                                                 |
""")

st.title("Project Objectives")
st.markdown("""
In the course of this project, our primary objective is to delve into the intricacies of the provided data fields, seeking to unravel and comprehend the interrelationships that exist among them. This exploration will be facilitated through the application of Statistical Theory, complemented by the utilization of Python's robust Data Analysis Libraries. Through these analytical tools, we endeavor to gain a comprehensive understanding of the patterns, correlations, and insights embedded within the dataset
""")
