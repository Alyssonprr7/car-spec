from Service import Service
import dash_core_components as dcc
from dash import no_update
import pandas as pd


df = pd.DataFrame.from_dict(Service.get_all_cars(5), orient='columns')


def render_new_layout(active_cell, application):
    if active_cell is not None:
        car_data = [Service.get_unique_car(active_cell["row_id"])]
        redirect = dcc.Location(pathname="/apps/app2", id="new-layout-page")
        df = pd.DataFrame.from_dict(car_data, orient="columns")
        application.layout = application.new_layout(df.to_dict('records'))
        return redirect

    else:
        return no_update

def display_page(pathname, table_application, attributes_application):
    if pathname == '/apps/app1':
        return table_application.layout
    elif pathname == '/apps/app2':
        return attributes_application.layout
    else:
        return '404'