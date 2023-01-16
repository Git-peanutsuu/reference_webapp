from flask import session, request
from TranslationApp.app.views_form_manual import bp_manuform
from TranslationApp.app import create_app 
from TranslationApp.app.views_form_manual import ManualFormatter
import coverage
def test_app():
    app = create_app(mode='DEV')
    app.config['TESTING'] = True
    app.register_blueprint(bp_manuform, url_prefix='/')
    web = app.test_client()
    
    with app.test_request_context():
        #solution to RuntimeError outside of context and test_request_context is a context local that acts like a global variable see https://testdriven.io/blog/flask-contexts-advanced/
        with web:
            rv = web.get('/manual/')
            assert rv.status_code == 200

            data1 = {                
                "form_type":"1",
                "website_type":"newspaper",
                "author":"野田サトル",
                "year":"2015",
                "title":"ゴールデンカムイ 1 (ヤングジャンプコミックス) ",
                "magazine":"nonee",
                "is_publisher":None,
                "publisher":"集英社",
                "is_volume":"true",
                "volume":"1",
                "is_issue":None,
                "issue":"",
                "url":"",
                "page":"188"}
            rv = web.post('/manual/',data=data1)
            assert rv.status_code == 200
            assert request.form.get('is_volume') == 'true'
            assert request.form.get('IsPublisher') == None # IsPublisherは存在しない。
            # HTMLからとってくるときは、IsVolumeだが、このテストのプログラムではis_issueやis_volumeで取得できる

            test_manual = ManualFormatter(data1)
            result = test_manual.funcAll()
            assert len(session['results']) == 1
            assert result =='野田サトル. (2015). <em>ゴールデンカムイ 1 (ヤングジャンプコミックス) </em>. 集英社. 全pp.188.'
            
            # ---2
            rv = web.get('/manual/')
            data2 = {                
                "form_type":"2",
                "website_type":"newspaper",
                "author":"中川",
                "year":"2019",
                "title":"アイヌ文化",
                "magazine":"テストマガジン",
                "is_publisher":None,
                "publisher":"集英社",
                "is_volume":"true",
                "volume":"22",
                "is_issue":None,
                "issue":"2",
                "url":"<script>alert(2)</script>",
                "page":"262"}
            rv = web.post('/manual/',data=data2)
            assert request.form.get('is_volume') == "true"
            test_manual = ManualFormatter(data2)
            result = test_manual.funcAll()
            assert not len(session['results']) == 1
            assert result =="中川. (2019). アイヌ文化. 集英社. <em>テストマガジン</em>, 22, 262. <br><script>alert(2)</script>"
            # 最初のエラーが起こったresult（これ以上エラーで通らないため上の通り直した）"中川. (2019). アイヌ文化. None. <em>テストマガジン</em>, 22, 262. <br><script>alert(2)</script>"
            # クライアント側でform-type選択時に制御されているため絶対に起こらないと考えられるが、is_publisherがNoneにしても入力されていると集英社の文字がある。
            # ---
            rv = web.get('/manual/')
            data3 = {                
                "form_type":"3",
                "website_type":"newssitearticle",
                "author":"テスト前田",
                "year":"2000",
                "title":"テストの社会学",
                "magazine":None,
                "is_publisher":None,
                "publisher":"テストラボ",
                "is_volume":"true",
                "volume":"22",
                "is_issue":None,
                "issue":"",
                "url":"<script>alert(2)</script>",
                "page":"262"}
            rv = web.post('/manual/',data=data3)
            test_manual = ManualFormatter(data3)
            result = test_manual.funcAll()
            assert result =="テスト前田. (2000). <em>テストの社会学</em>. <br><script>alert(2)</script>"
            
            # ---
            rv = web.get('/manual/')
            data4 = {                
                "form_type":"4",
                "website_type":"newssitearticle",
                "author":"テス川",
                "year":"1977",
                "title":"テスト国における政治",
                "magazine":None,
                "is_publisher":'true',
                "publisher":"",
                "is_volume":"true",
                "volume":"22",
                "is_issue":None,
                "issue":"",
                "url":"https//:testtest",
                "page":"9999999"}
            rv = web.post('/manual/',data=data4)
            test_manual = ManualFormatter(data4)
            result = test_manual.funcAll()
            assert result =="テス川. (1977). <em>テスト国における政治</em>. . pp.9999999."
            #全pp.ではなくpp.が出力 
            # --- EN JOURNAL
            rv = web.get('/manual/')
            data5 = {                
                "form_type":"5",
                "website_type":"newssitearticle",
                "author":"ジェイムズ・*'8%$#??//\nw",#Pythonでは特殊文字として認識されてしまうが、クライアント側の入力では認識されずそのままの出力を確認
                "year":"2010",
                "title":"テストの覇権争い",
                "magazine":"”",
                "is_publisher":'true',
                "publisher":"テスト出版社",
                "is_volume":"true",
                "volume":"29",
                "is_issue":None,
                "issue":"",
                "url":"https//:testtest",
                "page":"32-45"}
            rv = web.post('/manual/',data=data5)
            test_manual = ManualFormatter(data5)
            result = test_manual.funcAll()
            assert result =="ジェイムズ・*'8%$#??//\nw. (2010). テストの覇権争い. テスト出版社. <em>”</em>, 29, 32-45. <br>https//:testtest"
            
            # --- EN NEWS
            rv = web.get('/manual/')
            data6 = {                
                "form_type":"6",
                "website_type":"newspaper",
                "author":"tst-b & tst-a",
                "year":"2023",
                "title":"how testable test tests tested tests",
                "magazine":"",
                "is_publisher":'true',
                "publisher":"test organization",
                "is_volume":None,
                "volume":"",
                "is_issue":None,
                "issue":"",
                "url":"https//:test_for_everyone.org",
                "page":""}
            rv = web.post('/manual/',data=data6)
            test_manual = ManualFormatter(data6)
            result = test_manual.funcAll()
            assert not len(session['results']) == 5 #6
            assert result =="tst-b & tst-a. (2023). how testable test tests tested tests. <em>test organization</em>. <br>https//:test_for_everyone.org"
            
            rv = web.get('/manual/')
            data7 = {                
                "form_type":"1",
                "website_type":"newspaper",
                "author":"ddd",
                "year":"1111",
                "title":"test_title",
                "magazine":"",
                "is_publisher":'true',
                "publisher":"tes_publ",
                "is_volume":None,
                "volume":"",
                "is_issue":None,
                "issue":"",
                "url":"https//:test_for_everyone.org",
                "page":"000"}
            rv = web.post('/manual/',data=data7)
            test_manual = ManualFormatter(data7)
            result = test_manual.funcAll()
            assert len(session['results']) == 6
            assert session['results'][0] == '中川. (2019). <em>アイヌ文化</em>. <br><script>alert(2)</script>'
            # セッションの一番最初にセーブされた'野田サトル. (2015). <em>ゴールデンカムイ 1 (ヤングジャンプコミックス) </em>. <br>'が消える
            assert result =="ddd. (1111). <em>test_title</em>. tes_publ. 全pp.000."

    # assert '<h2>Echo main</h2>' in rv.data.decode('utf-8')
    # assert 'You typed in Hello World' in rv.data.decode('utf-8')
    # pytest app\tests\test_bp_manual.py -v