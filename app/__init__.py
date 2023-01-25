import os
from flask import Flask, render_template
from config import ProductionConfig
from config import DefaultConfig
from datetime import timedelta
# import os
# def load_config(mode=os.environ.get('MODE')):
#     """Load config."""
#     try:
#         if mode == 'PRODUCTION':
#             from .production import ProductionConfig
#             return ProductionConfig
#         elif mode == 'TESTING':
#             from .testing import TestingConfig
#             return TestingConfig
#         else:
#             from .development import DevelopmentConfig
#             return DevelopmentConfig
#     except ImportError:
#         from .default import Config
#         return Config
# """Create Flask app."""
# config = load_config(mode)
# app = Flask(__name__)
# app.config.from_object(config)
def create_app(mode='DEV'):
    app= Flask(__name__, template_folder="templates", instance_path="/app/instance/")
    if mode == 'DEV':
        app.config.from_object(DefaultConfig)
        app.config.from_pyfile('config.cfg')
        # app.config.from_pyfile('config.cfg') 
        # Vscode can not recognize instance folder appropreately because of Pipenv set in the working directory
    else:
        app.config.from_object(ProductionConfig)
        app.config.from_envvar('config.cfg')
        # app.config.from_pyfile('config.cfg')

    #https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/config.html
    return app

def bad_request(e):
    errortitle = 'Bad Request 400'
    errortext = '送信されたリクエストに、何らかの原因で処理が完了できませんでした。'
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return render_template('error.html',errortitle=errortitle, errortext=errortext), 400
def page_not_found(e):
    errortitle = 'Page Not Found 404'
    errortext = 'お探しのページは一時的にアクセスができない状況にある可能性があります。URL、ファイル名にタイプミスがないか再度ご確認ください。'
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return render_template('error.html',errortitle=errortitle, errortext=errortext), 404
def internal_error(e):
    errortitle = 'Internal Server Error 500'
    errortext = '運営サーバーに問題が起こりました。もう一度やり直してください'
    # print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return render_template('error.html',errortitle=errortitle, errortext=errortext), 500
basedir = os.path.abspath(os.path.dirname(__file__))
#実行中のスクリプトを獲得
print('basedir==',basedir)

app = create_app(mode='PRO')
# for checking
# print("C O N F I G >>",app.config)
# print("instance_path === ",app.instance_path)
app.permanent_session_lifetime = timedelta(minutes=30)
app.register_error_handler(400, bad_request)
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_error)

from app.home import bp_home
app.register_blueprint(bp_home)
from app.views_form_manual import bp_manuform
app.register_blueprint(bp_manuform)
from app.views_form_auto import bp_autoform
app.register_blueprint(bp_autoform)
#blueprint does not have own url. no way of knowing which errorhandler run. So `app.~` is used here.
@app.route("/index")
def index():
  return render_template("index.html", config=app.config.items())


#TODO ✖でフォームの横にresetするボタンが欲しい in auto_form.html, in manual_form.html
#TODO 英語分権も。また、文章を入力すると、推測したところからもってきて
# virtualenvを使うべき他の仮想環境であるVENVよりも