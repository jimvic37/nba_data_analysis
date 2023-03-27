NBA 2017-2022 season analysis
================

``` r
# libraries used for the project
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
library(ggplot2)
```

``` r
# get current working directory
getwd()
```

    ## [1] "C:/Users/jimvi/OneDrive/Documents/job/Projects/nba_project_data_analysis&web_scraper"

``` r
# set directory to nba_player_data.csv to read csv file
setwd("C://Users//jimvi//OneDrive//Documents//job//Projects//nba_project_data_analysis&web_scraper//webscrapeNba")
# reading csv file for player data through 2017-2022 season
df_player <- read.csv("nba_player_data.csv")
# reading csv file for team standing data through 2017-2022 season
df_standing <- read.csv("nba_team_data.csv")
```

<h3>
Preliminary data exploration
</h3>

``` r
nrow(df_player)
```

    ## [1] 1237

``` r
ncol(df_player)
```

    ## [1] 24

``` r
head(df_player)
```

    ##   X  Season                 Player Team GP  MIN  PTS  FGM  FGA  FG. X3PM X3PA
    ## 1 0 2017-18          James Harden   HOU 72 35.4 30.4  9.0 20.1 44.9  3.7 10.0
    ## 2 1 2017-18         Anthony Davis   NOP 75 36.4 28.1 10.4 19.5 53.4  0.7  2.2
    ## 3 2 2017-18          LeBron James   CLE 82 36.9 27.5 10.5 19.3 54.2  1.8  5.0
    ## 4 3 2017-18        Damian Lillard   POR 73 36.6 26.9  8.5 19.4 43.9  3.1  8.6
    ## 5 4 2017-18 Giannis Antetokounmpo   MIL 75 36.7 26.9  9.9 18.7 52.9  0.6  1.9
    ## 6 5 2017-18          Kevin Durant   GSW 68 34.2 26.4  9.3 18.0 51.6  2.5  6.1
    ##   X3P. FTM  FTA  FT. OREB DREB  REB AST STL BLK TOV  EFF
    ## 1 36.7 8.7 10.1 85.8  0.6  4.8  5.4 8.8 1.8 0.7 4.4 30.1
    ## 2 34.0 6.6  8.0 82.8  2.5  8.6 11.1 2.3 1.5 2.6 2.2 33.0
    ## 3 36.7 4.7  6.5 73.1  1.2  7.5  8.6 9.1 1.4 0.9 4.2 32.7
    ## 4 36.1 6.8  7.4 91.6  0.8  3.6  4.5 6.6 1.1 0.4 2.8 25.0
    ## 5 30.7 6.5  8.5 76.0  2.1  8.0 10.0 4.8 1.5 1.4 3.0 30.7
    ## 6 41.9 5.3  5.9 88.9  0.5  6.4  6.8 5.4 0.7 1.8 3.0 28.6

``` r
tail(df_player)
```

    ##         X  Season                 Player Team GP  MIN PTS FGM FGA  FG. X3PM
    ## 1232 1231 2021-22          Jevon Carter   MIL 66 13.7 4.2 1.5 3.8 38.7  1.0
    ## 1233 1232 2021-22       Frank Ntilikina   DAL 58 11.8 4.1 1.5 3.8 39.9  0.7
    ## 1234 1233 2021-22 Juan Toscano-Anderson   GSW 73 13.6 4.1 1.6 3.2 48.9  0.4
    ## 1235 1234 2021-22     Jordan McLaughlin   MIN 62 14.5 3.8 1.4 3.2 44.0  0.4
    ## 1236 1235 2021-22         Trent Forrest   UTA 60 12.8 3.3 1.3 2.6 49.0  0.1
    ## 1237 1236 2021-22         Dalano Banton   TOR 64 10.9 3.2 1.3 3.2 41.1  0.2
    ##      X3PA X3P. FTM FTA  FT. OREB DREB REB AST STL BLK TOV EFF
    ## 1232  2.6 38.8 0.2 0.3 83.3  0.2  1.5 1.7 1.5 0.4 0.2 0.5 5.0
    ## 1233  1.9 34.2 0.4 0.4 96.0  0.2  1.2 1.4 1.2 0.5 0.1 0.5 4.4
    ## 1234  1.2 32.2 0.5 1.0 57.1  0.4  2.0 2.4 1.7 0.7 0.2 0.9 6.1
    ## 1235  1.4 31.8 0.5 0.6 75.0  0.4  1.2 1.5 2.9 0.9 0.2 0.6 6.7
    ## 1236  0.5 18.5 0.6 0.8 79.2  0.4  1.3 1.7 1.8 0.5 0.1 0.8 5.0
    ## 1237  0.8 25.5 0.4 0.7 59.1  0.6  1.3 1.9 1.5 0.4 0.2 0.8 4.3

``` r
str(df_player)
```

    ## 'data.frame':    1237 obs. of  24 variables:
    ##  $ X     : int  0 1 2 3 4 5 6 7 8 9 ...
    ##  $ Season: chr  "2017-18" "2017-18" "2017-18" "2017-18" ...
    ##  $ Player: chr  "James Harden " "Anthony Davis " "LeBron James " "Damian Lillard " ...
    ##  $ Team  : chr  "HOU" "NOP" "CLE" "POR" ...
    ##  $ GP    : int  72 75 82 73 75 68 80 60 75 75 ...
    ##  $ MIN   : num  35.4 36.4 36.9 36.6 36.7 34.2 36.4 32.2 33.5 34 ...
    ##  $ PTS   : num  30.4 28.1 27.5 26.9 26.9 26.4 25.4 24.4 23.1 23.1 ...
    ##  $ FGM   : num  9 10.4 10.5 8.5 9.9 9.3 9.5 8.9 9.2 8.5 ...
    ##  $ FGA   : num  20.1 19.5 19.3 19.4 18.7 18 21.1 18.1 18 17.9 ...
    ##  $ FG.   : num  44.9 53.4 54.2 43.9 52.9 51.6 44.9 49.1 51 47.7 ...
    ##  $ X3PM  : num  3.7 0.7 1.8 3.1 0.6 2.5 1.2 2.8 0.4 2.1 ...
    ##  $ X3PA  : num  10 2.2 5 8.6 1.9 6.1 4.1 6.8 1.2 5.8 ...
    ##  $ X3P.  : num  36.7 34 36.7 36.1 30.7 41.9 29.8 40.8 29.3 37.1 ...
    ##  $ FTM   : num  8.7 6.6 4.7 6.8 6.5 5.3 5.2 3.9 4.5 3.9 ...
    ##  $ FTA   : num  10.1 8 6.5 7.4 8.5 5.9 7.1 4.4 5.3 4.9 ...
    ##  $ FT.   : num  85.8 82.8 73.1 91.6 76 88.9 73.7 88.9 83.7 79.9 ...
    ##  $ OREB  : num  0.6 2.5 1.2 0.8 2.1 0.5 1.9 0.6 3.3 0.6 ...
    ##  $ DREB  : num  4.8 8.6 7.5 3.6 8 6.4 8.2 3.2 5.2 4.6 ...
    ##  $ REB   : num  5.4 11.1 8.6 4.5 10 6.8 10.1 3.8 8.5 5.2 ...
    ##  $ AST   : num  8.8 2.3 9.1 6.6 4.8 5.4 10.3 5.1 2 4.3 ...
    ##  $ STL   : num  1.8 1.5 1.4 1.1 1.5 0.7 1.8 1.1 0.6 2.4 ...
    ##  $ BLK   : num  0.7 2.6 0.9 0.4 1.4 1.8 0.3 0.3 1.2 0.8 ...
    ##  $ TOV   : num  4.4 2.2 4.2 2.8 3 3 4.8 2.3 1.5 2.9 ...
    ##  $ EFF   : num  30.1 33 32.7 25 30.7 28.6 29.5 22.7 24.3 22.5 ...

``` r
summary(df_player)
```

    ##        X           Season             Player              Team          
    ##  Min.   :   0   Length:1237        Length:1237        Length:1237       
    ##  1st Qu.: 309   Class :character   Class :character   Class :character  
    ##  Median : 618   Mode  :character   Mode  :character   Mode  :character  
    ##  Mean   : 618                                                           
    ##  3rd Qu.: 927                                                           
    ##  Max.   :1236                                                           
    ##        GP             MIN             PTS             FGM        
    ##  Min.   :45.00   Min.   : 4.90   Min.   : 1.00   Min.   : 0.300  
    ##  1st Qu.:62.00   1st Qu.:19.90   1st Qu.: 7.40   1st Qu.: 2.800  
    ##  Median :68.00   Median :25.60   Median :10.40   Median : 3.800  
    ##  Mean   :67.65   Mean   :25.24   Mean   :11.81   Mean   : 4.343  
    ##  3rd Qu.:74.00   3rd Qu.:30.90   3rd Qu.:15.10   3rd Qu.: 5.600  
    ##  Max.   :82.00   Max.   :37.90   Max.   :36.10   Max.   :11.200  
    ##       FGA              FG.            X3PM            X3PA       
    ##  Min.   : 0.800   Min.   :33.0   Min.   :0.000   Min.   : 0.000  
    ##  1st Qu.: 5.900   1st Qu.:42.2   1st Qu.:0.600   1st Qu.: 1.800  
    ##  Median : 8.300   Median :45.2   Median :1.200   Median : 3.400  
    ##  Mean   : 9.334   Mean   :46.8   Mean   :1.272   Mean   : 3.496  
    ##  3rd Qu.:12.100   3rd Qu.:49.5   3rd Qu.:1.900   3rd Qu.: 5.000  
    ##  Max.   :24.500   Max.   :76.3   Max.   :5.300   Max.   :13.200  
    ##       X3P.             FTM              FTA              FT.        
    ##  Min.   :  0.00   Min.   : 0.100   Min.   : 0.100   Min.   : 30.00  
    ##  1st Qu.: 31.40   1st Qu.: 0.900   1st Qu.: 1.200   1st Qu.: 71.40  
    ##  Median : 35.20   Median : 1.400   Median : 1.900   Median : 78.40  
    ##  Mean   : 32.93   Mean   : 1.856   Mean   : 2.388   Mean   : 76.88  
    ##  3rd Qu.: 38.50   3rd Qu.: 2.300   3rd Qu.: 3.000   3rd Qu.: 84.00  
    ##  Max.   :100.00   Max.   :10.200   Max.   :11.800   Max.   :100.00  
    ##       OREB            DREB             REB              AST        
    ##  Min.   :0.100   Min.   : 0.500   Min.   : 0.700   Min.   : 0.300  
    ##  1st Qu.:0.500   1st Qu.: 2.300   1st Qu.: 2.900   1st Qu.: 1.200  
    ##  Median :0.800   Median : 3.200   Median : 4.100   Median : 1.900  
    ##  Mean   :1.033   Mean   : 3.597   Mean   : 4.629   Mean   : 2.597  
    ##  3rd Qu.:1.300   3rd Qu.: 4.400   3rd Qu.: 5.600   3rd Qu.: 3.400  
    ##  Max.   :5.400   Max.   :11.400   Max.   :16.000   Max.   :11.700  
    ##       STL              BLK              TOV             EFF      
    ##  Min.   :0.1000   Min.   :0.0000   Min.   :0.200   Min.   : 1.3  
    ##  1st Qu.:0.5000   1st Qu.:0.2000   1st Qu.:0.800   1st Qu.: 9.0  
    ##  Median :0.7000   Median :0.4000   Median :1.200   Median :12.1  
    ##  Mean   :0.8036   Mean   :0.4989   Mean   :1.418   Mean   :13.4  
    ##  3rd Qu.:1.0000   3rd Qu.:0.6000   3rd Qu.:1.800   3rd Qu.:16.5  
    ##  Max.   :2.4000   Max.   :2.9000   Max.   :5.000   Max.   :38.7

``` r
nrow(df_standing)
```

    ## [1] 150

``` r
ncol(df_standing)
```

    ## [1] 8

``` r
head(df_standing)
```

    ##   X  Season Conference Rank                Team  W  L  WIN.
    ## 1 0 2017-18    Eastern    1     Toronto Raptors 59 23 0.720
    ## 2 1 2017-18    Eastern    2      Boston Celtics 55 27 0.671
    ## 3 2 2017-18    Eastern    3  Philadelphia 76ers 52 30 0.634
    ## 4 3 2017-18    Eastern    4 Cleveland Cavaliers 50 32 0.610
    ## 5 4 2017-18    Eastern    5      Indiana Pacers 48 34 0.585
    ## 6 5 2017-18    Eastern    6          Miami Heat 44 38 0.537

``` r
tail(df_standing)
```

    ##       X  Season Conference Rank                   Team  W  L  WIN.
    ## 145 144 2021-22    Western   10      San Antonio Spurs 34 48 0.415
    ## 146 145 2021-22    Western   11     Los Angeles Lakers 33 49 0.402
    ## 147 146 2021-22    Western   12       Sacramento Kings 30 52 0.366
    ## 148 147 2021-22    Western   13 Portland Trail Blazers 27 55 0.329
    ## 149 148 2021-22    Western   14  Oklahoma City Thunder 24 58 0.293
    ## 150 149 2021-22    Western   15        Houston Rockets 20 62 0.244

``` r
str(df_standing)
```

    ## 'data.frame':    150 obs. of  8 variables:
    ##  $ X         : int  0 1 2 3 4 5 6 7 8 9 ...
    ##  $ Season    : chr  "2017-18" "2017-18" "2017-18" "2017-18" ...
    ##  $ Conference: chr  "Eastern" "Eastern" "Eastern" "Eastern" ...
    ##  $ Rank      : int  1 2 3 4 5 6 7 8 9 10 ...
    ##  $ Team      : chr  "Toronto Raptors" "Boston Celtics" "Philadelphia 76ers" "Cleveland Cavaliers" ...
    ##  $ W         : int  59 55 52 50 48 44 44 43 39 36 ...
    ##  $ L         : int  23 27 30 32 34 38 38 39 43 46 ...
    ##  $ WIN.      : num  0.72 0.671 0.634 0.61 0.585 0.537 0.537 0.524 0.476 0.439 ...

``` r
summary(df_standing)
```

    ##        X             Season           Conference             Rank   
    ##  Min.   :  0.00   Length:150         Length:150         Min.   : 1  
    ##  1st Qu.: 37.25   Class :character   Class :character   1st Qu.: 4  
    ##  Median : 74.50   Mode  :character   Mode  :character   Median : 8  
    ##  Mean   : 74.50                                         Mean   : 8  
    ##  3rd Qu.:111.75                                         3rd Qu.:12  
    ##  Max.   :149.00                                         Max.   :15  
    ##      Team                 W               L              WIN.      
    ##  Length:150         Min.   :15.00   Min.   :17.00   Min.   :0.207  
    ##  Class :character   1st Qu.:30.25   1st Qu.:30.25   1st Qu.:0.393  
    ##  Mode  :character   Median :41.00   Median :38.00   Median :0.518  
    ##                     Mean   :38.86   Mean   :38.86   Mean   :0.499  
    ##                     3rd Qu.:48.00   3rd Qu.:46.75   3rd Qu.:0.610  
    ##                     Max.   :65.00   Max.   :65.00   Max.   :0.793

<h3>
Data cleaning/modifying
</h3>

``` r
df_player$X <- NULL
df_standing$X <- NULL
```

``` r
any(is.na(df_player))
```

    ## [1] FALSE

``` r
any(duplicated(df_player))
```

    ## [1] FALSE

``` r
any(is.na(df_standing))
```

    ## [1] FALSE

``` r
any(duplicated(df_standing))
```

    ## [1] FALSE

``` r
# adding EFG% 
df_player$EFG <- round(((df_player$FGM + 0.5 * df_player$X3PM)/
                          df_player$FGA * 100), 1)
# adding TS% column 
df_player$TS <- round((0.5*df_player$PTS*df_player$GP/
                         (df_player$FGA*df_player$GP + 
                            (0.44*df_player$FTA*df_player$GP)))*100, 1)
# adding points per minute column
df_player$PPM <- round(df_player$PTS/df_player$MIN, 2)
```

<h3>
Data visualizing
</h3>

``` r
team_names <- c('ATL' = 'Atlanta Hawks', 'BKN' = 'Brooklyn Nets', 'BOS' = 'Boston Celtics', 'CHA' = 'Charlotte Hornets', 
                'CHI' = 'Chicago Bulls', 'CLE' = 'Cleveland Cavaliers', 'DAL' = 'Dallas Mavericks', 'DEN' = 'Denver Nuggets', 
                'DET' = 'Detroit Pistons', 'GSW' = 'Golden State Warriors', 'HOU' = 'Houston Rockets', 'IND' = 'Indiana Pacers', 
                'LAC' = 'LA Clippers', 'LAL' = 'Los Angeles Lakers', 'MEM' = 'Memphis Grizzlies', 'MIA' = 'Miami Heat', 
                'MIL' = 'Milwaukee Bucks', 'MIN' = 'Minnesota Timberwolves', 'NOP' = 'New Orleans Pelicans', 'NYK' = 'New York Knicks', 
                'OKC' = 'Oklahoma City Thunder', 'ORL' = 'Orlando Magic', 'PHI' = 'Philadelphia 76ers', 'PHX' = 'Phoenix Suns', 
                'POR' = 'Portland Trail Blazers', 'SAC' = 'Sacramento Kings', 'SAS' = 'San Antonio Spurs', 'TOR' = 'Toronto Raptors', 
                'UTA' = 'Utah Jazz', 'WAS' = 'Washington Wizards')
df_player$Team <- team_names[df_player$Team]
```

<h4>
Creating data frame of MVP of each season
</h4>

``` r
mvp <- data.frame(
  Season = c("2017-18", "2018-19", "2019-20", "2020-21", "2021-22"),
  Player = c("James Harden ", "Giannis Antetokounmpo ", "Giannis Antetokounmpo "
             , "Nikola Jokic ", "Nikola Jokic ")
)
```

<h4>
Merging data frame to check whether player with max efficiency won the
MVP each season
</h4>

``` r
max_eff_by_season <- df_player %>%
  group_by(Season) %>%
  filter(EFF == max(EFF)) %>%
  select(Season, Player, EFF) %>%
  distinct()
colnames(max_eff_by_season) <- c("Season", "Player_with_max_EFF", "EFF")
merged_mvp_eff <- merge(max_eff_by_season, mvp, by = "Season")
colnames(merged_mvp_eff)[4] <- "MVP"
merged_mvp_eff
```

    ##    Season    Player_with_max_EFF  EFF                    MVP
    ## 1 2017-18         Anthony Davis  33.0          James Harden 
    ## 2 2018-19 Giannis Antetokounmpo  35.3 Giannis Antetokounmpo 
    ## 3 2019-20 Giannis Antetokounmpo  34.6 Giannis Antetokounmpo 
    ## 4 2020-21          Nikola Jokic  35.9          Nikola Jokic 
    ## 5 2021-22          Nikola Jokic  38.7          Nikola Jokic

<h4>
Average efficiency by team
</h4>

``` r
avg_EFF<- aggregate(EFF~Season + Team, df_player, FUN=mean)
avg_EFF$EFF <- round(avg_EFF$EFF, 1)
avg_EFF <- avg_EFF[order(avg_EFF$Season), ]
avg_EFF
```

    ##      Season                   Team  EFF
    ## 1   2017-18          Atlanta Hawks 13.5
    ## 6   2017-18         Boston Celtics 13.0
    ## 11  2017-18          Brooklyn Nets 12.1
    ## 16  2017-18      Charlotte Hornets 12.4
    ## 21  2017-18          Chicago Bulls 12.6
    ## 26  2017-18    Cleveland Cavaliers 13.5
    ## 31  2017-18       Dallas Mavericks 11.5
    ## 36  2017-18         Denver Nuggets 13.5
    ## 41  2017-18        Detroit Pistons 11.5
    ## 46  2017-18  Golden State Warriors 12.3
    ## 51  2017-18        Houston Rockets 15.3
    ## 56  2017-18         Indiana Pacers 14.1
    ## 61  2017-18            LA Clippers 12.8
    ## 66  2017-18     Los Angeles Lakers 14.5
    ## 71  2017-18      Memphis Grizzlies 11.1
    ## 76  2017-18             Miami Heat 12.6
    ## 81  2017-18        Milwaukee Bucks 15.2
    ## 86  2017-18 Minnesota Timberwolves 14.8
    ## 91  2017-18   New Orleans Pelicans 15.9
    ## 96  2017-18        New York Knicks 11.2
    ## 101 2017-18  Oklahoma City Thunder 11.1
    ## 106 2017-18          Orlando Magic  9.5
    ## 111 2017-18     Philadelphia 76ers 15.3
    ## 116 2017-18           Phoenix Suns 11.3
    ## 121 2017-18 Portland Trail Blazers 12.2
    ## 126 2017-18       Sacramento Kings 11.4
    ## 131 2017-18      San Antonio Spurs 10.7
    ## 136 2017-18        Toronto Raptors 12.3
    ## 141 2017-18              Utah Jazz 11.2
    ## 146 2017-18     Washington Wizards 11.6
    ## 2   2018-19          Atlanta Hawks 13.7
    ## 7   2018-19         Boston Celtics 14.8
    ## 12  2018-19          Brooklyn Nets 12.7
    ## 17  2018-19      Charlotte Hornets 12.5
    ## 22  2018-19          Chicago Bulls 10.3
    ## 27  2018-19    Cleveland Cavaliers 11.9
    ## 32  2018-19       Dallas Mavericks 11.3
    ## 37  2018-19         Denver Nuggets 13.7
    ## 42  2018-19        Detroit Pistons 12.5
    ## 47  2018-19  Golden State Warriors 13.3
    ## 52  2018-19        Houston Rockets 15.7
    ## 57  2018-19         Indiana Pacers 12.6
    ## 62  2018-19            LA Clippers 11.4
    ## 67  2018-19     Los Angeles Lakers 11.4
    ## 72  2018-19      Memphis Grizzlies 13.3
    ## 77  2018-19             Miami Heat 14.2
    ## 82  2018-19        Milwaukee Bucks 14.1
    ## 87  2018-19 Minnesota Timberwolves 13.1
    ## 92  2018-19   New Orleans Pelicans 11.7
    ## 97  2018-19        New York Knicks 12.7
    ## 102 2018-19  Oklahoma City Thunder 13.9
    ## 107 2018-19          Orlando Magic 13.8
    ## 112 2018-19     Philadelphia 76ers 16.5
    ## 117 2018-19           Phoenix Suns 14.4
    ## 122 2018-19 Portland Trail Blazers 13.5
    ## 127 2018-19       Sacramento Kings 13.7
    ## 132 2018-19      San Antonio Spurs 13.3
    ## 137 2018-19        Toronto Raptors 15.5
    ## 142 2018-19              Utah Jazz 13.8
    ## 147 2018-19     Washington Wizards 16.0
    ## 3   2019-20          Atlanta Hawks 10.9
    ## 8   2019-20         Boston Celtics 14.2
    ## 13  2019-20          Brooklyn Nets 15.2
    ## 18  2019-20      Charlotte Hornets 12.8
    ## 23  2019-20          Chicago Bulls 12.6
    ## 28  2019-20    Cleveland Cavaliers 14.7
    ## 33  2019-20       Dallas Mavericks 14.2
    ## 38  2019-20         Denver Nuggets 14.0
    ## 43  2019-20        Detroit Pistons 11.1
    ## 48  2019-20  Golden State Warriors 13.3
    ## 53  2019-20        Houston Rockets 16.5
    ## 58  2019-20         Indiana Pacers 13.7
    ## 63  2019-20            LA Clippers 13.4
    ## 68  2019-20     Los Angeles Lakers 14.5
    ## 73  2019-20      Memphis Grizzlies 13.1
    ## 78  2019-20             Miami Heat 14.4
    ## 83  2019-20        Milwaukee Bucks 12.6
    ## 88  2019-20 Minnesota Timberwolves 10.7
    ## 93  2019-20   New Orleans Pelicans 13.3
    ## 98  2019-20        New York Knicks 10.8
    ## 103 2019-20  Oklahoma City Thunder 13.7
    ## 108 2019-20          Orlando Magic 13.2
    ## 113 2019-20     Philadelphia 76ers 12.9
    ## 118 2019-20           Phoenix Suns 13.6
    ## 123 2019-20 Portland Trail Blazers 15.2
    ## 128 2019-20       Sacramento Kings 13.8
    ## 133 2019-20      San Antonio Spurs 12.7
    ## 138 2019-20        Toronto Raptors 15.3
    ## 143 2019-20              Utah Jazz 13.4
    ## 148 2019-20     Washington Wizards 13.0
    ## 4   2020-21          Atlanta Hawks 16.1
    ## 9   2020-21         Boston Celtics 13.8
    ## 14  2020-21          Brooklyn Nets 13.5
    ## 19  2020-21      Charlotte Hornets 12.5
    ## 24  2020-21          Chicago Bulls 15.0
    ## 29  2020-21    Cleveland Cavaliers 13.8
    ## 34  2020-21       Dallas Mavericks 13.3
    ## 39  2020-21         Denver Nuggets 16.8
    ## 44  2020-21        Detroit Pistons 12.8
    ## 49  2020-21  Golden State Warriors 13.3
    ## 54  2020-21        Houston Rockets 12.7
    ## 59  2020-21         Indiana Pacers 14.8
    ## 64  2020-21            LA Clippers 15.0
    ## 69  2020-21     Los Angeles Lakers 10.2
    ## 74  2020-21      Memphis Grizzlies 14.2
    ## 79  2020-21             Miami Heat 15.6
    ## 84  2020-21        Milwaukee Bucks 14.1
    ## 89  2020-21 Minnesota Timberwolves 10.5
    ## 94  2020-21   New Orleans Pelicans 15.0
    ## 99  2020-21        New York Knicks 13.1
    ## 104 2020-21  Oklahoma City Thunder 10.5
    ## 109 2020-21          Orlando Magic 10.9
    ## 114 2020-21     Philadelphia 76ers 13.6
    ## 119 2020-21           Phoenix Suns 15.1
    ## 124 2020-21 Portland Trail Blazers 14.9
    ## 129 2020-21       Sacramento Kings 16.8
    ## 134 2020-21      San Antonio Spurs 13.3
    ## 139 2020-21        Toronto Raptors 12.2
    ## 144 2020-21              Utah Jazz 14.4
    ## 149 2020-21     Washington Wizards 13.5
    ## 5   2021-22          Atlanta Hawks 16.1
    ## 10  2021-22         Boston Celtics 16.6
    ## 15  2021-22          Brooklyn Nets 11.5
    ## 20  2021-22      Charlotte Hornets 16.8
    ## 25  2021-22          Chicago Bulls 15.8
    ## 30  2021-22    Cleveland Cavaliers 14.2
    ## 35  2021-22       Dallas Mavericks 13.2
    ## 40  2021-22         Denver Nuggets 13.5
    ## 45  2021-22        Detroit Pistons 13.2
    ## 50  2021-22  Golden State Warriors 12.6
    ## 55  2021-22        Houston Rockets 13.2
    ## 60  2021-22         Indiana Pacers 15.1
    ## 65  2021-22            LA Clippers 13.0
    ## 70  2021-22     Los Angeles Lakers 11.9
    ## 75  2021-22      Memphis Grizzlies 13.1
    ## 80  2021-22             Miami Heat 12.2
    ## 85  2021-22        Milwaukee Bucks 16.3
    ## 90  2021-22 Minnesota Timberwolves 13.4
    ## 95  2021-22   New Orleans Pelicans 13.1
    ## 100 2021-22        New York Knicks 14.4
    ## 105 2021-22  Oklahoma City Thunder 10.4
    ## 110 2021-22          Orlando Magic 12.9
    ## 115 2021-22     Philadelphia 76ers 16.3
    ## 120 2021-22           Phoenix Suns 14.7
    ## 125 2021-22 Portland Trail Blazers  8.9
    ## 130 2021-22       Sacramento Kings 15.4
    ## 135 2021-22      San Antonio Spurs 14.5
    ## 140 2021-22        Toronto Raptors 15.4
    ## 145 2021-22              Utah Jazz 13.9
    ## 150 2021-22     Washington Wizards 11.8

<h4>
Preparing data for plotting
</h4>

``` r
merged_team_eff <- merge(df_standing, avg_EFF, by = c("Season", "Team"))
merged_team_eff <- merged_team_eff[order(merged_team_eff$Season, 
                                         merged_team_eff$Rank, 
                                       desc(merged_team_eff$W)),]
merged_team_eff
```

    ##      Season                   Team Conference Rank  W  L  WIN.  EFF
    ## 11  2017-18        Houston Rockets    Western    1 65 17 0.793 15.3
    ## 28  2017-18        Toronto Raptors    Eastern    1 59 23 0.720 12.3
    ## 10  2017-18  Golden State Warriors    Western    2 58 24 0.707 12.3
    ## 2   2017-18         Boston Celtics    Eastern    2 55 27 0.671 13.0
    ## 23  2017-18     Philadelphia 76ers    Eastern    3 52 30 0.634 15.3
    ## 25  2017-18 Portland Trail Blazers    Western    3 49 33 0.598 12.2
    ## 6   2017-18    Cleveland Cavaliers    Eastern    4 50 32 0.610 13.5
    ## 21  2017-18  Oklahoma City Thunder    Western    4 48 34 0.585 11.1
    ## 12  2017-18         Indiana Pacers    Eastern    5 48 34 0.585 14.1
    ## 29  2017-18              Utah Jazz    Western    5 48 34 0.585 11.2
    ## 19  2017-18   New Orleans Pelicans    Western    6 48 34 0.585 15.9
    ## 16  2017-18             Miami Heat    Eastern    6 44 38 0.537 12.6
    ## 27  2017-18      San Antonio Spurs    Western    7 47 35 0.573 10.7
    ## 17  2017-18        Milwaukee Bucks    Eastern    7 44 38 0.537 15.2
    ## 18  2017-18 Minnesota Timberwolves    Western    8 47 35 0.573 14.8
    ## 30  2017-18     Washington Wizards    Eastern    8 43 39 0.524 11.6
    ## 8   2017-18         Denver Nuggets    Western    9 46 36 0.561 13.5
    ## 9   2017-18        Detroit Pistons    Eastern    9 39 43 0.476 11.5
    ## 13  2017-18            LA Clippers    Western   10 42 40 0.512 12.8
    ## 4   2017-18      Charlotte Hornets    Eastern   10 36 46 0.439 12.4
    ## 14  2017-18     Los Angeles Lakers    Western   11 35 47 0.427 14.5
    ## 20  2017-18        New York Knicks    Eastern   11 29 53 0.354 11.2
    ## 3   2017-18          Brooklyn Nets    Eastern   12 28 54 0.341 12.1
    ## 26  2017-18       Sacramento Kings    Western   12 27 55 0.329 11.4
    ## 5   2017-18          Chicago Bulls    Eastern   13 27 55 0.329 12.6
    ## 7   2017-18       Dallas Mavericks    Western   13 24 58 0.293 11.5
    ## 22  2017-18          Orlando Magic    Eastern   14 25 57 0.305  9.5
    ## 15  2017-18      Memphis Grizzlies    Western   14 22 60 0.268 11.1
    ## 1   2017-18          Atlanta Hawks    Eastern   15 24 58 0.293 13.5
    ## 24  2017-18           Phoenix Suns    Western   15 21 61 0.256 11.3
    ## 47  2018-19        Milwaukee Bucks    Eastern    1 60 22 0.732 14.1
    ## 40  2018-19  Golden State Warriors    Western    1 57 25 0.695 13.3
    ## 58  2018-19        Toronto Raptors    Eastern    2 58 24 0.707 15.5
    ## 38  2018-19         Denver Nuggets    Western    2 54 28 0.659 13.7
    ## 55  2018-19 Portland Trail Blazers    Western    3 53 29 0.646 13.5
    ## 53  2018-19     Philadelphia 76ers    Eastern    3 51 31 0.622 16.5
    ## 41  2018-19        Houston Rockets    Western    4 53 29 0.646 15.7
    ## 32  2018-19         Boston Celtics    Eastern    4 49 33 0.598 14.8
    ## 59  2018-19              Utah Jazz    Western    5 50 32 0.610 13.8
    ## 42  2018-19         Indiana Pacers    Eastern    5 48 34 0.585 12.6
    ## 51  2018-19  Oklahoma City Thunder    Western    6 49 33 0.598 13.9
    ## 33  2018-19          Brooklyn Nets    Eastern    6 42 40 0.512 12.7
    ## 57  2018-19      San Antonio Spurs    Western    7 48 34 0.585 13.3
    ## 52  2018-19          Orlando Magic    Eastern    7 42 40 0.512 13.8
    ## 43  2018-19            LA Clippers    Western    8 48 34 0.585 11.4
    ## 39  2018-19        Detroit Pistons    Eastern    8 41 41 0.500 12.5
    ## 34  2018-19      Charlotte Hornets    Eastern    9 39 43 0.476 12.5
    ## 56  2018-19       Sacramento Kings    Western    9 39 43 0.476 13.7
    ## 46  2018-19             Miami Heat    Eastern   10 39 43 0.476 14.2
    ## 44  2018-19     Los Angeles Lakers    Western   10 37 45 0.451 11.4
    ## 48  2018-19 Minnesota Timberwolves    Western   11 36 46 0.439 13.1
    ## 60  2018-19     Washington Wizards    Eastern   11 32 50 0.390 16.0
    ## 45  2018-19      Memphis Grizzlies    Western   12 33 49 0.402 13.3
    ## 31  2018-19          Atlanta Hawks    Eastern   12 29 53 0.354 13.7
    ## 49  2018-19   New Orleans Pelicans    Western   13 33 49 0.402 11.7
    ## 35  2018-19          Chicago Bulls    Eastern   13 22 60 0.268 10.3
    ## 37  2018-19       Dallas Mavericks    Western   14 33 49 0.402 11.3
    ## 36  2018-19    Cleveland Cavaliers    Eastern   14 19 63 0.232 11.9
    ## 54  2018-19           Phoenix Suns    Western   15 19 63 0.232 14.4
    ## 50  2018-19        New York Knicks    Eastern   15 17 65 0.207 12.7
    ## 77  2019-20        Milwaukee Bucks    Eastern    1 56 17 0.767 12.6
    ## 74  2019-20     Los Angeles Lakers    Western    1 52 19 0.732 14.5
    ## 88  2019-20        Toronto Raptors    Eastern    2 53 19 0.736 15.3
    ## 73  2019-20            LA Clippers    Western    2 49 23 0.681 13.4
    ## 62  2019-20         Boston Celtics    Eastern    3 48 24 0.667 14.2
    ## 68  2019-20         Denver Nuggets    Western    3 46 27 0.630 14.0
    ## 72  2019-20         Indiana Pacers    Eastern    4 45 28 0.616 13.7
    ## 71  2019-20        Houston Rockets    Western    4 44 28 0.611 16.5
    ## 76  2019-20             Miami Heat    Eastern    5 44 29 0.603 14.4
    ## 81  2019-20  Oklahoma City Thunder    Western    5 44 28 0.611 13.7
    ## 89  2019-20              Utah Jazz    Western    6 44 28 0.611 13.4
    ## 83  2019-20     Philadelphia 76ers    Eastern    6 43 30 0.589 12.9
    ## 67  2019-20       Dallas Mavericks    Western    7 43 32 0.573 14.2
    ## 63  2019-20          Brooklyn Nets    Eastern    7 35 37 0.486 15.2
    ## 85  2019-20 Portland Trail Blazers    Western    8 35 39 0.473 15.2
    ## 82  2019-20          Orlando Magic    Eastern    8 33 40 0.452 13.2
    ## 75  2019-20      Memphis Grizzlies    Western    9 34 39 0.466 13.1
    ## 90  2019-20     Washington Wizards    Eastern    9 25 47 0.347 13.0
    ## 84  2019-20           Phoenix Suns    Western   10 34 39 0.466 13.6
    ## 64  2019-20      Charlotte Hornets    Eastern   10 23 42 0.354 12.8
    ## 87  2019-20      San Antonio Spurs    Western   11 32 39 0.451 12.7
    ## 65  2019-20          Chicago Bulls    Eastern   11 22 43 0.338 12.6
    ## 86  2019-20       Sacramento Kings    Western   12 31 41 0.431 13.8
    ## 80  2019-20        New York Knicks    Eastern   12 21 45 0.318 10.8
    ## 79  2019-20   New Orleans Pelicans    Western   13 30 42 0.417 13.3
    ## 69  2019-20        Detroit Pistons    Eastern   13 20 46 0.303 11.1
    ## 61  2019-20          Atlanta Hawks    Eastern   14 20 47 0.299 10.9
    ## 78  2019-20 Minnesota Timberwolves    Western   14 19 45 0.297 10.7
    ## 66  2019-20    Cleveland Cavaliers    Eastern   15 19 46 0.292 14.7
    ## 70  2019-20  Golden State Warriors    Western   15 15 50 0.231 13.3
    ## 119 2020-21              Utah Jazz    Western    1 52 20 0.722 14.4
    ## 113 2020-21     Philadelphia 76ers    Eastern    1 49 23 0.681 13.6
    ## 114 2020-21           Phoenix Suns    Western    2 51 21 0.708 15.1
    ## 93  2020-21          Brooklyn Nets    Eastern    2 48 24 0.667 13.5
    ## 98  2020-21         Denver Nuggets    Western    3 47 25 0.653 16.8
    ## 107 2020-21        Milwaukee Bucks    Eastern    3 46 26 0.639 14.1
    ## 103 2020-21            LA Clippers    Western    4 47 25 0.653 15.0
    ## 110 2020-21        New York Knicks    Eastern    4 41 31 0.569 13.1
    ## 97  2020-21       Dallas Mavericks    Western    5 42 30 0.583 13.3
    ## 91  2020-21          Atlanta Hawks    Eastern    5 41 31 0.569 16.1
    ## 115 2020-21 Portland Trail Blazers    Western    6 42 30 0.583 14.9
    ## 106 2020-21             Miami Heat    Eastern    6 40 32 0.556 15.6
    ## 104 2020-21     Los Angeles Lakers    Western    7 42 30 0.583 10.2
    ## 92  2020-21         Boston Celtics    Eastern    7 36 36 0.500 13.8
    ## 105 2020-21      Memphis Grizzlies    Western    8 38 34 0.528 14.2
    ## 120 2020-21     Washington Wizards    Eastern    8 34 38 0.472 13.5
    ## 100 2020-21  Golden State Warriors    Western    9 39 33 0.542 13.3
    ## 102 2020-21         Indiana Pacers    Eastern    9 34 38 0.472 14.8
    ## 94  2020-21      Charlotte Hornets    Eastern   10 33 39 0.458 12.5
    ## 117 2020-21      San Antonio Spurs    Western   10 33 39 0.458 13.3
    ## 95  2020-21          Chicago Bulls    Eastern   11 31 41 0.431 15.0
    ## 109 2020-21   New Orleans Pelicans    Western   11 31 41 0.431 15.0
    ## 116 2020-21       Sacramento Kings    Western   12 31 41 0.431 16.8
    ## 118 2020-21        Toronto Raptors    Eastern   12 27 45 0.375 12.2
    ## 108 2020-21 Minnesota Timberwolves    Western   13 23 49 0.319 10.5
    ## 96  2020-21    Cleveland Cavaliers    Eastern   13 22 50 0.306 13.8
    ## 111 2020-21  Oklahoma City Thunder    Western   14 22 50 0.306 10.5
    ## 112 2020-21          Orlando Magic    Eastern   14 21 51 0.292 10.9
    ## 99  2020-21        Detroit Pistons    Eastern   15 20 52 0.278 12.8
    ## 101 2020-21        Houston Rockets    Western   15 17 55 0.236 12.7
    ## 144 2021-22           Phoenix Suns    Western    1 64 18 0.780 14.7
    ## 136 2021-22             Miami Heat    Eastern    1 53 29 0.646 12.2
    ## 135 2021-22      Memphis Grizzlies    Western    2 56 26 0.683 13.1
    ## 122 2021-22         Boston Celtics    Eastern    2 51 31 0.622 16.6
    ## 130 2021-22  Golden State Warriors    Western    3 53 29 0.646 12.6
    ## 137 2021-22        Milwaukee Bucks    Eastern    3 51 31 0.622 16.3
    ## 127 2021-22       Dallas Mavericks    Western    4 52 30 0.634 13.2
    ## 143 2021-22     Philadelphia 76ers    Eastern    4 51 31 0.622 16.3
    ## 149 2021-22              Utah Jazz    Western    5 49 33 0.598 13.9
    ## 148 2021-22        Toronto Raptors    Eastern    5 48 34 0.585 15.4
    ## 128 2021-22         Denver Nuggets    Western    6 48 34 0.585 13.5
    ## 125 2021-22          Chicago Bulls    Eastern    6 46 36 0.561 15.8
    ## 138 2021-22 Minnesota Timberwolves    Western    7 46 36 0.561 13.4
    ## 123 2021-22          Brooklyn Nets    Eastern    7 44 38 0.537 11.5
    ## 121 2021-22          Atlanta Hawks    Eastern    8 43 39 0.524 16.1
    ## 139 2021-22   New Orleans Pelicans    Western    8 36 46 0.439 13.1
    ## 126 2021-22    Cleveland Cavaliers    Eastern    9 44 38 0.537 14.2
    ## 133 2021-22            LA Clippers    Western    9 42 40 0.512 13.0
    ## 124 2021-22      Charlotte Hornets    Eastern   10 43 39 0.524 16.8
    ## 147 2021-22      San Antonio Spurs    Western   10 34 48 0.415 14.5
    ## 140 2021-22        New York Knicks    Eastern   11 37 45 0.451 14.4
    ## 134 2021-22     Los Angeles Lakers    Western   11 33 49 0.402 11.9
    ## 150 2021-22     Washington Wizards    Eastern   12 35 47 0.427 11.8
    ## 146 2021-22       Sacramento Kings    Western   12 30 52 0.366 15.4
    ## 145 2021-22 Portland Trail Blazers    Western   13 27 55 0.329  8.9
    ## 132 2021-22         Indiana Pacers    Eastern   13 25 57 0.305 15.1
    ## 141 2021-22  Oklahoma City Thunder    Western   14 24 58 0.293 10.4
    ## 129 2021-22        Detroit Pistons    Eastern   14 23 59 0.280 13.2
    ## 142 2021-22          Orlando Magic    Eastern   15 22 60 0.268 12.9
    ## 131 2021-22        Houston Rockets    Western   15 20 62 0.244 13.2

``` r
t <- ggplot(data=merged_team_eff)
t + ggtitle("Average Efficiency by Team Rank 2017-2022") +
  geom_point(aes(x=Rank, y=EFF),size=3, color="#FE6244") +
  geom_smooth(aes(x=Rank, y=EFF), fill=NA) +
  scale_x_continuous(breaks = seq(0, 15, by = 1)) +
  scale_y_continuous(breaks = seq(7.5, 20, by = 2.5)) +
  theme(axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
        plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'loess' and formula = 'y ~ x'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->
<h4>
Aggregated data by team field goal percentage
</h4>

``` r
avg_fg <- aggregate(FG.~Season + Team, df_player, FUN=mean)
avg_fg$FG. <- round(avg_fg$FG., 1)
avg_fg <- avg_fg[order(avg_fg$Season), ]
avg_fg
```

    ##      Season                   Team  FG.
    ## 1   2017-18          Atlanta Hawks 46.7
    ## 6   2017-18         Boston Celtics 45.9
    ## 11  2017-18          Brooklyn Nets 44.5
    ## 16  2017-18      Charlotte Hornets 44.9
    ## 21  2017-18          Chicago Bulls 44.5
    ## 26  2017-18    Cleveland Cavaliers 47.4
    ## 31  2017-18       Dallas Mavericks 47.6
    ## 36  2017-18         Denver Nuggets 47.2
    ## 41  2017-18        Detroit Pistons 47.5
    ## 46  2017-18  Golden State Warriors 51.7
    ## 51  2017-18        Houston Rockets 46.3
    ## 56  2017-18         Indiana Pacers 47.7
    ## 61  2017-18            LA Clippers 49.1
    ## 66  2017-18     Los Angeles Lakers 47.3
    ## 71  2017-18      Memphis Grizzlies 45.9
    ## 76  2017-18             Miami Heat 45.7
    ## 81  2017-18        Milwaukee Bucks 49.2
    ## 86  2017-18 Minnesota Timberwolves 47.7
    ## 91  2017-18   New Orleans Pelicans 48.3
    ## 96  2017-18        New York Knicks 46.2
    ## 101 2017-18  Oklahoma City Thunder 44.0
    ## 106 2017-18          Orlando Magic 45.6
    ## 111 2017-18     Philadelphia 76ers 47.6
    ## 116 2017-18           Phoenix Suns 44.7
    ## 121 2017-18 Portland Trail Blazers 45.5
    ## 126 2017-18       Sacramento Kings 46.2
    ## 131 2017-18      San Antonio Spurs 44.6
    ## 136 2017-18        Toronto Raptors 47.7
    ## 141 2017-18              Utah Jazz 45.4
    ## 146 2017-18     Washington Wizards 47.6
    ## 2   2018-19          Atlanta Hawks 45.6
    ## 7   2018-19         Boston Celtics 46.8
    ## 12  2018-19          Brooklyn Nets 47.3
    ## 17  2018-19      Charlotte Hornets 44.9
    ## 22  2018-19          Chicago Bulls 47.5
    ## 27  2018-19    Cleveland Cavaliers 46.3
    ## 32  2018-19       Dallas Mavericks 44.7
    ## 37  2018-19         Denver Nuggets 47.7
    ## 42  2018-19        Detroit Pistons 43.6
    ## 47  2018-19  Golden State Warriors 49.8
    ## 52  2018-19        Houston Rockets 43.7
    ## 57  2018-19         Indiana Pacers 48.0
    ## 62  2018-19            LA Clippers 45.5
    ## 67  2018-19     Los Angeles Lakers 45.1
    ## 72  2018-19      Memphis Grizzlies 43.4
    ## 77  2018-19             Miami Heat 48.3
    ## 82  2018-19        Milwaukee Bucks 47.1
    ## 87  2018-19 Minnesota Timberwolves 45.2
    ## 92  2018-19   New Orleans Pelicans 47.6
    ## 97  2018-19        New York Knicks 48.7
    ## 102 2018-19  Oklahoma City Thunder 46.1
    ## 107 2018-19          Orlando Magic 44.5
    ## 112 2018-19     Philadelphia 76ers 49.4
    ## 117 2018-19           Phoenix Suns 47.8
    ## 122 2018-19 Portland Trail Blazers 48.0
    ## 127 2018-19       Sacramento Kings 46.4
    ## 132 2018-19      San Antonio Spurs 48.5
    ## 137 2018-19        Toronto Raptors 46.8
    ## 142 2018-19              Utah Jazz 47.8
    ## 147 2018-19     Washington Wizards 49.0
    ## 3   2019-20          Atlanta Hawks 44.3
    ## 8   2019-20         Boston Celtics 46.4
    ## 13  2019-20          Brooklyn Nets 49.5
    ## 18  2019-20      Charlotte Hornets 45.2
    ## 23  2019-20          Chicago Bulls 42.9
    ## 28  2019-20    Cleveland Cavaliers 45.9
    ## 33  2019-20       Dallas Mavericks 46.5
    ## 38  2019-20         Denver Nuggets 48.6
    ## 43  2019-20        Detroit Pistons 46.7
    ## 48  2019-20  Golden State Warriors 44.8
    ## 53  2019-20        Houston Rockets 43.5
    ## 58  2019-20         Indiana Pacers 47.6
    ## 63  2019-20            LA Clippers 45.9
    ## 68  2019-20     Los Angeles Lakers 50.4
    ## 73  2019-20      Memphis Grizzlies 47.0
    ## 78  2019-20             Miami Heat 45.8
    ## 83  2019-20        Milwaukee Bucks 46.1
    ## 88  2019-20 Minnesota Timberwolves 42.0
    ## 93  2019-20   New Orleans Pelicans 47.4
    ## 98  2019-20        New York Knicks 47.8
    ## 103 2019-20  Oklahoma City Thunder 48.4
    ## 108 2019-20          Orlando Magic 44.1
    ## 113 2019-20     Philadelphia 76ers 45.7
    ## 118 2019-20           Phoenix Suns 44.9
    ## 123 2019-20 Portland Trail Blazers 45.9
    ## 128 2019-20       Sacramento Kings 45.4
    ## 133 2019-20      San Antonio Spurs 46.6
    ## 138 2019-20        Toronto Raptors 46.6
    ## 143 2019-20              Utah Jazz 49.9
    ## 148 2019-20     Washington Wizards 43.7
    ## 4   2020-21          Atlanta Hawks 46.0
    ## 9   2020-21         Boston Celtics 49.5
    ## 14  2020-21          Brooklyn Nets 51.4
    ## 19  2020-21      Charlotte Hornets 44.4
    ## 24  2020-21          Chicago Bulls 47.6
    ## 29  2020-21    Cleveland Cavaliers 46.1
    ## 34  2020-21       Dallas Mavericks 50.3
    ## 39  2020-21         Denver Nuggets 47.6
    ## 44  2020-21        Detroit Pistons 46.8
    ## 49  2020-21  Golden State Warriors 47.7
    ## 54  2020-21        Houston Rockets 45.8
    ## 59  2020-21         Indiana Pacers 48.7
    ## 64  2020-21            LA Clippers 50.0
    ## 69  2020-21     Los Angeles Lakers 44.1
    ## 74  2020-21      Memphis Grizzlies 48.2
    ## 79  2020-21             Miami Heat 48.0
    ## 84  2020-21        Milwaukee Bucks 47.2
    ## 89  2020-21 Minnesota Timberwolves 45.4
    ## 94  2020-21   New Orleans Pelicans 49.8
    ## 99  2020-21        New York Knicks 46.8
    ## 104 2020-21  Oklahoma City Thunder 43.0
    ## 109 2020-21          Orlando Magic 44.7
    ## 114 2020-21     Philadelphia 76ers 46.7
    ## 119 2020-21           Phoenix Suns 48.5
    ## 124 2020-21 Portland Trail Blazers 46.5
    ## 129 2020-21       Sacramento Kings 48.3
    ## 134 2020-21      San Antonio Spurs 47.4
    ## 139 2020-21        Toronto Raptors 44.0
    ## 144 2020-21              Utah Jazz 47.8
    ## 149 2020-21     Washington Wizards 50.3
    ## 5   2021-22          Atlanta Hawks 47.4
    ## 10  2021-22         Boston Celtics 48.4
    ## 15  2021-22          Brooklyn Nets 47.9
    ## 20  2021-22      Charlotte Hornets 50.5
    ## 25  2021-22          Chicago Bulls 48.1
    ## 30  2021-22    Cleveland Cavaliers 46.1
    ## 35  2021-22       Dallas Mavericks 46.9
    ## 40  2021-22         Denver Nuggets 46.5
    ## 45  2021-22        Detroit Pistons 44.1
    ## 50  2021-22  Golden State Warriors 49.1
    ## 55  2021-22        Houston Rockets 45.8
    ## 60  2021-22         Indiana Pacers 43.0
    ## 65  2021-22            LA Clippers 48.9
    ## 70  2021-22     Los Angeles Lakers 46.7
    ## 75  2021-22      Memphis Grizzlies 48.1
    ## 80  2021-22             Miami Heat 46.3
    ## 85  2021-22        Milwaukee Bucks 45.9
    ## 90  2021-22 Minnesota Timberwolves 46.2
    ## 95  2021-22   New Orleans Pelicans 46.1
    ## 100 2021-22        New York Knicks 47.3
    ## 105 2021-22  Oklahoma City Thunder 40.8
    ## 110 2021-22          Orlando Magic 43.9
    ## 115 2021-22     Philadelphia 76ers 44.9
    ## 120 2021-22           Phoenix Suns 48.4
    ## 125 2021-22 Portland Trail Blazers 46.3
    ## 130 2021-22       Sacramento Kings 46.4
    ## 135 2021-22      San Antonio Spurs 47.8
    ## 140 2021-22        Toronto Raptors 44.5
    ## 145 2021-22              Utah Jazz 49.3
    ## 150 2021-22     Washington Wizards 48.0

<h4>
Merged average FG. with team standing data
</h4>

``` r
merged_team_fg <- merge(df_standing, avg_fg, by = c("Season", "Team"))
merged_team_fg <- merged_team_fg[order(merged_team_fg$Season, 
                                       merged_team_fg$Rank, 
                                       desc(merged_team_fg$W)),]
```

``` r
# plotting to see the trend between field goal percentage and rank of the team
q <- ggplot(data=merged_team_fg)

q + ggtitle("Average Field goal percentage by Team Rank 2017-2022") +
  geom_point(aes(x=Rank, y=FG.),size=3, color="#FE6244") +
  geom_smooth(aes(x=Rank, y=FG.), fill=NA) +
  scale_x_continuous(breaks = seq(0, 15, by = 1)) +
  scale_y_continuous(breaks = seq(37.5, 55, by = 2.5)) +
  theme(axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
        plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'loess' and formula = 'y ~ x'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->
<h4>
Average rank by each team 2017-2022
</h4>

``` r
average_rank <- aggregate(Rank~Team, df_standing, FUN=mean)
average_rank <- average_rank[order(average_rank$Rank),]
average_rank
```

    ##                      Team Rank
    ## 17        Milwaukee Bucks  3.0
    ## 23     Philadelphia 76ers  3.4
    ## 2          Boston Celtics  3.6
    ## 28        Toronto Raptors  4.4
    ## 29              Utah Jazz  4.4
    ## 8          Denver Nuggets  4.6
    ## 16             Miami Heat  5.6
    ## 10  Golden State Warriors  6.0
    ## 13            LA Clippers  6.6
    ## 25 Portland Trail Blazers  6.6
    ## 3           Brooklyn Nets  6.8
    ## 12         Indiana Pacers  7.2
    ## 11        Houston Rockets  7.8
    ## 14     Los Angeles Lakers  8.0
    ## 7        Dallas Mavericks  8.6
    ## 21  Oklahoma City Thunder  8.6
    ## 24           Phoenix Suns  8.6
    ## 15      Memphis Grizzlies  9.0
    ## 27      San Antonio Spurs  9.0
    ## 30     Washington Wizards  9.6
    ## 4       Charlotte Hornets  9.8
    ## 19   New Orleans Pelicans 10.2
    ## 18 Minnesota Timberwolves 10.6
    ## 20        New York Knicks 10.6
    ## 1           Atlanta Hawks 10.8
    ## 5           Chicago Bulls 10.8
    ## 6     Cleveland Cavaliers 11.0
    ## 26       Sacramento Kings 11.4
    ## 22          Orlando Magic 11.6
    ## 9         Detroit Pistons 11.8

``` r
p <- ggplot(data=df_player)

# if player have higher free throw attempt, are they more likely to get more points
p + ggtitle("Free throw attempt by pts with trend line 2017-2022") +
  geom_point(aes(x=PTS,y=FTA), colour="#FC2947") +
  geom_smooth(aes(x=PTS,y=FTA), fill=NA, colour="#7149C6", alpha = 0.3) +
  theme(axis.title.x=element_text(size=7),
        axis.title.y=element_text(size=7),
        axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
    plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'gam' and formula = 'y ~ s(x, bs = "cs")'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-18-1.png)<!-- -->

``` r
# trend between FG. and PTS
p + ggtitle("FG. by PTS with trend line 2017-2022") +
  geom_point(aes(x=FG., y=PTS, colour=PTS), colour="#98DFD6", size = 2) +
  geom_smooth(aes(x=FG., y = PTS), fill=NA) + 
  coord_cartesian(xlim=c(34,75), ylim=c(0,40)) +
  theme(axis.title.x=element_text(size=7),
        axis.title.y=element_text(size=7),
        axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
    plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'gam' and formula = 'y ~ s(x, bs = "cs")'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-19-1.png)<!-- -->

``` r
# trend between true shooting percentage and points
p + ggtitle("TS by EFG over 2017-2022") +
  geom_point(aes(x=TS, y=EFG), color="#7AA874") + 
  geom_smooth(aes(x=TS, y=EFG), fill=NA) +
  theme(axis.title.x=element_text(size=7),
        axis.title.y=element_text(size=7),
        axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
    plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'gam' and formula = 'y ~ s(x, bs = "cs")'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-20-1.png)<!-- -->

``` r
p + ggtitle("Distribution of PPM by player 2017-2022") +
  geom_histogram(binwidth=0.01, aes(x=PPM), fill="#9A208C",colour="#F5C6EC") +
  theme(axis.title.x=element_text(size=7),
        axis.title.y=element_text(size=7),
        axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
        plot.title = element_text(size=15, face="bold"))
```

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-21-1.png)<!-- -->

``` r
# more points more turnover and more assist?
p + ggtitle("Scatterplot of points by AST / TOV") +
  ylab("TOV / AST") +
  geom_point(aes(x=PTS, y=TOV, color="TOV")) + 
  geom_smooth(aes(x=PTS, y=TOV, color="TOV")) + 
  geom_point(aes(x=PTS, y=AST, color="AST")) + 
  geom_smooth(aes(x=PTS, y=AST, color="AST")) +
  coord_cartesian(xlim=c(0,35), ylim=c(0,12)) +
  scale_color_manual(name = "", values = c("TOV" = "#82AAE3", "AST" = "#F7DB6A")) +
  theme(axis.title.x=element_text(size=7),
        axis.title.y=element_text(size=7),
        axis.text.x=element_text(size=7),
        axis.text.y=element_text(size=7),
        plot.title = element_text(size=15, face="bold"))
```

    ## `geom_smooth()` using method = 'gam' and formula = 'y ~ s(x, bs = "cs")'
    ## `geom_smooth()` using method = 'gam' and formula = 'y ~ s(x, bs = "cs")'

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-22-1.png)<!-- -->

``` r
# player with average eff of top 20 over past 5 seasons. 
avg_eff_by_player <- aggregate(EFF~Player, df_player,FUN=mean)
avg_eff_by_player <- avg_eff_by_player[order(desc(avg_eff_by_player$EFF)),]
avg_eff_by_player$EFF <- round(avg_eff_by_player$EFF,1)
top20_eff_by_player <- head(avg_eff_by_player, 20)
filter <- df_player$Player %in% top20_eff_by_player$Player
top_20_players <- df_player[filter,]
top_20_players <- top_20_players[order(top_20_players$Player),]
top_20_players
```

    ##       Season                 Player                   Team GP  MIN  PTS  FGM
    ## 49   2017-18        Andre Drummond         Detroit Pistons 78 33.7 15.0  6.0
    ## 296  2018-19        Andre Drummond         Detroit Pistons 79 33.5 17.3  7.1
    ## 563  2019-20        Andre Drummond     Cleveland Cavaliers 57 32.9 17.7  7.3
    ## 1183 2021-22        Andre Drummond           Brooklyn Nets 73 19.7  7.9  3.4
    ## 2    2017-18         Anthony Davis    New Orleans Pelicans 75 36.4 28.1 10.4
    ## 521  2019-20         Anthony Davis      Los Angeles Lakers 62 34.4 26.1  8.9
    ## 4    2017-18        Damian Lillard  Portland Trail Blazers 73 36.6 26.9  8.5
    ## 262  2018-19        Damian Lillard  Portland Trail Blazers 80 35.5 25.8  8.5
    ## 514  2019-20        Damian Lillard  Portland Trail Blazers 66 37.5 30.0  9.5
    ## 775  2020-21        Damian Lillard  Portland Trail Blazers 67 35.8 28.8  9.0
    ## 5    2017-18 Giannis Antetokounmpo         Milwaukee Bucks 75 36.7 26.9  9.9
    ## 256  2018-19 Giannis Antetokounmpo         Milwaukee Bucks 72 32.8 27.7 10.0
    ## 516  2019-20 Giannis Antetokounmpo         Milwaukee Bucks 63 30.4 29.5 10.9
    ## 777  2020-21 Giannis Antetokounmpo         Milwaukee Bucks 61 33.0 28.1 10.3
    ## 1011 2021-22 Giannis Antetokounmpo         Milwaukee Bucks 67 32.9 29.9 10.3
    ## 1    2017-18          James Harden         Houston Rockets 72 35.4 30.4  9.0
    ## 254  2018-19          James Harden         Houston Rockets 78 36.8 36.1 10.8
    ## 512  2019-20          James Harden         Houston Rockets 68 36.5 34.3  9.9
    ## 1026 2021-22          James Harden      Philadelphia 76ers 65 37.2 22.0  6.3
    ## 15   2017-18          Jimmy Butler  Minnesota Timberwolves 59 36.7 22.2  7.4
    ## 288  2018-19          Jimmy Butler      Philadelphia 76ers 65 33.6 18.7  6.4
    ## 540  2019-20          Jimmy Butler              Miami Heat 58 33.8 19.9  5.9
    ## 798  2020-21          Jimmy Butler              Miami Heat 52 33.6 21.5  7.0
    ## 12   2017-18           Joel Embiid      Philadelphia 76ers 63 30.3 22.9  8.1
    ## 257  2018-19           Joel Embiid      Philadelphia 76ers 64 33.7 27.5  9.1
    ## 776  2020-21           Joel Embiid      Philadelphia 76ers 51 31.1 28.5  9.0
    ## 1010 2021-22           Joel Embiid      Philadelphia 76ers 68 33.8 30.6  9.8
    ## 19   2017-18    Karl-Anthony Towns  Minnesota Timberwolves 82 35.6 21.3  7.8
    ## 266  2018-19    Karl-Anthony Towns  Minnesota Timberwolves 77 33.1 24.4  8.8
    ## 1020 2021-22    Karl-Anthony Towns  Minnesota Timberwolves 74 33.4 24.6  8.7
    ## 259  2018-19         Kawhi Leonard         Toronto Raptors 60 34.0 26.6  9.3
    ## 519  2019-20         Kawhi Leonard             LA Clippers 57 32.4 27.1  9.3
    ## 788  2020-21         Kawhi Leonard             LA Clippers 52 34.1 24.8  8.9
    ## 6    2017-18          Kevin Durant   Golden State Warriors 68 34.2 26.4  9.3
    ## 261  2018-19          Kevin Durant   Golden State Warriors 78 34.6 26.0  9.2
    ## 8    2017-18          Kyrie Irving          Boston Celtics 60 32.2 24.4  8.9
    ## 267  2018-19          Kyrie Irving          Boston Celtics 67 33.0 23.8  9.0
    ## 781  2020-21          Kyrie Irving           Brooklyn Nets 54 34.9 26.9 10.2
    ## 3    2017-18          LeBron James     Cleveland Cavaliers 82 36.9 27.5 10.5
    ## 523  2019-20          LeBron James      Los Angeles Lakers 67 34.6 25.3  9.6
    ## 275  2018-19           Luka Doncic        Dallas Mavericks 72 32.2 21.2  7.0
    ## 517  2019-20           Luka Doncic        Dallas Mavericks 61 33.6 28.8  9.5
    ## 778  2020-21           Luka Doncic        Dallas Mavericks 66 34.3 27.7  9.8
    ## 1012 2021-22           Luka Doncic        Dallas Mavericks 65 35.4 28.4  9.9
    ## 28   2017-18          Nikola Jokic          Denver Nuggets 75 32.6 18.5  6.7
    ## 282  2018-19          Nikola Jokic          Denver Nuggets 80 31.3 20.1  7.7
    ## 541  2019-20          Nikola Jokic          Denver Nuggets 73 32.0 19.9  7.7
    ## 784  2020-21          Nikola Jokic          Denver Nuggets 72 34.6 26.4 10.2
    ## 1015 2021-22          Nikola Jokic          Denver Nuggets 74 33.5 27.1 10.3
    ## 280  2018-19        Nikola Vucevic           Orlando Magic 80 31.4 20.8  8.8
    ## 544  2019-20        Nikola Vucevic           Orlando Magic 62 32.2 19.6  8.0
    ## 793  2020-21        Nikola Vucevic           Chicago Bulls 70 33.5 23.4  9.5
    ## 1048 2021-22        Nikola Vucevic           Chicago Bulls 73 33.1 17.6  7.5
    ## 311  2018-19           Rudy Gobert               Utah Jazz 81 31.8 15.9  5.9
    ## 585  2019-20           Rudy Gobert               Utah Jazz 68 34.3 15.1  5.7
    ## 837  2020-21           Rudy Gobert               Utah Jazz 71 30.8 14.3  5.5
    ## 1066 2021-22           Rudy Gobert               Utah Jazz 66 32.1 15.6  5.5
    ## 7    2017-18     Russell Westbrook   Oklahoma City Thunder 80 36.4 25.4  9.5
    ## 270  2018-19     Russell Westbrook   Oklahoma City Thunder 73 36.0 22.9  8.6
    ## 518  2019-20     Russell Westbrook         Houston Rockets 57 35.9 27.2 10.6
    ## 796  2020-21     Russell Westbrook      Washington Wizards 65 36.4 22.2  8.4
    ## 1040 2021-22     Russell Westbrook      Los Angeles Lakers 78 34.3 18.5  7.0
    ## 258  2018-19         Stephen Curry   Golden State Warriors 69 33.8 27.3  9.2
    ## 773  2020-21         Stephen Curry   Golden State Warriors 63 34.2 32.0 10.4
    ## 1019 2021-22         Stephen Curry   Golden State Warriors 64 34.5 25.5  8.4
    ## 287  2018-19            Trae Young           Atlanta Hawks 81 30.9 19.1  6.5
    ## 515  2019-20            Trae Young           Atlanta Hawks 60 35.3 29.6  9.1
    ## 786  2020-21            Trae Young           Atlanta Hawks 63 33.7 25.3  7.7
    ## 1013 2021-22            Trae Young           Atlanta Hawks 76 34.9 28.4  9.4
    ## 780  2020-21       Zion Williamson    New Orleans Pelicans 61 33.2 27.0 10.4
    ##       FGA  FG. X3PM X3PA X3P.  FTM  FTA  FT. OREB DREB  REB  AST STL BLK TOV
    ## 49   11.3 52.9  0.0  0.1  0.0  3.1  5.1 60.5  5.1 10.9 16.0  3.0 1.5 1.6 2.6
    ## 296  13.3 53.3  0.1  0.5 13.2  3.1  5.2 59.0  5.4 10.2 15.6  1.4 1.7 1.7 2.2
    ## 563  13.8 53.3  0.1  0.6 14.3  3.0  5.2 57.5  4.4 10.8 15.2  2.7 1.9 1.6 3.6
    ## 1183  5.9 57.0  0.0  0.0  0.0  1.2  2.2 52.4  3.1  6.2  9.3  1.8 1.1 0.9 1.6
    ## 2    19.5 53.4  0.7  2.2 34.0  6.6  8.0 82.8  2.5  8.6 11.1  2.3 1.5 2.6 2.2
    ## 521  17.7 50.3  1.2  3.5 33.0  7.2  8.5 84.6  2.3  7.0  9.3  3.2 1.5 2.3 2.5
    ## 4    19.4 43.9  3.1  8.6 36.1  6.8  7.4 91.6  0.8  3.6  4.5  6.6 1.1 0.4 2.8
    ## 262  19.2 44.4  3.0  8.0 36.9  5.9  6.4 91.2  0.9  3.8  4.6  6.9 1.1 0.4 2.7
    ## 514  20.4 46.3  4.1 10.2 40.1  7.0  7.8 88.8  0.5  3.8  4.3  8.0 1.1 0.3 2.9
    ## 775  19.9 45.1  4.1 10.5 39.1  6.7  7.2 92.8  0.5  3.7  4.2  7.5 0.9 0.3 3.0
    ## 5    18.7 52.9  0.6  1.9 30.7  6.5  8.5 76.0  2.1  8.0 10.0  4.8 1.5 1.4 3.0
    ## 256  17.3 57.8  0.7  2.8 25.6  6.9  9.5 72.9  2.2 10.3 12.5  5.9 1.3 1.5 3.7
    ## 516  19.7 55.3  1.4  4.7 30.4  6.3 10.0 63.3  2.2 11.4 13.6  5.6 1.0 1.0 3.7
    ## 777  18.0 56.9  1.1  3.6 30.3  6.5  9.5 68.5  1.6  9.4 11.0  5.9 1.2 1.2 3.4
    ## 1011 18.6 55.3  1.1  3.6 29.3  8.3 11.4 72.2  2.0  9.6 11.6  5.8 1.1 1.4 3.3
    ## 1    20.1 44.9  3.7 10.0 36.7  8.7 10.1 85.8  0.6  4.8  5.4  8.8 1.8 0.7 4.4
    ## 254  24.5 44.2  4.8 13.2 36.8  9.7 11.0 87.9  0.8  5.8  6.6  7.5 2.0 0.7 5.0
    ## 512  22.3 44.4  4.4 12.4 35.5 10.2 11.8 86.5  1.0  5.5  6.6  7.5 1.8 0.9 4.5
    ## 1026 15.3 41.0  2.3  6.9 33.0  7.2  8.2 87.7  0.8  6.8  7.7 10.3 1.3 0.6 4.4
    ## 15   15.6 47.4  1.2  3.4 35.0  6.2  7.2 85.4  1.3  4.0  5.3  4.9 2.0 0.4 1.8
    ## 288  13.9 46.2  1.0  3.0 34.7  4.8  5.6 85.5  1.9  3.4  5.3  4.0 1.9 0.6 1.5
    ## 540  13.1 45.5  0.5  2.1 24.4  7.6  9.1 83.4  1.8  4.8  6.7  6.0 1.8 0.6 2.2
    ## 798  14.2 49.7  0.5  2.0 24.5  6.9  8.0 86.3  1.8  5.1  6.9  7.1 2.1 0.3 2.1
    ## 12   16.8 48.3  1.0  3.4 30.8  5.7  7.4 76.9  2.3  8.7 11.0  3.2 0.6 1.8 3.7
    ## 257  18.7 48.4  1.2  4.1 30.0  8.2 10.1 80.4  2.5 11.1 13.6  3.7 0.7 1.9 3.5
    ## 776  17.6 51.3  1.1  3.0 37.7  9.2 10.7 85.9  2.2  8.4 10.6  2.8 1.0 1.4 3.1
    ## 1010 19.6 49.9  1.4  3.7 37.1  9.6 11.8 81.4  2.1  9.6 11.7  4.2 1.1 1.5 3.1
    ## 19   14.3 54.5  1.5  3.5 42.1  4.2  4.9 85.8  2.9  9.4 12.3  2.4 0.8 1.4 1.9
    ## 266  17.1 51.8  1.8  4.6 40.0  4.9  5.8 83.6  3.4  9.0 12.4  3.4 0.9 1.6 3.1
    ## 1020 16.4 52.9  2.0  4.9 41.0  5.2  6.3 82.2  2.6  7.2  9.8  3.6 1.0 1.1 3.1
    ## 259  18.8 49.6  1.9  5.0 37.1  6.1  7.1 85.4  1.3  6.0  7.3  3.3 1.8 0.4 2.0
    ## 519  19.9 47.0  2.2  5.7 37.8  6.2  7.1 88.6  0.9  6.1  7.1  4.9 1.8 0.6 2.6
    ## 788  17.5 51.2  1.9  4.9 39.8  5.0  5.7 88.5  1.1  5.4  6.5  5.2 1.6 0.4 2.0
    ## 6    18.0 51.6  2.5  6.1 41.9  5.3  5.9 88.9  0.5  6.4  6.8  5.4 0.7 1.8 3.0
    ## 261  17.7 52.1  1.8  5.0 35.3  5.7  6.5 88.5  0.4  5.9  6.4  5.9 0.7 1.1 2.9
    ## 8    18.1 49.1  2.8  6.8 40.8  3.9  4.4 88.9  0.6  3.2  3.8  5.1 1.1 0.3 2.3
    ## 267  18.5 48.7  2.6  6.5 40.1  3.2  3.7 87.3  1.1  3.9  5.0  6.9 1.5 0.5 2.6
    ## 781  20.1 50.6  2.8  7.0 40.2  3.7  4.0 92.2  1.0  3.8  4.8  6.0 1.4 0.7 2.4
    ## 3    19.3 54.2  1.8  5.0 36.7  4.7  6.5 73.1  1.2  7.5  8.6  9.1 1.4 0.9 4.2
    ## 523  19.4 49.3  2.2  6.3 34.8  3.9  5.7 69.3  1.0  6.9  7.8 10.2 1.2 0.5 3.9
    ## 275  16.5 42.7  2.3  7.1 32.7  4.8  6.7 71.3  1.2  6.6  7.8  6.0 1.1 0.3 3.4
    ## 517  20.6 46.3  2.8  8.9 31.6  7.0  9.2 75.8  1.3  8.1  9.4  8.8 1.0 0.2 4.3
    ## 778  20.5 47.9  2.9  8.3 35.0  5.2  7.1 73.0  0.8  7.2  8.0  8.6 1.0 0.5 4.3
    ## 1012 21.6 45.7  3.1  8.8 35.3  5.6  7.5 74.4  0.9  8.3  9.1  8.7 1.2 0.6 4.5
    ## 28   13.5 49.9  1.5  3.7 39.6  3.5  4.2 85.0  2.6  8.1 10.7  6.1 1.2 0.8 2.8
    ## 282  15.1 51.1  1.0  3.4 30.7  3.6  4.4 82.1  2.9  8.0 10.8  7.3 1.4 0.7 3.1
    ## 541  14.7 52.8  1.1  3.5 31.4  3.4  4.1 81.7  2.3  7.5  9.7  7.0 1.2 0.6 3.1
    ## 784  18.0 56.6  1.3  3.3 38.8  4.8  5.5 86.8  2.8  8.0 10.8  8.3 1.3 0.7 3.1
    ## 1015 17.7 58.3  1.3  3.9 33.7  5.1  6.3 81.0  2.8 11.0 13.8  7.9 1.5 0.9 3.8
    ## 280  16.9 51.8  1.1  2.9 36.4  2.2  2.8 78.9  2.8  9.2 12.0  3.8 1.0 1.1 2.0
    ## 544  16.7 47.7  1.6  4.7 33.9  2.1  2.7 78.4  2.3  8.6 10.9  3.6 0.9 0.8 1.4
    ## 793  19.9 47.7  2.5  6.3 40.0  1.9  2.2 84.0  2.1  9.6 11.7  3.8 0.9 0.7 1.8
    ## 1048 15.8 47.3  1.4  4.5 31.4  1.3  1.7 76.0  1.9  9.1 11.0  3.2 1.0 1.0 1.9
    ## 311   8.8 66.9  0.0  0.0  0.0  4.1  6.4 63.6  3.8  9.0 12.9  2.0 0.8 2.3 1.6
    ## 585   8.2 69.3  0.0  0.0  0.0  3.7  5.9 63.0  3.4 10.1 13.5  1.5 0.8 2.0 1.9
    ## 837   8.2 67.5  0.0  0.1  0.0  3.3  5.3 62.3  3.4 10.1 13.5  1.3 0.6 2.7 1.7
    ## 1066  7.7 71.3  0.0  0.1  0.0  4.6  6.7 69.0  3.7 11.0 14.7  1.1 0.7 2.1 1.8
    ## 7    21.1 44.9  1.2  4.1 29.8  5.2  7.1 73.7  1.9  8.2 10.1 10.3 1.8 0.3 4.8
    ## 270  20.2 42.8  1.6  5.6 29.0  4.1  6.2 65.6  1.5  9.6 11.1 10.7 1.9 0.5 4.5
    ## 518  22.5 47.2  1.0  3.7 25.8  5.1  6.7 76.3  1.8  6.2  7.9  7.0 1.6 0.4 4.5
    ## 796  19.0 43.9  1.3  4.2 31.5  4.2  6.4 65.6  1.7  9.9 11.5 11.7 1.4 0.4 4.8
    ## 1040 15.8 44.4  1.0  3.4 29.8  3.4  5.1 66.7  1.4  6.0  7.4  7.1 1.0 0.3 3.8
    ## 258  19.4 47.2  5.1 11.7 43.7  3.8  4.2 91.6  0.7  4.7  5.3  5.2 1.3 0.4 2.8
    ## 773  21.7 48.2  5.3 12.7 42.1  5.7  6.3 91.6  0.5  5.0  5.5  5.8 1.2 0.1 3.4
    ## 1019 19.1 43.7  4.5 11.7 38.0  4.3  4.7 92.3  0.5  4.7  5.2  6.3 1.3 0.4 3.2
    ## 287  15.5 41.8  1.9  6.0 32.4  4.2  5.1 82.9  0.8  2.9  3.7  8.1 0.9 0.2 3.8
    ## 515  20.8 43.7  3.4  9.5 36.1  8.0  9.3 86.0  0.5  3.7  4.3  9.3 1.1 0.1 4.8
    ## 786  17.7 43.8  2.2  6.3 34.3  7.7  8.7 88.6  0.6  3.3  3.9  9.4 0.8 0.2 4.1
    ## 1013 20.3 46.0  3.1  8.0 38.2  6.6  7.3 90.4  0.7  3.1  3.7  9.7 0.9 0.1 4.0
    ## 780  17.0 61.1  0.2  0.6 29.4  6.0  8.7 69.8  2.7  4.5  7.2  3.7 0.9 0.6 2.7
    ##       EFF  EFG   TS  PPM
    ## 49   27.2 53.1 55.4 0.45
    ## 296  27.3 53.8 55.5 0.52
    ## 563  26.9 53.3 55.0 0.54
    ## 1183 15.9 57.6 57.5 0.40
    ## 2    33.0 55.1 61.0 0.77
    ## 521  29.8 53.7 60.9 0.76
    ## 4    25.0 51.8 59.4 0.73
    ## 262  25.0 52.1 58.6 0.73
    ## 514  28.9 56.6 62.9 0.80
    ## 775  27.2 55.5 62.4 0.80
    ## 5    30.7 54.5 59.9 0.73
    ## 256  35.3 59.8 64.5 0.84
    ## 516  34.6 58.9 61.2 0.97
    ## 777  33.2 60.3 63.3 0.85
    ## 1011 35.0 58.3 63.3 0.91
    ## 1    30.1 54.0 61.9 0.86
    ## 254  33.1 53.9 61.5 0.98
    ## 512  32.6 54.3 62.4 0.94
    ## 1026 27.4 48.7 58.2 0.59
    ## 15   23.6 51.3 59.1 0.60
    ## 288  20.7 49.6 57.1 0.56
    ## 540  24.2 46.9 58.2 0.59
    ## 798  27.6 51.1 60.7 0.64
    ## 12   25.3 51.2 57.1 0.76
    ## 257  32.2 51.9 59.4 0.82
    ## 776  31.0 54.3 63.9 0.92
    ## 1010 33.9 53.6 61.7 0.91
    ## 19   29.1 59.8 64.7 0.60
    ## 266  30.4 56.7 62.1 0.74
    ## 1020 28.2 59.1 64.2 0.74
    ## 259  26.9 54.5 60.7 0.78
    ## 519  27.5 52.3 58.9 0.84
    ## 788  27.3 56.3 62.0 0.73
    ## 6    28.6 58.6 64.1 0.77
    ## 261  27.9 57.1 63.2 0.75
    ## 8    22.7 56.9 60.9 0.76
    ## 267  25.3 55.7 59.1 0.72
    ## 781  27.1 57.7 61.5 0.77
    ## 3    32.7 59.1 62.0 0.75
    ## 523  29.6 55.2 57.7 0.73
    ## 275  21.6 49.4 54.5 0.66
    ## 517  30.8 52.9 58.4 0.86
    ## 778  29.0 54.9 58.6 0.81
    ## 1012 29.8 53.0 57.0 0.80
    ## 28   27.1 55.2 60.3 0.57
    ## 282  28.9 54.3 59.0 0.64
    ## 541  27.7 56.1 60.3 0.62
    ## 784  35.9 60.3 64.6 0.76
    ## 1015 38.7 61.9 66.2 0.81
    ## 280  28.0 55.3 57.4 0.66
    ## 544  25.0 52.7 54.8 0.61
    ## 793  28.0 54.0 56.1 0.70
    ## 1048 23.2 51.9 53.2 0.53
    ## 311  27.0 67.0 68.4 0.50
    ## 585  26.2 69.5 69.9 0.44
    ## 837  26.0 67.1 67.9 0.46
    ## 1066 28.0 71.4 73.3 0.49
    ## 7    29.5 47.9 52.4 0.70
    ## 270  29.0 46.5 49.9 0.64
    ## 518  26.2 49.3 53.4 0.76
    ## 796  29.6 47.6 50.9 0.61
    ## 1040 19.9 47.5 51.3 0.54
    ## 258  26.1 60.6 64.2 0.81
    ## 773  29.4 60.1 65.4 0.94
    ## 1019 24.4 55.8 60.2 0.74
    ## 287  18.3 48.1 53.8 0.62
    ## 515  26.6 51.9 59.5 0.84
    ## 786  24.6 49.7 58.8 0.75
    ## 1013 27.2 53.9 60.4 0.81
    ## 780  27.5 61.8 64.8 0.81

``` r
u <- ggplot(data=top_20_players)
u + ggtitle("Top 20 players efficiency over 2017-2022 season") +
  geom_boxplot(aes(x=Player, y =EFF, colour=Player), size=1) +
  geom_jitter(aes(x=Player, y =EFF, colour=Player)) + 
  ylim(18, 40) +
  theme(axis.ticks.x = element_blank(),
        axis.text.x = element_blank(),
        axis.title.x=element_text(size=15),
        axis.title.y=element_text(size=15),
        axis.text.y=element_text(size=15),
        plot.title = element_text(size=30, face="bold"))
```

    ## Warning: Removed 1 rows containing non-finite values (`stat_boxplot()`).

    ## Warning: Removed 1 rows containing missing values (`geom_point()`).

![](nbaAnalysisNotebook_files/figure-gfm/unnamed-chunk-24-1.png)<!-- -->
