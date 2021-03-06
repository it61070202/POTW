import pandas as pd
import pygal as pg
def main():
    """ Team Chart 
    make data with pandas library
    make chart with pygal
    """
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    seasons = [dt[i]["Season short"] for i in dt]
    seasons = sorted(list(set(seasons)))
    team = [dt[i]["Team"] for i in dt]
    team_list = sorted(list(set(team)))
    team_count = {}
    for i in team_list:
        team_count[i] = team.count(i)
    chartmaker(team_count, "every season")

    team_line_count = [[] for _ in team_list]

    for season in seasons:
        team2 = [dt[i]["Team"] for i in dt if dt[i]["Season short"] == season]
        team_list2 = sorted(list(set(team2)))
        for i in range(len(team_list)):
            team_line_count[i].append(team2.count(team_list[i]))
        team_count2 = {}
        for i in team_list2:
            team_count2[i] = team2.count(i)
        chartmaker(team_count2, season)
  
def chartmaker(team_count, season):
    """chartmaker function"""
    line_chart = pg.HorizontalBar(legend_at_bottom=True, legend_at_bottom_columns=4)
    line_chart.title = "POTW teams count in %s" %season
    for key, value in team_count.items():
        line_chart.add(str(key), value)
    line_chart.render_to_file('pic/team/POTW teams count in %s.svg' %season)
main()
    