from app import app
# appフォルダからappオブジェクトをインポート
if __name__ == '__main__':
    #コマンドラインから実行すると、mainが格納される
    #つまりコマンドラインから実行されたとき、以下を実行するという意味
    #importされたときには、nameにはモジュール名が格納されるため、以下の文は実行されない。
    app.run(debug=True)
    #アプリを起動(ブラウザで立ち上がる様に)

# app created learning these sites
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