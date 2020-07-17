import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import requests
from dash.dependencies import Input, Output
from dash import no_update
import dash_table
import controller
import service
import view


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    view.navbar,
    dbc.Container(children=[
        view.all_selects(list(set(controller.df["brand"]))),
        #html.Div(id="table"),
        view.render_table(controller.df.to_dict('records')),
        html.Div(id="teste"),
        html.Div([
            # represents the URL bar, doesn't render anything
            dcc.Location(id='url', refresh=False),

            dcc.Link('Navigate to "/"', href='/'),
            html.Br(),
            dcc.Link('Navigate to "/page-2"', href='/page-2'),

            # content will be rendered in this element
            html.Div(id='page-content')
        ])

    ])
])


@app.callback(
    Output('model_dropdown', 'value'),
    [Input('brand_dropdown', 'value')])
def update_selected_model_to_none(selected_brand):
    return None


@app.callback(
    Output('year_dropdown', 'value'),
    [Input('model_dropdown', 'value')])
def update_selected_year_to_none(selected_model):
    return None


@app.callback(
    [Output('model_dropdown', 'options'),
     Output('year_dropdown', 'options')],
    [Input('brand_dropdown', 'value'),
     Input('model_dropdown', 'value')])
def update_selects_with_data(selected_brand, selected_model):
    return controller.update_selects_with_data(selected_brand, selected_model)


@app.callback(
    Output('native-table', 'data'),
    [Input('brand_dropdown', 'value'),
     Input('model_dropdown', 'value'),
     Input('year_dropdown', 'value')])
def update_table(selected_brand, selected_model, selected_year):
    return controller.update_table(selected_brand, selected_model, selected_year)


@app.callback(Output('teste', 'children'),
              [Input('native-table', 'active_cell'),
               Input('native-table', 'data')])
def get_active_letter(active_cell, data):
    if active_cell is not None:
        new_data = requests.get('https://5f0785109c5c2500163070bb.mockapi.io/cars/{}'.format(active_cell["row_id"]))
        page_car = dcc.Link('Navigate to "/page-2"', href='/{}'.format(active_cell["row_id"]))
        print(new_data.json())
#Preciso pegar o row_id e puxar o valor na coluna id do df naquela row_id

    return no_update


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
