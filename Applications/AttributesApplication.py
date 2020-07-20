import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import controller
import dash_bootstrap_components as dbc

import view
from app import app
from Controllers import IndexController
from Views import AttributesView

layout = AttributesView.layout


def new_layout(data):
    return AttributesView.render_new_layout(data)

