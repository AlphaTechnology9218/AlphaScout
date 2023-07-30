from bokeh.embed import components
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange,  Label, LabelSet
from math import pi
from bokeh.palettes import PuBu3, Reds3
from bokeh.transform import cumsum
import back
from bokeh.models.tools import HoverTool 
import pandas as pd

nodes = []

# Gráficos Vermelho

def BarGraphR(teamsR):
    team1R = back.getMatchesTeamInfo(teamsR[0])
    team2R = back.getMatchesTeamInfo(teamsR[1])
    team3R = back.getMatchesTeamInfo(teamsR[2])
    teams = [teamsR[0],teamsR[1],teamsR[2]]
    node = ["High","Mid","Low"]
    DataR = {
        'equipes': teams,
        'HN':[int(team1R[2]),int(team2R[2]),int(team3R[2])],
        'MN': [int(team1R[3]),int(team2R[3]),int(team3R[3])],
        'LN': [int(team1R[4]),int(team2R[4]),int(team3R[4])],
    }
    x = [(teams, nodes) for teams in teams for nodes in node]
    counts = sum(zip(DataR['HN'], DataR['MN'], DataR['LN']),())
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    NodesGradpR = figure(x_range=FactorRange(*x), sizing_mode= "scale_width", height=320, title="Altura de nodes por equipe",
           toolbar_location=None, tools="hover")
    NodesGradpR.vbar(x='x', top='counts', width=0.8, source=source, color ='Red')
    NodesGradpR.y_range.start = 0
    NodesGradpR.x_range.range_padding = 0.05
    NodesGradpR.xaxis.major_label_orientation = 1
    NodesGradpR.xgrid.grid_line_color = None
    return NodesGradpR
def PieGraph1R(teamsR):
    team1R = back.getMatchesTeamInfo(teamsR[0])
    team2R = back.getMatchesTeamInfo(teamsR[1])
    team3R = back.getMatchesTeamInfo(teamsR[2])
    x = {
        teamsR[0]: int(team1R[5]),
        teamsR[1]: int(team2R[5]),
        teamsR[2]: int(team3R[5])
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'equipes'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Reds3

    AutoGradpR = figure(height=400,sizing_mode= "scale_width", title="Pontos autônomos", toolbar_location=None,
           tools="hover", tooltips="@equipes: @value", x_range=(-0.5, 1.0))
    AutoGradpR.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', source=data)
    AutoGradpR.axis.axis_label = None
    AutoGradpR.axis.visible = False
    AutoGradpR.grid.grid_line_color = None
    AutoGradpR.title.align = "center"
    AutoGradpR.title_location = "left"
    return AutoGradpR
def PieGraph2R(teamsR):
    team1R = back.getMatchesTeamInfo(teamsR[0])
    team2R = back.getMatchesTeamInfo(teamsR[1])
    team3R = back.getMatchesTeamInfo(teamsR[2])
    x = {
        teamsR[0]: int(team1R[6]),
        teamsR[1]: int(team2R[6]),
        teamsR[2]: int(team3R[6])
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'equipes'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Reds3

    TeleopGradpR = figure(height=400,sizing_mode= "scale_width", title="Pontos teleoperados", toolbar_location=None,
           tools="hover", tooltips="@equipes: @value", x_range=(-0.5, 1.0))
    TeleopGradpR.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', source=data)
    TeleopGradpR.axis.axis_label = None
    TeleopGradpR.axis.visible = False
    TeleopGradpR.grid.grid_line_color = None
    TeleopGradpR.title_location = "left"
    TeleopGradpR.title.align = "center"
    return TeleopGradpR

def chargeR(teamsR):
    team1R = back.getMatchesTeamInfo(teamsR[0])
    team2R = back.getMatchesTeamInfo(teamsR[1])
    team3R = back.getMatchesTeamInfo(teamsR[2])
    totPR = [team1R[7],team2R[7],team3R[7]]
    charge_infoR = [[team1R[8],team1R[9],team1R[10]],[team2R[8],team2R[9],team2R[10]],[team3R[8],team3R[9],team3R[10]]]
    return charge_infoR, totPR
# Gráficos Azul

def BarGraphB(teamsB):
    team1B = back.getMatchesTeamInfo(teamsB[0])
    team2B = back.getMatchesTeamInfo(teamsB[1])
    team3B = back.getMatchesTeamInfo(teamsB[2])
    
    teams = [teamsB[0],teamsB[1],teamsB[2]]
    node = ["High","Mid","Low"]
    DataB = {
        'equipes': teams,
        'HN':[int(team1B[2]),int(team2B[2]),int(team3B[2])],
        'MN': [int(team1B[3]),int(team2B[3]),int(team3B[3])],
        'LN': [int(team1B[4]),int(team2B[4]),int(team3B[4])],
    }
    x = [(teams, nodes) for teams in teams for nodes in node]
    counts = sum(zip(DataB['HN'], DataB['MN'], DataB['LN']),())
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    NodesGradpB = figure(x_range=FactorRange(*x), sizing_mode= "scale_width", height =320 , title="Altura de nodes por equipe",
           toolbar_location=None, tools="hover")
    NodesGradpB.vbar(x='x', top='counts', width=0.8, source=source, color ='darkblue')
    NodesGradpB.y_range.start = 0
    NodesGradpB.x_range.range_padding = 0.1
    NodesGradpB.xaxis.major_label_orientation = 1
    NodesGradpB.xgrid.grid_line_color = None
    return NodesGradpB
def Pie1GraphB(teamsB):
    team1B = back.getMatchesTeamInfo(teamsB[0])
    team2B = back.getMatchesTeamInfo(teamsB[1])
    team3B = back.getMatchesTeamInfo(teamsB[2])
    x = {
        teamsB[0]: int(team1B[5]),
        teamsB[1]: int(team2B[5]),
        teamsB[2]: int(team3B[5])
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'equipes'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = PuBu3

    AutoGradpB = figure(height=400,sizing_mode= "scale_width", title="Pontos autônomos", toolbar_location=None,
           tools="hover", tooltips="@equipes: @value", x_range=(-0.5, 1.0))
    AutoGradpB.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', source=data)
    AutoGradpB.axis.axis_label = None
    AutoGradpB.axis.visible = False
    AutoGradpB.grid.grid_line_color = None
    AutoGradpB.title_location = "left"
    AutoGradpB.title.align = "center"
    return AutoGradpB
def Pie2GraphB(teamsB):
    team1B = back.getMatchesTeamInfo(teamsB[0])
    team2B = back.getMatchesTeamInfo(teamsB[1])
    team3B = back.getMatchesTeamInfo(teamsB[2])
    x = {
        teamsB[0]: int(team1B[6]),
        teamsB[1]: int(team2B[6]),
        teamsB[2]: int(team3B[6])
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'equipes'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = PuBu3

    TeleopGradpB = figure(height=400,sizing_mode= "scale_width", title="Pontos teleoperados", toolbar_location=None,
           tools="hover", tooltips="@equipes: @value", x_range=(-0.5, 1.0))
    TeleopGradpB.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', source=data)
    TeleopGradpB.axis.axis_label = None
    TeleopGradpB.axis.visible = False
    TeleopGradpB.grid.grid_line_color = None
    TeleopGradpB.title_location = "left"
    TeleopGradpB.title.align = "center"
    return TeleopGradpB

def chargeB(teamsB):
    team1B = back.getMatchesTeamInfo(teamsB[0])
    team2B = back.getMatchesTeamInfo(teamsB[1])
    team3B = back.getMatchesTeamInfo(teamsB[2])
    totPB = [team1B[7],team2B[7],team3B[7]]
    charge_infoB = [[team1B[8],team1B[9],team1B[10]],[team2B[8],team2B[9],team2B[10]],[team3B[8],team3B[9],team3B[10]]]
    return charge_infoB, totPB


"""
Ordem:
charge_auto - 0
charge_teleop - 1
HighN - 2 - foi
MidN - 3 - foi
LowN - 4 - foi
AutoT - 5 - foi
TeleT - 6 - foi
Total - 7 - foi 
charge_auto_docked - 8 - foi
charge_teleop_docked - 9 - foi
charge_teleop_park - 10 - foi
"""