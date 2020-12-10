from typing import Text
import nbconvert
"""jupyter nbconvert --to html IG.ipynb"""

'''
import plotly.graph_objects as go

fig = go.Figure(data=[go.Pie(
    labels=['ТехСтанкоМаш', 'Компания А', 'Компания Б', 'Компания B', 'Компания Г', 'Компания Д', 'РусСтанкоСтрой',
            'Компания E', 'Компания Ж'],
    values=[23, 9, 8, 10, 11, 7, 25, 10, 6])])

fig.update_traces(hoverinfo='label+value', textinfo='value', textfont_size=20, textfont_color='#000000',
                  marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(template="plotly_dark", title="№1 Задание лабораторной работы")

fig.show()
fig.write_html("./1Zadanie.html")
'''

'''
import plotly.graph_objects as go

name = ['Центральный регион', 'Северо-запад', 'Поволжье', 'Урал', 'Сибирь', 'Дальний восток']
date = [4.1, 2.5, 1.5, 1.7, 2.5, 0.9]

colors = []
color_marcer = lambda date: 'blue' if float(date) > 2.0 else 'red'
for i in range(len(date)):
    colors.append(color_marcer(date[i]))

fig = go.Figure()
fig.add_trace(go.Bar(
    x=name,
    y=date,
    marker_color=colors))

fig.update_layout(template="plotly_dark",
                  title="№2 Объем продаж по регионам", shapes=[
        {'type': 'line', 'y0': 2, 'y1': 2, 'x0': -1, 'x1': 6, 'xref': 'x1', 'yref': 'y1',
         'line': {'color': 'grey', 'width': 3, }}])
# fig.show()
fig.write_html("./2Zadanie.html")
'''

'''
import plotly.graph_objects as go

year = [2012, 2013, 2014, 2015, 2016]
opr = [387, 420, 477, 513, 530]
opr_p = [100, 109, 123, 133, 137]
opb = [24, 39, 35, 45, 29]
opb_p = [100, 162, 146, 188, 121]


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=year,
    y=opr_p,
    # mode = 'year+opr_p',
    name='Обьем продаж',
    marker_color='red'))

fig.add_trace(go.Scatter(
    x=year,
    y=opb_p,
    # mode = 'year+opb_p',
    name ='Приыбль',
    marker_color='blue'))

fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        dtick = 1
    ),
    title="№3 Изменения Обьема продаж и прибали компании «ТехСтанкоМаш» и 2012-2016 г.",
    template="plotly_dark"
)
fig.show()
# fig.write_html("./3Zadanie.html")
'''

'''
import plotly.graph_objects as go

name = ['Менее 500', '500-999', '1000-1999', '2000-2999', '3000 и более']
date_1 = [320, 770, 410, 260, 105]
date_2 = [280, 340, 615, 890, 550]


fig = go.Figure()
fig.add_trace(go.Bar(x = name, y = date_1, name='Компания Г'))
fig.add_trace(go.Bar(x = name, y = date_2, name='«ТехСтанкоМаш»'))
fig.update_layout(barmode='stack', template="plotly_dark",
                  title="№4 Доли продаж")
fig.show()
# fig.write_html("./4Zadanie.html")
'''

'''
import plotly.graph_objects as go
fig = go.Figure()
# text = [15, 30, 10, 5, '19.3%', '10.1%', '16.6%', '12.4%', '31.8%', '9.8%']
fig = fig.add_trace(go.Sunburst(
    labels = ['Токарные станки', 'Фрезерные станки', 'Промышленные станки', 'Сверлильные станки', '«ТехСтанкоМаш»', 'Компания А', 'Компания Б', 'Компания В', 'Компания Г', 'Компания Д'],
    values= [15, 30, 10, 5, 60, 311*10.1/100, 311*16.6/100, 311*12.4/100, 311*31.8/100, 311*9.8/100],
    branchvalues='total',
    parents=['«ТехСтанкоМаш»', '«ТехСтанкоМаш»', '«ТехСтанкоМаш»', '«ТехСтанкоМаш»', '', '', '', '', '', ''],
    hoverinfo = 'text',
    hovertext = ['15 млн', '30 млн', '10 млн', '5 млн', '19.3%', '10.1%', '16.6%', '12.4%', '31.8%', '9.8%'],
    textfont_color = '#000000'
    ))
fig.update_layout(margin = dict(t=50, l=0, r=0, b=0), title="№5 Продажи")
# fig.show()
fig.write_html("./5Zadanie.html")
'''
