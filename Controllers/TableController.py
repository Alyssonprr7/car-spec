import pandas as pd
from Service import Service
from Views import TableView
import dash_core_components as dcc
from dash import no_update

df = pd.DataFrame.from_dict(Service.get_all_cars(5), orient='columns')


def update_selects_with_data(selected_brand, selected_model):
    models_options_object = []
    year_options_object = []

    unique_models_from_brand = list(set(df.loc[df["brand"] == selected_brand]["model"]))
    unique_years_from_model = list(set(df.loc[df["model"] == selected_model]["year"]))

    for model in unique_models_from_brand:
        models_options_object += [{'label': model, 'value': model}]

    for year in unique_years_from_model:
        if not selected_brand:
            year_options_object = []
        else:
            year_options_object += [{'label': year, 'value': year}]

    return models_options_object, year_options_object


def update_table(selected_brand, selected_model, selected_year):
    if selected_brand is None:
        return df.to_dict('records')

    elif selected_model is None:
        return df.loc[df["brand"] == selected_brand].to_dict('records')

    elif selected_year is None:
        return df.loc[df["model"] == selected_model].to_dict('records')

    else:
        return df.loc[df["year"] == selected_year].to_dict('records')


def generate_single_select(label, option_array, dropdown_id):
    option_object = []
    for field in option_array:
        option_object += [{'label': field, 'value': field}]
    return TableView.dropdown(label, dropdown_id, option_object)
