import dash_core_components as dcc
import dash_html_components as html


layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-test'),
    html.Div(id="hidden_div_for_redirect_callback"),
])