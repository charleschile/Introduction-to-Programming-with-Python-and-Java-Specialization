""" Q1: 
Get the summary statistics for imdb_score and gross, then use the describe() function to summarize this visually. Save the
result in a variable called score_gross_description and print it.
"""

# your code here
score_gross = ["imdb_score", "gross"]
df_score_gross = df[score_gross]
score_gross_description = df_score_gross.describe()
print(score_gross_description)


"""Q2:
What is the average rating of the director Christopher Nolan's movies? Save this value in a variable called nolan_mean and 
print.
"""

# your code here

chritopher_nolan = df["director_name"] == "Christopher Nolan"
nolan_mean = df[chritopher_nolan]["imdb_score"].mean()
print(nolan_mean)


"""Q3: 
Create a series called 'directors' that contains each director's name and his or her average rating.  Print out the type of your variable.
Use the 'directors' series to find the average rating for Steven Spielberg.  Print the value.
"""

# your code here
import numpy as np
directors = df.groupby(["director_name"]).mean()["imdb_score"]
print(type(directors))
print(directors["director_name" == "Steven Spielberg"])


"""Q4:
Select the non-USA movies made after 1960 by Hayao Miyazaki.
Save the result in a DataFrame called 'miyazaki', then print it.

Here are the steps:
1. Query the data ('df' DataFrame) based on the following conditions:
- Non-USA movies (country_id != 1)
- Movies made after 1960 (title_year > 1960)
- Movies made by director Hayao Miyazaki (director_id == 46)
2. Save the filtered data in a DataFrame called 'miyazaki' and print it

"""

# your code here

hayao = df["director_id"] == 46
non_usa = df["country_id"] != 1
made_year = df["title_year"] > 1960

miyazaki = df[hayao & non_usa & made_year]
print(miyazaki)


"""Q5: 
Create a Pivot Table that shows the median rating for each director, grouped by their respective countries. Name your variable
'pivot_agg'
"""

# your code here

pivot_agg = pd.pivot_table(
    df, index=["country", "director_name"],
    values=["imdb_score"],
    aggfunc=[np.median])

"""Q6:
How long did the movie Gladiator aim to keep your attention? Save the series with this information
in a variable called 'gladiator_duration', then print it.
"""

# your code here
df_gladiator = df[df["movie_title"] == "Gladiator"]
gladiator_duration = df_gladiator["duration"]
