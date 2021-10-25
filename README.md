# Basketball Project
### Purpose
This purpose of this project is to solve the hypothesis that certain basketball players perform better or worse during the playoffs. Certain examples would include 
Paul George, who was given the nickname "Pandemic P" for his lackluster performance during the 2020 playoffs, as well as Lebron James, who numerous players label
as the hardest obstacle to get over in order to continue chasing their dreams of a championship, especially during his time on the East Coast. In the .png files in this repository, I used field goal percentage as an example.
<br />
<br />
In addition, this project would help strengthen my Python skills, specifically the use of Numpy, Pandas, and Matplotlib towards Data Science projects. 
### Skills used
This program was primarily written in Python, however I had also used Excel and a scrapper to obtain proper statistics that could feed into Pandas Dataframes and Numpy Arrays.

### Explanation
The program asks for a specific player and what stats that one would like to compare, and then print out a chart that showed the stat from the regular seasons in comparison to the stat in the playoff season.
<br />
In order to see the comparisons between the statistics, I wrote a Python script that took used a scrapper to obtain data from Basketball Reference, a website that holds
almost all the NBA statistics for every player. The scrapper had allowed one to search for any specific player, so I had used it to create two Pandas Dataframes; one for all of their regular seasons and one for seasons they made the playoffs. The two were then cross-referenced so the first dataframe would only include the seasons they made the playoffs. The program would then scan to see if the player had been traded during that season or not to a different team. Finally, I used Matplotlib to create the settings and create the chart, as well as the ability for the chart to be saved as a png.

### Issues Encountered
I had encountered an issue regarding players that were traded once or even multiple times during a season, as this affected the amount of data points they had for one season. On the graph, there would be three Y-values (performance) for one X-value (season). In order to solve this, I decided it was best to average their performance on all of the teams. However, this doesn't cover every problem, like how they could have performed better/worse depending on the team they got traded to, or how many games they played on each team. But averaging their performance was the most simple solution, and in the future I could implement a more statisically correct answer.
