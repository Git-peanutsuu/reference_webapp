from flask import Blueprint, render_template
from flask import flash, request, session
from .forms import CiniiSearch
from requests.exceptions import HTTPError, ConnectionError, ProxyError
import requests
from .auto_class import auto
from app import internal_error
bp_autoform = Blueprint('bp_autoform', __name__, url_prefix='')
#Blueprintはアプリの機能の違うファイルに分割化appとviewsを分けたいとき？
#普通であればimport _init_モジュールか、_ini_のファイルにルーティングする
@bp_autoform.route('/auto/',methods=['GET','POST'])
def createAutoTemplates():
    form = CiniiSearch(request.form)
    if request.method == 'POST':
        'POSTとvalidationが通った場合にのみFuncAutoを出力'
        if form.validate_url(form.url_name.data):
            form_data = form.url_name.data
            return FuncAuto(form_data)
        else:
            flash('*現在CiNiiのURLのみのご使用をお願いしております。')
            return render_template('auto_form.html', form=form)
    else:
        return render_template('auto_form.html', form=form)

@bp_autoform.route('/auto/')
def FuncAuto(form_data):
    form = CiniiSearch(request.form)
    auto_class = auto()
    try:
        url = requests.get(form_data, timeout= (3.0,7.5), verify=False)
        url.raise_for_status()
    except HTTPError as e:
        # 存在しないURLをキャッチする
        print('error message:',e.response.status_code,e.response.reason)
        print(e)
        flash("*リクエストに失敗しました 無効なURLなどの原因があります:requests.exceptions.HTTPError")
        return render_template('auto_form.html',form=form), 404#requests.exceptions.HTTPError
    except ProxyError as e:
        print('Proxyerror:',e)
        internal_error(e)
    except ConnectionError as e:
        print('ConnectionError:',e)
        internal_error(e)
    except Exception as e:
        internal_error(e)
    resp = auto_class.toRISResponse(form_data)
    if auto_class.hasValidresponse(resp) == False:
        # CiNiiのURLではないURLがバリデーションを通過してしまった際のエラー
        # print('NOT valid error message: 404 ,requests.exceptions.RequestException')
        flash("*リクエストに失敗しました 無効なURLなどの原因があります:requests.exceptions.RequestException")
        return render_template('auto_form.html',form=form), 404#requests.exceptions.RequestException

    current_result = auto_class.callCreateresultFunctions(resp)

    print('BEGINING WITH :',session)
    if session.get('results') is None:
        # print('session.clear-------')
        session.clear()
    if not 'results' in session:
        session['results'] = []
        session['results'].append(current_result)
        session['results'] = session['results']
        # print('result_name created firstly')
        return render_template("auto_form.html", form= form, current_result=current_result)
    if 'results' in session and current_result in session.get('results'):
        # print("same value sets")
        return render_template("auto_form.html", form= form, current_result=current_result)
    if 'results' in session and not current_result in session.get('results'):
        if len(session['results']) == 6:
            session['results'].pop(0)
            session['results'].append(current_result)
            session['results'] = session['results']
            # print('len 発動!!!!\n',session)
            return render_template("auto_form.html", form= form, current_result=current_result)

        session['results'].append(current_result)
        # print(session)
        session['results'] = session['results']
        return render_template("auto_form.html", form= form, current_result=current_result)
    # print('ERROR session.clear method conducted')
    session.clear()
    return render_template('auto_form.html',form=form, current_result=current_result)
