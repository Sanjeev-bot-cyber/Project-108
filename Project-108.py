import pandas as pd
import plotly.figure_factory as px

fd = pd.read_csv("Mobile Brand - Average Rating.csv")
figure = px.create_distplot([fd["Avg Rating"].tolist()],["result"])
figure.show()