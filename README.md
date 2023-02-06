# Australian-roads-deaths

Exploring Australian Road Deaths (ARD) dataset -
[Source code](https://github.com/VincentNguyenDuc/Australian-roads-deaths)

## Table of contents

- [Australian-roads-deaths](#australian-roads-deaths)
  - [Table of contents](#table-of-contents)
  - [General information](#general-information)
  - [Technologies](#technologies)
  - [Algorithms](#algorithms)
  - [Project Objectives](#project-objectives)

## General information

The Australian Road Deaths (ARD) dataset provides basic details of road transport crash fatalities in Australia as reported by the police each month to the State and Territory road safety authorities. It is published by the Bureau of Infrastructure, Transport and Regional Economics.

- The ARD dataset (Australian_Road_Deaths.csv file) contains basic demographic and
crash details of people who have died in an Australian road crash.
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

## Technologies

- Python
- Jupyter Notebook
- Pandas
- Scikit-learn
- Matplotlib
- Numpy

## Algorithms

- Linear Regression
- Polynomial Regression
- Pearson Correlation

## Project Objectives

- Use sklearn to fit linear regression to data
- Explore and perform data analysis on the ARD dataset
- Use various graphical and non-graphical tools to perform data exploration, data wrangling, and data analysis
- Investigate crashes over different months for specific road user
- Investigate the relationship between Age, Speed, and Driving Experiences
- Investigate yearly trend of crash
- Use a model-based approach to fill in the counter-intuitive values
