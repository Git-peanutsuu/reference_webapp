import pytest
# ModuleNotFound 解決法 上のディレクトリのinitを外す　https://zenn.dev/pesuchin/articles/9573476d53d234f09433

def test_displat_homepage():
    from TranslationApp.app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
def test_Not_Found():
    from TranslationApp.app import app
    client = app.test_client()
    response = client.get('/notfound')
    assert 'Page Not Found' in response.text
    assert response.status_code == 404

from reference_webapp.app import create_app
@pytest.fixture()
def test_create_app():
    app_test = create_app(mode='DEV')
    app_test.config['TESTING'] = True
    #
    yield app_test

@pytest.fixture
def runner(app):
    """Clickのコマンドを呼び出し可能なrunner（実行者）を作成"""
    return app.test_cli_runner()
# -------------------------------------------------
# >coverage run -m pytest -v and > coverage report
# app\__init__.py                  49     15    69%
# app\auto_class.py                95     30    68%
# app\forms.py                     24      4    83%
# app\home.py                       5      1    80%
# app\tests\__init__.py             1      0   100%
# app\tests\conftest.py            27     13    52%
# app\tests\test_bp_auto.py        39      0   100%
# app\tests\test_bp_manual.py      64      0   100%
# app\views_form_auto.py           63     10    84%
# app\views_form_manual.py        105     18    83%
# config.py                        21      0   100%
# instance\config.cfg               4      0   100%
# -------------------------------------------------
# TOTAL                           497     91    82%
# pytest app\tests\conftest.py