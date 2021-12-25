import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
#import dash_core_components as dcc
#import dash_html_components as html

# Added
import flask
import os
from flask import Flask

# Added
server = Flask(__name__)
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.A('Navigate to google.com', href='http://google.com', target='_blank'),
    html.B(html.Label("Comptrain")),
    html.Br(),
    html.B(html.Embed(src='/static/wod1.html', height='400', width='300', title="Comptrain")),
    html.Br(),
    html.Br(),
    html.B(html.Label("Invictus")),
    html.B(html.Embed(src='/static/wod2.html', height='400', width='300', title="Invictus")),
])

# Added
@app.server.route('/static/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)

if __name__ == '__main__':
    app.run_server(debug=True)
