"""
Mock for Flask class
"""
class FlaskMock:
    """
    Mock for Flask class
    """

    def __init__(self, app):
        self.app = app
        self.config = Config()

    def __call__(self):
        return self.app

    def run(self):
        """
        Flask.run() method
        """
        return self.app

    def register_blueprint(self, route, url_prefix):
        """
        Flask.register_blueprint() method
        """
        path = url_prefix + route.name
        return path

class Config:
    """
    Mock for Config class
    """
    def __init__(self):
        self.config = {}

    def from_prefixed_env(self):
        """
        Config.from_prefixed_env() method
        """
        return self.config

    def __getitem__(self, key):
        return self.config[key]
