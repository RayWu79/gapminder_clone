import sqlite3
import pandas as pd
import plotly.express as px

connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting""", con=connection)
connection.close()
# print(plotting_df.columns)
fig = px.scatter(data_frame=plotting_df, x="gdp_per_capita", y="life_expectancy"
                 , color="continent", size="population", animation_frame="dt_year"
                 , animation_group="country_name", size_max=100, hover_name="country_name"
                 , range_x=[100, 100000], range_y=[20, 100], title="Gapminder Clone 1800-2400", log_x=True)
fig.write_html("gapminder_clone.html", auto_open=True)