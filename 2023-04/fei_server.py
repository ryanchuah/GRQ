import datetime
from flask import Flask, request


name_to_count_mapping = None


winner = None


app = Flask(__name__)


def template_html(body_content: str) -> str:
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">

            <!--Let browser know website is optimized for mobile-->
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            </head>

            <body>
                <h2></h2>
                <div style="margin:auto;width:50%;">
                    {body_content}
                    
                </div>

            </body>
        </html>
        """


@app.route("/")
def index():
    global name_to_count_mapping
    global winner

    if winner is not None:
        return template_html(
            f"<h1>Fuck {winner}.</h1><h1>Thank you for playing Get Rick Quik</h1>"
        )

    name_and_count_table_data = [
        f"<td>{idx+1}</td><td>{name}</td><td>{name_to_count_mapping[name]}</td>"
        for idx, name in enumerate(name_to_count_mapping)
    ]
    return template_html(
        f"""
            <h3>Leaderboard:</h3>
            <table>
                <thead>
                    <tr>
                        <th>Position</th>
                        <th>Name</th>
                        <th>Times this name has been picked</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join([f"<tr>{table_data}</tr>" for table_data in name_and_count_table_data])}
                </tbody>
            </table> 
            </span><a class="button" onClick="window.location.reload();" href="#"><span class="pln">Refresh!</span></a><span class="pln">
            """
    )


@app.route("/update_leaderboard", methods=["POST"])
def update_leaderboard():
    global name_to_count_mapping
    if request.headers["API_KEY"] == "herfwiughreouighrewogiuwerhgoergrewoh":
        name_to_count_mapping = request.json["name_to_count_mapping"]
        return ""
    else:
        return "Fuck you"


@app.route("/end_lottery", methods=["POST"])
def end_lottery():
    global winner
    if request.headers["API_KEY"] == "herfwiughreouighrewogiuwerhgoergrewoh":
        winner = request.json["winner"]
        return ""
    else:
        return "Fuck you"
