from .app import app


@app.route('/')
def main_page():
    return '<h1>API for KPI 2nd year Databases coursework. Yaroslav Vysotskyi</h1>'