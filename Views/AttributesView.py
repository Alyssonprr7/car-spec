import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from Controllers import IndexController
import dash_table
from Components import Navbar

import view


def render_new_layout(data):
    return html.Div([
        Navbar.navbar,
        dbc.Container(
            className="mt-4",
            children=[
                html.H3('Attributes'),
                dash_table.DataTable(
                    data=data,
                    columns=[{'id': c, 'name': c} for c in IndexController.df.columns],
                    page_size=10,
                )
            ]),
        dbc.Container(children=[
            dcc.Link('Voltar para Tabela', href='/apps/app1'),
        ], className="mt-4"),
    ])

layout = html.Div(children=[
    Navbar.navbar,
    dbc.Container(children=[
        dcc.Link('Ir para Tabela', href='/apps/app1'),
    ], className="mt-4"),
])
