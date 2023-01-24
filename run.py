from app import app
from waitress import serve
# appフォルダからappオブジェクトをインポート
if __name__ == '__main__':
    #コマンドラインから実行すると、mainが格納される
    #つまりコマンドラインから実行されたとき、以下を実行するという意味
    #importされたときには、nameにはモジュール名が格納されるため、以下の文は実行されない。
    serve(app, host='0.0.0.0', port=5000)

# app created learning these sPites
# -https://blog.wordvice.jp/%E5%BC%95%E7%94%A8-citation-%E8%91%97%E8%80%85%E5%90%8D-%E8%A1%A8%E8%A8%98%E6%B3%95-apa-mla-chicago/
# -https://apastyle.apa.org/style-grammar-guidelines/references/examples/journal-article-references

#app
#license pyproject requirements.txt
#run.py
# - view
#   view/_init_.pyで公開
#   view/homepy
#     - templates
#     - static
#          - js
#          - img
# - venv (venv内にSRC必要ない)
# - test