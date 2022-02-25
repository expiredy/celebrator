from flask import Flask

WEB_APPLICATION = Flask(__name__)


@WEB_APPLICATION.route('/')
def greattings():
    return "<h2>Hello dumbass!</h2>"

@WEB_APPLICATION.route('/card', methods=["GET"])
def get_presetted_data():
    pass

def run():
    pass