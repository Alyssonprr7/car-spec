import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import controller
import dash_table


navbar = dbc.NavbarSimple(
    brand="Teste Car-Spec",
    brand_href="#",
    color="#FF6C2F",
    dark=True,
)


def all_selects(brands_series):
    return html.Div(
        className="mt-4",
        children=[
            dbc.Row(
                [
                    dbc.Col(controller.generate_single_select("Fabricante", brands_series, "brand_dropdown"), md=2),
                    dbc.Col(controller.generate_single_select("Modelo", [], "model_dropdown"), md=2),
                    dbc.Col(controller.generate_single_select("Ano", [], "year_dropdown"), md=2),

                ],
                justify="center"
            )
        ]
    )


def dropdown(label, dropdown_id, option_object):
    return html.Div(children=[
        html.Label(label),
        dcc.Dropdown(
            id=dropdown_id,
            options=option_object,
            value=None
        ),
    ])


def render_table(data):
    return html.Div(
        children=[
            dash_table.DataTable(
                id='native-table',
                columns=[{"name": "Marca", "id": "brand"},
                         {"name": "Modelo", "id": "model"},
                         {"name": "Ano", "id": "year"}],
                data=data,
                page_size=15,
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
