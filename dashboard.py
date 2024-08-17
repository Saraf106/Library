from dash import Dash, dcc, ctx, html, Input, Output, State
import dash_bootstrap_components as bootstrap
from dash.long_callback import DiskcacheLongCallbackManager
import diskcache
from dash import dash_table
import pandas as pd
from src.retrieve_file import retrieve_options
from src.add_file import insert_file_dashboard




cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)
external_stylesheet = [bootstrap.themes.BOOTSTRAP, bootstrap.icons.BOOTSTRAP]
app = Dash(__name__, long_callback_manager=long_callback_manager, external_stylesheets=external_stylesheet)


list_path = "Database/list_options.csv"
data_path = "Database/database.csv"

df = pd.read_csv(data_path)
df = df[['FileName', 'Path', 'Subject', 'School', 'Year']]

def get_list_subject_and_school(list_path):

    subjects = retrieve_options(list_path)[0]
    schools = retrieve_options(list_path)[1]

    return subjects,schools


children_subject, children_school = get_list_subject_and_school(list_path)


#Structure of the page

header = bootstrap.Navbar(bootstrap.Container(html.H3("Jessica's School Library", style={'color': 'white'}, className="text-center"), fluid=True), dark=True, color='#c71585', sticky='top')


content = bootstrap.Container([
    bootstrap.Row(bootstrap.Col(html.Div("Look for a file here"),  style={"padding-top": "4%", "font-size": "24px"})),
    bootstrap.Row([

        bootstrap.Col([
            subject_drop := dcc.Dropdown(options = [x for x in sorted(df.Subject.unique())], placeholder="Subject", className='mb-3', style={"padding-top": "4%"})
        ]),

        bootstrap.Col([
            school_drop := dcc.Dropdown(options = [x for x in sorted(df.School.unique())], placeholder="School", className='mb-3', style={"padding-top": "4%"})
        ])
    ]),

    bootstrap.Row([
        #(table_header + table_body, bordered=True, style={"padding-top": "4%"})
        my_table :=
            dash_table.DataTable(
                columns=[
                    {'name': "FileName", 'id': 'FileName', 'type': 'text'},
                    {'name': "Path", 'id': 'Path', 'type': 'text'},
                    {'name': "Subject", 'id': 'Subject', 'type': 'text'},
                    {'name': "School", 'id': 'School', 'type': 'text'},
                    {'name': "Year", 'id': 'Year', 'type': 'numeric'},
                ],
                data=df.to_dict('records'),
                filter_action='native',
                page_size=8,

                style_data={
                    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'scroll-y': 'overflow'
                }
            )



    ]),

    bootstrap.Row(bootstrap.Col(html.Div("Save a new file here"),  style={"padding-top": "4%", "font-size": "24px"})),
    bootstrap.Row([
        bootstrap.Col([
            bootstrap.InputGroup(
                [bootstrap.InputGroupText("File Name"), bootstrap.Input(placeholder="Write the name of the file", id='InsertFileName' ), ],
                className="mb-3", size="lg", style={"padding-top": "2%"}
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("File path"), bootstrap.Input(placeholder="Write the path of the file" , id='InsertFilePath')],
                className="mb-3", size="lg"
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("Subject"), bootstrap.Input(placeholder="Write the subject name", id='InsertSubject')],
                className="mb-3", size="lg"
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("School"), bootstrap.Input(placeholder="Write the school name", id='InsertSchool')],
                className="mb-3", size="lg"
            ),

            bootstrap.InputGroup(
                [bootstrap.InputGroupText("Year"), bootstrap.Input(placeholder="Write the year", id='InsertYear')],
                className="mb-3", size="lg"
            ),

            bootstrap.Button("Add file", color="success", className="me-1", size="lg", id="addbutton"),
            bootstrap.Button("Clear", color="danger", className="me-1", size="lg", id="clearbutton"),

            bootstrap.Button("Click me", id="open-centered", size="lg"),
            bootstrap.Modal(
                [
                    bootstrap.ModalHeader(bootstrap.ModalTitle("Message"), close_button=True),
                    bootstrap.ModalBody("Ti voglio bene!!"),
                    bootstrap.ModalFooter(
                        bootstrap.Button(
                            "Close",
                            id="close-centered",
                            className="ms-auto",
                            n_clicks=0,
                        )
                    ),
                ],
                id="modal-centered",
                centered=True,
                is_open=False,
            ),

        ]),

        bootstrap.Col(
            bootstrap.Card(
                [
                    bootstrap.CardImg(src= "https://varthana.com/school/wp-content/uploads/2023/04/B296.jpg", top=True),
                    bootstrap.CardBody(
                        html.P("Teaching for a better future", className="card-text", style={"font-size": "20px"} )
                    ),
                ],
                style={"width": "18rem"},
            ), style={"margin-left": "100px"}, width = 3
        ),

        bootstrap.Col(
            bootstrap.Card(
                [
                    bootstrap.CardImg(src= "https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books-illustration_23-2149341898.jpg?size=626&ext=jpg", top=True),
                    bootstrap.CardBody(
                        html.P("", className="card-text", style={"font-size": "20px"} )
                    ),
                ],
                style={"width": "16rem", "height": "17rem"},
            ), style={"margin-left": "10px"}, width = 3

        )
    ]),

])
app.layout = html.Div([header, content])

@app.callback(
    Output(component_id=subject_drop,component_property="options"),
    Output(component_id=school_drop, component_property="options"),
    State(component_id="InsertFileName", component_property="value"),
    State(component_id="InsertFilePath", component_property="value"),
    State(component_id="InsertSubject", component_property="value"),
    State(component_id="InsertSchool", component_property="value"),
    State(component_id="InsertYear", component_property="value"),
    Input(component_id="addbutton", component_property="n_clicks")
)
def insert_callback(file_name = None, file_path = None, subject = None, school = None, year = None, click = None):
    print(click)
    if click is not None:
        if click > 0:
            #updated the two file csv with the new elements
            insert_file_dashboard(data_path, list_path, file_name, file_path, subject, school, year)
            dff = pd.read_csv(data_path)
            dff = dff[['FileName', 'Path', 'Subject', 'School', 'Year']]
            subjects = [x for x in sorted(dff.Subject.unique())]
            schools = [x for x in sorted(dff.School.unique())]
            print(subjects)
            print(schools)
            return subjects, schools
    else:
        return [x for x in sorted(df.Subject.unique())],[x for x in sorted(df.School.unique())]



@app.callback(
    Output(my_table, 'data'),
    Input(subject_drop, 'value'),
    Input(school_drop, 'value'),
    Input('addbutton', 'n_clicks')
)
def retrieve_file(subject, school, click):

    #dff = df.copy()
    dff = pd.read_csv(data_path)
    dff = dff[['FileName', 'Path', 'Subject', 'School', 'Year']]

    if school and subject:
        dff = dff[dff['Subject'] == subject]
        dff = dff[dff['School'] == school]
        print("DataFrame after filtering:\n", dff)
        return dff.to_dict('records')

    elif subject:
        dff = dff[dff['Subject'] == subject]
        print("DataFrame after filtering:\n", dff)
        return dff.to_dict('records')

    elif school:
        dff = dff[dff['School'] == school]
        print("DataFrame after filtering:\n", dff)
        return dff.to_dict('records')

    """
    if click:
        
        print("I have to print the updated table")
        print(dff)
        return dff.to_dict('records')
    """
    return dff.to_dict('records')

@app.callback(
    Output(component_id="InsertFileName", component_property="value"),
    Output(component_id="InsertFilePath", component_property="value"),
    Output(component_id="InsertSubject", component_property="value"),
    Output(component_id="InsertSchool", component_property="value"),
    Output(component_id="InsertYear", component_property="value"),
    Input(component_id="clearbutton", component_property="n_clicks"),
)
def clear_options(click):

    return None, None, None, None, None

@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run(debug=True)
