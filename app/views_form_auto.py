from flask import Blueprint, render_template, redirect, url_for
from flask import flash, request, session
from .forms import CiniiSearch
import requests
from requests.exceptions import HTTPError
from TranslationApp.app.auto_class import auto
import logging
bp_autoform = Blueprint('bp_autoform', __name__, url_prefix='')
#Blueprintはアプリの機能の違うファイルに分割化appとviewsを分けたいとき？
#普通であればimport _init_モジュールか、_ini_のファイルにルーティングする
@bp_autoform.route('/auto/',methods=['GET','POST'])
def createAutoTemplates():
    form = CiniiSearch(request.form)
    if request.method == 'POST' and form.validate_url:
        'POSTとvalidationが通った場合にのみFuncAutoを出力'
        print('VALIDATION SECCESS')
        form_data = form.url_name.data
        return FuncAuto(form_data)
    else:
        return render_template('auto_form.html', form=form)

@bp_autoform.route('/auto/')
def FuncAuto(form_data):
    form = CiniiSearch(request.form)
    auto_class = auto()
    try:
        url = auto_class.seturl(form_data)
        url.raise_for_status()
        print("GREAT")
    except HTTPError as e:
        # 存在しないURLをキャッチする
        print('error message:',e.response.status_code,e.response.reason )
        print(e)
        flash("*リクエストに失敗しました 無効なURLなどの原因があります:requests.exceptions.HTTPError")
        # abort(404)
        return render_template('auto_form.html',form=form), 404#requests.exceptions.HTTPError
    resp = auto_class.toRISResponse(form_data)
    if auto_class.hasValidresponse(resp) == False:
        # CiNiiのURLではないURLがバリデーションを通過してしまった際のエラー
        print('NOT valid error message: 404 ,requests.exceptions.RequestException')
        flash("*リクエストに失敗しました 無効なURLなどの原因があります:requests.exceptions.RequestException")
        return render_template('auto_form.html',form=form), 404#requests.exceptions.RequestException
    
    current_result = auto_class.callCreateresultFunctions(resp)
    
    print('BEGINING WITH :',session)
    if session.get('results') is None:
        print('session.clear-------')
        session.clear()
    if not 'results' in session:
        session['results'] = []
        session['results'].append(current_result)
        session['results'] = session['results']
        print('result_name created firstly')
        return render_template("auto_form.html", form= form, current_result=current_result)
    if 'results' in session and current_result in session.get('results'):
        print("same value sets")
        return render_template("auto_form.html", form= form, current_result=current_result)
    if 'results' in session and not current_result in session.get('results'):
        if len(session['results']) == 6:
            session['results'].pop(0)
            session['results'].append(current_result)
            session['results'] = session['results']
            print('len 発動!!!!\n',session)
            return render_template("auto_form.html", form= form, current_result=current_result)
        print('result appended')
        session['results'].append(current_result)
        print(session)
        session['results'] = session['results']
        return render_template("auto_form.html", form= form, current_result=current_result)
    print('ERROR session.clear method conducted')
    session.clear()
    return render_template('auto_form.html',form=form, current_result=current_result)
# @bp_autoform.errorhandler(404)
# def error_404(e):
#     'abort(404)からの呼び出し'
#     form = CiniiSearch(request.args)
#     print(e)
#     return render_template('auto_form.html', form=form), 404