from flask_frozen import Freezer
from website import create_app

app = create_app()
freezer = Freezer(app, with_static_files=True)  # Use with_static_files=True to include static files

@freezer.register_generator
def landing():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()
