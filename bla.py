# Flask Server
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
from flask import make_response
from sqlalchemy import create_engine


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'super_secret_key'
        self.engine = create_engine('sqlite:///catalog.db')
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
        self.session = self.engine.connect()
        self.session.execute('PRAGMA foreign_keys = ON')
        self.session.commit()
        self.session.close()
