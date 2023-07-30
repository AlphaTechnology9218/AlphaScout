import requests, json
import re
EC = open('EC.txt', 'r')
ev_cd = EC.read()


def getApi(URL_Parameter):
  url = "https://www.thebluealliance.com/api/v3/"+URL_Parameter
  headers = {
      "X-TBA-Auth-Key":"uhCYxoLaCGGEVbdBhaoqCDfy4mTWqj2trE3WZ3bdqd7D6ED0jZeTHGm5c4y05llV"
  }
  
  response = requests.get(url, headers=headers)
  
  if response.status_code == 200:
      data = response.json()
      # Faça algo com os dados recebidos
  else:
      # Trate erros da requisição
      print("Ocorreu um erro:", response.status_code)
  return(data)
def allianceInfo(team_num,data):
  alliance_color = []
  robot_number = []
  for i in range (len(data)):
    al_bl_round = data[i]["alliances"]["blue"]["team_keys"]
    for j in range(3):
      if al_bl_round[j]=="frc"+str(team_num):
        robot_number.append(j)
        alliance_color.append('b')
    al_rd_round = data[i]["alliances"]["red"]["team_keys"]
    for j in range(3):
      if al_rd_round[j]=="frc"+str(team_num):
        robot_number.append(j)
        alliance_color.append('r')
        
  return alliance_color,robot_number
def getCommunityInfo(infoBR,nodeLevel):
  node_occupation=0
  for i in range(8):
    if((infoBR["autoCommunity"][nodeLevel][i+1]) != "None"):
      node_occupation+=1
    if ((infoBR["teleopCommunity"][nodeLevel][i+1] != "None")):
      node_occupation+=1
  return(node_occupation)
def AllianceMedia(value):
  return(value/3)

def eventTeams():
  team_list = []
  teams = getApi("event/"+ev_cd+"/teams/simple")
  for i in range (len(teams)):
    team_list.append(teams[i]["nickname"])
  return(team_list)
def getMatchesTeamInfo(team_num):
  data = getApi("team/frc"+str(team_num)+"/event/"+ev_cd+"/matches")
  al_info = allianceInfo(team_num,data)
  charge_auto = []
  charge_teleop = []
  high_T_pontuation = 0 #check
  mid_T_pontuation = 0 #check
  low_T_pontuation = 0 #check
  auto_T_point = 0 #check
  teleop_T_point = 0 #check
  total_pts = 0 #check
  charge_auto_docked = 0 #check
  charge_teleop_park = 0 #check
  charge_teleop_docked = 0 #check
  # print(data[0]["score_breakdown"]["red"])
  
  for i in range(len(data)):
    infoB = data[i]["score_breakdown"]["blue"]
    infoR = data[i]["score_breakdown"]["red"]
    if (al_info[0][i]=='b'):
      teleop_T_point += AllianceMedia(infoB["teleopPoints"])
      auto_T_point += AllianceMedia(infoB["autoPoints"])
      total_pts += AllianceMedia(data[i]["alliances"]["blue"]["score"])
      low_T_pontuation+= AllianceMedia(getCommunityInfo(infoB,'B'))
      mid_T_pontuation+= AllianceMedia(getCommunityInfo(infoB,'M'))
      high_T_pontuation+=AllianceMedia(getCommunityInfo(infoB,'T'))
      charge_auto.append(infoB["autoChargeStationRobot"+str(al_info[1][i]+1)])
      charge_teleop.append(infoB["endGameChargeStationRobot"+str(al_info[1][i]+1)])
  
    if (al_info[0][i]=='r'):
      teleop_T_point += AllianceMedia(infoR["teleopPoints"])
      auto_T_point += AllianceMedia(infoR["autoPoints"])
      total_pts += AllianceMedia(data[i]["alliances"]["red"]["score"])
      low_T_pontuation+=AllianceMedia(getCommunityInfo(infoR,'B'))
      mid_T_pontuation+=AllianceMedia(getCommunityInfo(infoR,'M'))
      high_T_pontuation+=AllianceMedia(getCommunityInfo(infoR,'T'))
      charge_auto.append(infoR["autoChargeStationRobot"+str(al_info[1][i]+1)])
      charge_teleop.append(infoR["endGameChargeStationRobot"+str(al_info[1][i]+1)])
  
  charge_auto_docked = charge_auto.count("Docked")
  charge_teleop_docked = charge_teleop.count("Docked")
  charge_teleop_park = charge_teleop.count("Park")
  
  try:
    teleop_T_point = (teleop_T_point/(len(data)))
    auto_T_point =(auto_T_point/(len(data)))
    total_pts= (total_pts/len(data))
    total_pts = round(total_pts)
    low_T_pontuation = (low_T_pontuation/len(data))*10
    mid_T_pontuation = (mid_T_pontuation/len(data))*10
    high_T_pontuation = (high_T_pontuation/len(data))*10
  except ZeroDivisionError:
    x=0
  return(charge_auto , charge_teleop , high_T_pontuation , mid_T_pontuation , low_T_pontuation , auto_T_point , teleop_T_point , total_pts, charge_auto_docked, charge_teleop_docked, charge_teleop_park)
def getTeamInfo(team_number):
  try:
    plusData = getApi("team/frc" + str(team_number))
    city = plusData["city"]
    state = plusData["state_prov"]
    country = plusData["country"]
    number = plusData["team_number"]
    school = plusData["school_name"]
    nickname = plusData["nickname"]
    return city,state,country,number,school,nickname
  except UnboundLocalError:
    plusData = None

'''
getMatchesTeamInfo(team_num)#informações de partida de um time
getTeamInfo(team_num) #informações gerais de um time
eventTeams() #Todos os times que participaram do evento
'''

# https://www.thebluealliance.com/api/v3/team/frc1156/event/2023brbr/matches
#   X-TBA-Auth-Key
#  uhCYxoLaCGGEVbdBhaoqCDfy4mTWqj2trE3WZ3bdqd7D6ED0jZeTHGm5c4y05llV
# 2023xxrio