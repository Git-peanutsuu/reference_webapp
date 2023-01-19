# import pytest

# fixture デコレータにおける関数は、moduleベース。
# Pythonでは__init__.pyをすることでその位置にあるファイル軍はモジュールとして扱われている。
# initを作ることでおなじディレクトリ階層にあるファイルはfixtureを使うことができる。
# learn more - https://testdriven.io/blog/flask-pytest/#functional-test-examples
#            - https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/testing.html#form-data

# @pytest.fixture
# def client():
#     """Configures the app for testing

#     Sets app config variable ``TESTING`` to ``True``

#     :return: App for testing
#     """

#     #app.config['TESTING'] = True
#     client = app.test_client()

#     yield client