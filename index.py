from dash.dependencies import Input, Output

from app import app
from Applications import TableApplication, AttributesApplication

from Controllers import IndexController

from Views import IndexView

app.layout = IndexView.layout


@app.callback(Output("hidden_div_for_redirect_callback", "children"),
              [Input('native-table', 'active_cell')])
def get_active_letter(active_cell):
    return IndexController.render_new_layout(active_cell, AttributesApplication)


@app.callback(Output('page-test', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return IndexController.display_page(pathname, TableApplication, AttributesApplication)


if __name__ == '__main__':
    app.run_server(debug=True)
