# NBA player stat/standing analysis of 2017-2022 season 
<h4>Data analytic project</h4>
<li>Created a web scarper using python selenium module</li>
<li>Cleaned and visualized data using RStudio and R.</li>
<li>Scraped over 1,200 NBA player stat from 2017 to 2022 season from <a href="https://nba.com/"> nba.com</a></li>
<li>Obtained stat calculation method from <a href="https://www.nbastuffer.com/"> nbastuffer.com</a> and <a href="https://www.basketball-reference.com/"> basketball-reference.com</a></li>

<h3><b> Code and Resources Used</b></h3>
<hr>
  <p><b>R Version:</b> 4.2.2</p>
  <p><b>R studio version: 2023.3.0.386</p>
  <p><b> Packages used:</b> ggplot2, dplyr</p>
  <p><b>Python Version:</b> 3.10</p>
  <p><b>Packages used:</b> pandas, selenium</p>

<h3><b> Web Scraping </b></h3>
<hr>
<h4>NBA player data </h4>
<ul>
  <li>Season -- Season stat of the player</li>
  <li>Player -- Each player's name</li>
  <li>Team -- Abbreviated team name each player is in</li>
  <li>GP -- Game played</li>
  <li>MIN -- Average minute played per game</li>
  <li>PTS -- Average points per game</li>
  <li>FGM -- Average field Goal Made per game</li>
  <li>FGA -- Average field Goal Attempted per game</li>
  <li>FG. -- Average field Goal Percentage per game</li>
  <li>X3PM -- Average three point made per game</li>
  <li>X3PA -- Average three point attempt per game</li>
  <li>X3P. -- Average three point percentage per game</li>
  <li>FTM -- Average free throw made per game</li>
  <li>FTA -- Average free throw attempt per game</li>
  <li>FT. -- Average free throw percentage per game</li>
  <li>OREB -- Average offensive rebound per game</li>
  <li>DREB -- Average defensive rebound per game</li>
  <li>REB -- Average rebound per game</li>
  <li>AST -- Average assist per game</li>
  <li>STL -- Average steal per game</li>
  <li>BLK -- Average block per game</li>
  <li>TOV -- Average turnover per game</li>
  <li>EFF -- Individual player efficiency</li>
</ul>
<h4>NBA team standing data </h4>
<ul>
  <li>Season -- Season of the team standing</li>
  <li>Conference -- Each team's conference</li>
  <li>Rank -- Rank of each team. 15 teams for each conference</li>
  <li>Team -- Full name of the team</li>
  <li>W -- Number of wins</li>
  <li>L -- Number of loses</li>
  <li>WIN. -- Win percentage</li>
</ul>

<h3><b> Data Cleaning </b></h3>
<hr>
<li>Checked for missing values and duplicates</li>
<li>Dropped unnecessary rows and columns</li>

<h3><b> Data Modifying </b></h3>
<hr>
<ul>
  <li>PPM -- Points per minute </li>
    <ul>
      <li>Calculated: PTS/MIN</li>
    </ul>
  <li>EFG -- Effective field goal percentage </li>
    <ul>
      <li>The statistic adjusts for the face that a 3-point field goal is worth one more point than a 2-point field goal.</li>
      <li>Calculated: (FGM + 0.5 *3PM) / FGA</li>
    </ul>
  <li>TS -- True shooting percentage</li>
    <ul>
      <li> The statistic calculates player’s or a team’s performance at the free-throw line and considers the efficiency of all types of shots.</li>
      <li>Calculated: 0.5*(Total PTS)/[(Total FGA) + 0.44*(Total FTA)]</li>
    </ul>
</ul>

<h3><b> Data Visualizing </b></h3>
<hr>
I have looked at the distribution of the data and the value counts for various categorical varibales. Below are few highlights from the pivot tables.
<img src= "https://user-images.githubusercontent.com/47937864/227987578-6e803078-ec48-43b0-bf9a-a12b05b23b7f.png" width="800" height="500">
<img src= "https://user-images.githubusercontent.com/47937864/227987743-bbd3bc88-c5c8-4e62-a2b6-c345b01bfa67.png" width="800" height="500">
<img src= "https://user-images.githubusercontent.com/47937864/227987853-2d19ec9e-d82f-4ff9-b2df-274947550e82.png" width="800" height="500">




