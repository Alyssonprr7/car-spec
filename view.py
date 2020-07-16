import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

navbar = dbc.NavbarSimple(
    brand="Teste Car-Spec",
    brand_href="#",
    color="#FF6C2F",
    dark=True,
)


def dropdown(label, dropdown_id, option_object):
    html.Div(children=[
        html.Label(label),
        dcc.Dropdown(
            id=dropdown_id,
            options=option_object,
            value=None
        ),
    ])
