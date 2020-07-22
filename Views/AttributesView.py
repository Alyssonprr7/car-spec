import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from Controllers import AttributesController
import dash_table
from Components import Navbar


def render_new_layout(data):
    keys = AttributesController.translate_to_portuguese(data[0])
    values = AttributesController.get_values(data[0])
    return html.Div([
        Navbar.navbar,
        dbc.Container(
            className="mt-4",
            children=[
                html.H3('Attributes'),
                dbc.Row([
                    dbc.ListGroup(
                        [
                            dbc.ListGroupItem(key, style={"fontWeight": "bold"}) for key in keys
                        ]
                    ),
                    dbc.ListGroup(
                        [
                            dbc.ListGroupItem(value, style={"fontWeight": "thin"}) for value in values

                        ]
                    ),
                ], justify="center"),

            ]),
        dbc.Container(children=[
            dcc.Link('Voltar para Tabela', href='/table'),
        ], className="mt-4"),

    ]),


layout = html.Div(children=[
    Navbar.navbar,
    dbc.Container(children=[
        dcc.Link('Ir para Tabela', href='/table'),
    ], className="mt-4"),
])
