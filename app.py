from flask import Flask, render_template, request, url_for, flash, redirect
import graph,back
from bokeh.embed import components

messages = []
app = Flask(__name__)
app.config['SECRET_KEY']='df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

@app.route('/')
def base():
    return render_template('index.html')

#Scout Pre-Page
@app.route('/teamselect/',methods=["POST", "GET"])
def select():
   Red = []
   Blue = []
   RedA = []
   BlueA = []
   if request.method == "POST":
      Red.clear()
      Blue.clear()
      Red.append(request.form["Team1R"])
      Red.append(request.form["Team2R"])
      Red.append(request.form["Team3R"])
      Blue.append(request.form["Team1B"])
      Blue.append(request.form["Team2B"])
      Blue.append(request.form["Team3B"])
      scriptBarR, divBarR = components(graph.BarGraphR(Red))
      scriptPie1R, divPie1R = components(graph.PieGraph1R(Red))
      scriptPie2R, divPie2R = components(graph.PieGraph2R(Red))
      scriptBarB, divBarB = components(graph.BarGraphB(Blue))
      scriptPie1B, divPie1B = components(graph.Pie1GraphB(Blue))
      scriptPie2B, divPie2B = components(graph.Pie2GraphB(Blue))
      infosB, totpB = graph.chargeB(Blue)
      infosR, totpR = graph.chargeR(Red)
      return render_template('scout.html',scriptBarB = scriptBarB, divBarB=divBarB,
                              scriptBarR = scriptBarR, divBarR=divBarR,
                              scriptPie1B=scriptPie1B, divPie1B=divPie1B,
                              scriptPie1R = scriptPie1R, divPie1R =divPie1R,
                              scriptPie2R=scriptPie2R,divPie2R=divPie2R,
                              scriptPie2B=scriptPie2B,divPie2B=divPie2B,
                              infosB = infosB, infosR = infosR,
                              Red = Red, Blue=Blue,
                              totpB = totpB, totpR=totpR
                             )
   return render_template('TeamSelect.html')

#Scout
@app.route('/scout/',methods=["POST", "GET"])
def scout():
   return render_template('scout.html')


#Informações das equipes
@app.route('/equipes/',methods=["POST", "GET"])
def equipes():
   if request.method == "POST":
      TeamNumer = request.form["TN"]
      data= back.getTeamInfo(TeamNumer)
      if data == None:
         flash("Número de equipe inválido ou inexistente","warning")
         return render_template('equipes.html')
      else:

         return render_template('equipes.html',Local=data[0],Pais=data[2],Escola=data[4],Nome=data[5],Estado=data[1],Num=data[3])
   else: 
      return render_template('equipes.html')
   

#Check List Pré Partida
@app.route('/checklist/',methods=["POST", "GET"]) 
def checklist():
   return render_template('checklist.html')

#Sobre a 9218
@app.route('/about/')
def about():
   return render_template('about.html')


if (__name__) == "__main__":
   app.run(port="5100", debug="True") 

