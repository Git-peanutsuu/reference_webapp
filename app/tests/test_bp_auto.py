from flask import session, request
from app.auto_class import auto
from app import create_app
from reference_webapp.app.views_form_auto import bp_autoform
from app.forms import CiniiSearch
def test_auto_app_get():
    app = create_app(mode='DEV')

    app.config['TESTING'] = True
    app.register_blueprint(bp_autoform, url_prefix='/')

    # web = app.test_client()
    with app.test_request_context():
        with app.test_client() as web:
            au = web.get('/auto/')
            assert au.status_code == 200
            assert 'CiNii' in au.text

def test_auto_app_post():
    app = create_app(mode='DEV')
    app.config['TESTING'] = True
    app.register_blueprint(bp_autoform, url_prefix='/')

    with app.test_request_context():
        with app.test_client() as web:
            auto_class = auto()
            pstapp = web.get('/auto/')
            pstapp = web.post('/auto/',data={
                "url_name":"https://cir.nii.ac.jp/crid/1050010920565"#https://cir.nii.ac.jp/crid/1050010920565071616わざとエラーを引き出す
            })
            assert pstapp.status_code == 404
            # requests.exceptions.HTTPError

            # ---
            pstapp = web.post('/auto/',data={"url_name":"https://stanford-code-the-change-guides.readthedocs.io/en/latest/guide_flask_unit_testing.html"})
            # different url format :requests.exceptions.RequestException
            assert pstapp.status_code == 200 #なぜか200
            error_form_data = request.form.get("url_name")
            resp = auto_class.toRISResponse(error_form_data)
            current_result = auto_class.callCreateresultFunctions(resp)

            # --- 1
            pstapp = web.post('/auto/',data={"url_name":"https://cir.nii.ac.jp/crid/1050010920565071616"})
            form_data = request.form.get("url_name")
            resp = auto_class.toRISResponse(form_data)
            current_result = auto_class.callCreateresultFunctions(resp)
            assert 'ホーム' in current_result
            assert len(session['results']) == 1

            # --- 2
            pstapp = web.post('/auto/',data={"url_name":"https://cir.nii.ac.jp/crid/1050282677747672704"})
            form_data = request.form.get("url_name")
            resp = auto_class.toRISResponse(form_data)
            current_result = auto_class.callCreateresultFunctions(resp)
            assert len(session['results']) == 2
#テストデータ
#＿　https://cir.nii.ac.jp/crid/1050564285852280704
#＿　https://cir.nii.ac.jp/crid/1390853649770127616「インド・ラダーク地方南東部チャンタン高原における遊牧と交易」
#＿　https://cir.nii.ac.jp/crid/1050282677776419712「場とは何か」
#＿　https://cir.nii.ac.jp/crid/1050282677747672704「オー線てぃすてぃ」
#＿　https://cir.nii.ac.jp/crid/1050010920565071616「移動する「ホーム」」
#＿　https://cir.nii.ac.jp/crid/1390572174831395456
#＿　https://cir.nii.ac.jp/crid/1390282680279480192　「都市への権利」が問うもの

def test_validation():
    'validationtest'
    app = create_app(mode='DEV')
    app.config['TESTING'] = True
    app.register_blueprint(bp_autoform, url_prefix='/')

    with app.test_request_context():
        with app.test_client() as web:
            # au = web.get('/auto/')
            form = CiniiSearch(request.form)
            assert form.validate_url('https://qiita.com/nagataaaas/items/3116352da186df102d96') == False
            assert form.validate_url('https://teratail.com/questions/144250') == False
            assert form.validate_url('https://cir.nii.ac.jp/crid/1390001204654523264') == True
            assert form.validate_url('https://urllib3.readthedocs.io/en/1.26.x/user-guide.html#ssl') == True 


    # pytest tests\test_bp_auto.py