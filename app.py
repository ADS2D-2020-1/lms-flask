from flask import Flask, g
from db import get_db, query_db


app = Flask(__name__)


@app.before_request
def before_request():
    g.db = get_db()
    g.query_db = query_db


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


from controllers import *


if __name__ == "__main__":
    app.run(
        debug=True
    )

