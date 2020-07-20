import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import controller
from Views import TableView
from app import app
from Controllers import TableController


layout = TableView.layout


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
    return TableController.update_selects_with_data(selected_brand, selected_model)


@app.callback(
    Output('native-table', 'data'),
    [Input('brand_dropdown', 'value'),
     Input('model_dropdown', 'value'),
     Input('year_dropdown', 'value')])
def update_table(selected_brand, selected_model, selected_year):
    return TableController.update_table(selected_brand, selected_model, selected_year)


if __name__ == "__main__":
    app.run_server(debug=True)