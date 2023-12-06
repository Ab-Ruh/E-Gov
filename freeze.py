"""
This module is where we start the Flask application.
"""

from flask_frozen import Freezer
from website import create_app

app = create_app()
freezer = Freezer(app)

if __name__ == '__main__':
    # Uncomment the following line to freeze the app into static files
    # freezer.freeze()
    app.run(debug=True)
