# -*- coding: utf-8 -*-
#import plotly.graph_objects as go
import plotly.graph_objs as go
import cufflinks as cf
import pandas as pd
import os
from plotly.offline import iplot,plot

pd.set_option('display.max_columns', 30)

path  =  os.path.abspath("Data/titanic_train.csv")

data = pd.read_csv(path)

data.columns

data.describe()

data.info()

data.head()

data.Age.dtype

#----------------------------------------------------------
#Pie chart for Survived, pclass and Sex columns

Slabels = data["Survived"].value_counts().keys().tolist()
Svalues = data["Survived"].value_counts().values.tolist()

trace = go.Pie(labels= Slabels,
               values= Svalues,
               marker= dict(colors = ['red']),
               hoverinfo= "value")

data = [trace]
layout = go.Layout(title = "Survived Distribution", legend = {"0":"Surv","1":"notsur"})
fig = go.Figure(data = data, layout= layout)
plot(fig)


#----------------------------------------------------------

sex_label = data['Sex'].value_counts().keys().tolist()

sex_values = data['Sex'].value_counts().values.tolist()

sex_trace = go.Pie(labels = sex_label ,
                   values = sex_values,
                   marker = dict(colors = ['blue']),
                   hoverinfo = "value")

Sdata = [sex_trace]
Slayout = go.Layout(title = "Geneder summary")
sfig = go.Figure(data = Sdata, layout = Slayout) 
plot(sfig)

#----------------------------------------------------------
class_label = data['Pclass'].value_counts().keys().tolist()

class_values = data['Pclass'].value_counts().values.tolist()

class_trace = go.Pie(labels = class_label ,
                   values = class_values,
                   marker = dict(colors = ['green']),
                   hoverinfo = "value")

PCdata = [class_trace]
PClayout = go.Layout(title = "PClass summary")
PCfig = go.Figure(data = PCdata, layout = PClayout) 
plot(PCfig)

#----------------------------------------------------------
#Numerically columns Age and Fare -- Distribution
#defining Data
Atrace = go.Histogram(x = data['Age'], nbinsx = 40, histnorm = 'percent')
AAge = [Atrace]

#Defining layout
Alayout = go.Layout(title = "Age Distribution")

#Define figuring and plotting 
Afig = go.Figure(data = AAge , layout = Alayout)

plot(Afig)

#----------------------------------------------------------

Ftrace = go.Histogram(x = data['Fare'], nbinsx = 40, histnorm = 'percent')
FFare = [Ftrace]

#Defining layout
Flayout = go.Layout(title = "Fare Distribution")

#Define figuring and plotting 
Ffig = go.Figure(data = FFare , layout = Flayout)

plot(Ffig)

#----------------------------------------------------------
#--Scatter plot
#defining data
AFStrace = go.Scatter(x = data['Age'],y=data['Fare'],text = data['Survived'],mode='markers')

ASFdata=[AFStrace]

#defining layout
ASFlayout = go.Layout(title='Fare Vs Age Scatter Plot',xaxis=dict(title='Age'),yaxis=dict(title='Fare'),hovermode='closest')

#defining figure and plotting
ASFfigure = go.Figure(data=ASFdata,layout=ASFlayout)
plot(ASFfigure)

#----------------------------------------------------------
#Bar chart
y=[]
fare = []
for i in list(data['Pclass'].unique()):
    result = data[data['Pclass']==i]['Age'].mean()
    fares = data[data['Pclass']==i]['Fare'].mean()
    y.append(result)
    fare.append(fares)

#defining data
trace = go.Bar(x = list(data['Pclass'].unique()),y=y,marker=dict(color=fare,colorscale='Viridis',showscale=True),text = fare)
bardata=[trace]

#defining layout
barlayout = go.Layout(title='Age/Fare vs Pclass Bar Chart',xaxis=dict(title='Pclass'),yaxis=dict(title='Age'),hovermode='closest')

#defining figure and plotting
bfigure = go.Figure(data=bardata,layout=barlayout)
plot(bfigure)

#----------------------------------------------------------
#Distribution plots

import plotly.figure_factory as ff

#defining data
a = data[data['Pclass']==1]['Fare']
b = data[data['Pclass']==2]['Fare']
c = data[data['Pclass']==3]['Fare']
hist_data=[a,b,c]
group_labels=['1','2','3']

#defining fig and plotting
fig = ff.create_distplot(hist_data,group_labels,bin_size= [1,1,1],show_curve=False)

fig.update_layout(title_text='Distribution for Fares')
plot(fig)


a = data[data['Pclass']==1]['Age']
b = data[data['Pclass']==2]['Age']
c = data[data['Pclass']==3]['Age']

hist_data=[a,b,c]
group_labels=['1','2','3']

fig = ff.create_distplot(hist_data,group_labels,bin_size=[1,1,1],show_curve=False)

fig.update_layout(title_text='Distribution for Age')
plot(fig)

#----------------------------------------------------------
#Bubble chart
#defining data
Bubbledata=[ go.Scatter(x = data['Age'],y=data['Fare'],
               text=data['Pclass'],
                mode='markers',
               marker=dict(size=data['Pclass']*15, color=data['Survived'],showscale=True),
              )]
    
#defining layout
layout = go.Layout(title='Fare vs Age with Survivability and Pclass',xaxis=dict(title='Age'),yaxis=dict(title='Fare'),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=Bubbledata,layout=layout)
plot(figure)

#----------------------------------------------------------





























