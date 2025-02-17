# Practice Praoject: 

## Introduction:
This project, "200 Countries, 200 Years, 4 Minutes", is a recreation of the renowned data visualization by Hans Rosling. We built a database using pandas and sqlite3, conducted a proof of concept with matplotlib, and ultimately created the final visualization using plotly.express.

## How to Reproduce
 - Install Miniconda
 - Create the environment using `environment.yml`:
 ```bash
 conda env create -f environment.yml
 ```
 - Place the four CSV files from the `data/` folder into the `data/` folder in the working directory.
 ```bash
 python create_gapminder_db.py
 ```
 This will create `gapminder.db` in the `data/` floder.
 - Activate the environment and run:
 ```bash
 python plot_with_px.py
 ```
 This will generate `gapminder_clone.html`
