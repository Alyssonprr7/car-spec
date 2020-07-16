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

print(service.get_all_cars(10))

fetch_data = requests.get('https://5f0785109c5c2500163070bb.mockapi.io/cars')
cars_json = fetch_data.json()



df = pd.DataFrame.from_dict(cars_json, orient='columns')


ROWS_PER_PAGE = 15

navbar = dbc.NavbarSimple(
    brand="Teste Car-Spec",
    brand_href="#",
    color="#FF6C2F",
    dark=True,
)


def generate_single_select(label, option_array, dropdown_id):
    option_object = []
    for field in option_array:
        option_object += [{'label': field, 'value': field}]
    return html.Div(children=[
        html.Label(label),
        dcc.Dropdown(
            id=dropdown_id,
            options=option_object,
            value=None
        ),
    ])


all_selects = html.Div(
    className="mt-4",
    children=[
        dbc.Row(
            [
                dbc.Col(generate_single_select("Fabricante", list(set(df["brand"])), "brand_dropdown"), md=2),
                dbc.Col(generate_single_select("Modelo", [], "model_dropdown"), md=2),
                dbc.Col(generate_single_select("Ano", [], "year_dropdown"), md=2),

            ],
            justify="center"
        )
    ]
)
table = html.Div(
    children=[
      dash_table.DataTable(
          id='native-table',
          columns=[{"name": "Marca", "id": "brand"},
                   {"name": "Modelo", "id": "model"},
                   {"name": "Ano", "id": "year"}],
          data=df.to_dict('records'),
          page_size=ROWS_PER_PAGE,
          style_cell={'textAlign': 'center'},
          style_header={
              'backgroundColor': '#DADADA',
              'fontWeight': 'bold'
          },
          style_cell_conditional=[
              {
                  "if": {"column_id": "info"},
                  "backgroundColor":"#3CB371"
              }
          ],
#          style_data_conditional=[
#             {
#                  'if': {'row_index': 'odd'},
#                  'backgroundColor': 'rgb(248, 248, 248)'
#              }
#         ],
      )
    ],
    className="mt-4"


)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    view.navbar,
    dbc.Container(children=[
        all_selects,
        html.Div(id="table"),
        table,
        html.Div(id="teste"),

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
    return controller.update_table(selected_brand,selected_model, selected_year)


@app.callback(Output('teste', 'children'),
              [Input('native-table', 'active_cell'),
               Input('native-table', 'data')])
def get_active_letter(active_cell, data):
    if active_cell is not None:
        print (active_cell["row_id"])
        new_data = requests.get('https://5f0785109c5c2500163070bb.mockapi.io/cars/{}'.format(active_cell["row_id"]))
        print(new_data.json())
#Preciso pegar o row_id e puxar o valor na coluna id do df naquela row_id

    return no_update





if __name__ == "__main__":
    app.run_server(debug=True)
