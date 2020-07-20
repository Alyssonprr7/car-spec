from dash.dependencies import Input, Output

from app import app
from Applications import TableApplication, AttributesApplication

import controller
from Controllers import IndexController

import view
from Views import IndexView

app.layout = IndexView.layout


@app.callback(Output("hidden_div_for_redirect_callback", "children"),
              [Input('native-table', 'active_cell')])
def get_active_letter(active_cell):
    return IndexController.render_new_layout(active_cell, AttributesApplication)
    #if active_cell is not None:
    #    car_data = [service.get_unique_car(active_cell["row_id"])]
    #    redirect = dcc.Location(pathname="/apps/app2", id="new-layout-page")
    #    df = pd.DataFrame.from_dict(car_data, orient="columns")
    #    app2.layout = app2.new_layout(df.to_dict('records'))
    #    return redirect

    #else:
    #    return no_update


@app.callback(Output('page-test', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return IndexController.display_page(pathname, TableApplication, AttributesApplication)


if __name__ == '__main__':
    app.run_server(debug=True)
