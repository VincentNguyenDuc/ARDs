import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./data/raw/Australian_Road_Deaths.csv")

st.title("Data Wrangling")

st.markdown("""
We will first perform some simple data cleaning:
- Transform the format of YYYYMM column into 2 different columns, Year and Month.
- Remove the records with missing values, undetermined values, unspecified values, and duplicates.
""")

# Format datetime
df["YYYYMM"] = pd.to_datetime(
    df["YYYYMM"],
    format='%Y%m'
)
df["YYYYMM"] = df["YYYYMM"].dt.to_period("M")
year_value = df["YYYYMM"].dt.year
month_value = df["YYYYMM"].dt.month
df.insert(loc=3, column="Year", value=year_value)
df.insert(loc=4, column="Month", value=month_value)

# remove missing values
df.dropna(axis=0, how='any', inplace=True)

# remove undetermined and unspecified values
df = df[
    (df["National Road Type"] != "Undetermined") &
    (df["Gender"] != "Unspecified")
]

# remove duplicate
df.drop_duplicates(inplace=True)

# reset index
df.reset_index(drop=True, inplace=True)

st.dataframe(df)

st.markdown("""
We also realize that there are some counter-intuitive data in Age column and years of Driving Experience:
""")

counter_intuitive_values = df.loc[
    df["Age"] - df["Driving experience"] < 0,
    ["Age", "Driving experience"]
]
counter_intuitive_values = pd.DataFrame(counter_intuitive_values)

st.subheader("Road Users Age (Years) against Driving Experience (Years)")
st.scatter_chart(
    data=df,
    x="Driving experience",
    y="Age",
    color="#ff0000"
)

st.markdown("""
We can clearly see that there is a linear relationship between age and driving experience, except for outliers.
In order to handle this scenario, we can simply remove all the counter-intuitive records, or we can use a statistical model (such as: Linear Regression) to predict and replace the values at those records based on other predictors.
""")

# let x = driving experience[without counter intuitive data]
# let y = age[without counter intuitive data]
# let y_predict = age[with counter intuitive data]

# Training data
data_without_counter_intuitive = df.loc[
    df["Age"] - df["Driving experience"] >= 0,
    ["Age", "Driving experience"]
]

x = data_without_counter_intuitive["Driving experience"].values.reshape(-1, 1)
y = data_without_counter_intuitive["Age"].values.reshape(-1, 1)

# counter intuitive data
x_ = counter_intuitive_values["Driving experience"].values.reshape(-1, 1)
y_ = counter_intuitive_values["Age"]

# Using regression to fit
model = LinearRegression()
model.fit(x, y)

# predicted data from counter intuitive data
y_predict = model.predict(x_)

# plot for better visualization
fig, ax = plt.subplots()
ax.set_title("Age (Years) against Driving Experience (Years)")
ax.scatter(x_, y_, color="blue")
ax.scatter(x_, y_predict, color="red")
ax.set_xlabel("Driving Experience")
ax.set_ylabel("Age")
ax.legend(["recorded data", "predicted data"])
st.pyplot(fig)

st.markdown("""
Now, we can write the wrangled data into a new csv file: clean_ARD.csv
""")

# replace the data
counter_intuitive_values["Age"] = y_predict.flatten().astype(int)

def merge_dataframe(df1, df2):
    index_1 = df1.index
    value = list(df1["Age"])
    count = 0
    for i in index_1:
        df2.at[i, "Age"] = value[count]
        count += 1

merge_dataframe(counter_intuitive_values, df)
df.to_csv("./data/processed/clean_ARD.csv", index=False)
