from flask import Flask, render_template, request
app = Flask(__name__)

# Team logos dictionary
team_logos = {
    "49ers": "https://static.nfl.com/static/site/img/logos/teams/SF.svg",
    "Chiefs": "https://static.nfl.com/static/site/img/logos/teams/KC.svg",
    "Eagles": "https://static.nfl.com/static/site/img/logos/teams/PHI.svg",
    "Cowboys": "https://static.nfl.com/static/site/img/logos/teams/DAL.svg"
    # Add more teams here...
}

@app.route('/')
def home():
    return render_template('index.html', weeks=range(1, 18))

@app.route('/scores')
def scores():
    week = request.args.get('week', default=1, type=int)
    scores_data = [
        {"home_team": "49ers", "away_team": "Chiefs", "home_score": 27, "away_score": 24},
        {"home_team": "Eagles", "away_team": "Cowboys", "home_score": 21, "away_score": 17}
    ]
    return render_template('scores.html', scores=scores_data, logos=team_logos)

if __name__ == '__main__':
    app.run(debug=True)
