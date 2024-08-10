from dash import Dash, dcc, ctx, html, Input, Output, State
import dash_bootstrap_components as bootstrap
from dash.long_callback import DiskcacheLongCallbackManager
import diskcache
from src.retrieve_file import retrieve_options


cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)
external_stylesheet = [bootstrap.themes.BOOTSTRAP, bootstrap.icons.BOOTSTRAP]
app = Dash(__name__, long_callback_manager=long_callback_manager, external_stylesheets=external_stylesheet)


list_path = "Database/list_options.csv"


def get_list_subject_and_school(list_path):

    subjects = retrieve_options(list_path)[0]
    schools = retrieve_options(list_path)[1]

    children_subject = []
    children_school = []

    for subject in subjects:
        children_subject.append(bootstrap.DropdownMenuItem(subject))

    for school in schools:
        children_school.append(bootstrap.DropdownMenuItem(school))

    return children_subject, children_school


children_subject, children_school = get_list_subject_and_school(list_path)


#Structure of the page

header = bootstrap.Navbar(bootstrap.Container(html.H3("Jessica's School Library", style={'color': 'white'}, className="text-center"), fluid=True), dark=True, color='#c71585', sticky='top')

table_header = [
    html.Thead(html.Tr([html.Th("File Name"), html.Th("Path File"), html.Th("Subject"), html.Th("School"), html.Th("Year")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

content = bootstrap.Container([
    bootstrap.Row(bootstrap.Col(html.Div("Look for a file here"),  style={"padding-top": "4%", "font-size": "24px"})),
    bootstrap.Row([

        bootstrap.Col([
            bootstrap.DropdownMenu(label="Subject", children=children_subject, color='danger', className='mb-3', style={"padding-top": "4%"})
        ]),

        bootstrap.Col([
            bootstrap.DropdownMenu(label="School", children=children_school, className='mb-3', style={"padding-top": "4%"})
        ])
    ]),

    bootstrap.Row([

        bootstrap.Col([
            bootstrap.Table(table_header + table_body, bordered=True, style={"padding-top": "4%"})

        ])

    ]),

    bootstrap.Row(bootstrap.Col(html.Div("Save a new file here"),  style={"padding-top": "4%", "font-size": "24px"})),
    bootstrap.Row([
        bootstrap.Col([
            bootstrap.InputGroup(
                [bootstrap.InputGroupText("File Name"), bootstrap.Input(placeholder="Write the name of the file"), ],
                className="mb-3", size="lg", style={"padding-top": "2%"}
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("File path"), bootstrap.Input(placeholder="Write the path of the file")],
                className="mb-3", size="lg",
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("Subject"), bootstrap.Input(placeholder="Write the subject name")],
                className="mb-3", size="lg",
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("School"), bootstrap.Input(placeholder="Write the school name")],
                className="mb-3", size="lg",
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("Year"), bootstrap.Input(placeholder="Write the year")],
                className="mb-3", size="lg",
            ),
        ]),

        bootstrap.Col(
            bootstrap.Card(
                [
                    bootstrap.CardImg(src= "https://varthana.com/school/wp-content/uploads/2023/04/B296.jpg", top=True),
                    bootstrap.CardBody(
                        html.P("Teaching for a better future", className="card-text")
                    ),
                ],
                style={"width": "18rem"},
            ), style={"margin-left": "100px"}
        )
    ]),

])
app.layout = html.Div([header, content])


if __name__ == '__main__':
    app.run(debug=True)
