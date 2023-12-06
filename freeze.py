from flask_frozen import Freezer
from website import create_app  # Replace 'your_flask_app' with the actual name of your Flask app

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def landing():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()
