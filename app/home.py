from flask import render_template, request, redirect, url_for, Blueprint
bp_home = Blueprint('bp_home', __name__, url_prefix='')
@bp_home.route('/', methods=['GET'])
def index():
    return render_template('home.html')
#home.htmlに直接views_form_manual or autoのfunctionを書き込むことで(yrl_for('bp_manual.manualGenerate'))
#下記は必要ない。というか動作しない
# @bp_home.route('/', methods=['POST'])
# def transPage1():
#     print("transPage1(generate) is done")
#     return redirect(url_for('bp_autoform.autoGenerate'))
# def transPage2():
#     print("transPage2(diplay) is done")
#     return redirect(url_for('bp_manuform.manualGenerate'))
#やる必要ないが、form.submit(value=auto)などどしてもできそう　複数 submit