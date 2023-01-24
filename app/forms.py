from flask_wtf import FlaskForm
from nbformat import ValidationError
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired
import re
from flask import flash

class FormatDisplay(FlaskForm):
    #manualのform.htmlのFlaskForm
    author = StringField('author/著者:', validators=[DataRequired(message="必須です")])
    year = StringField('year/年:', validators=[DataRequired(message="参考した文献の発行年数は必須です")])
    title = StringField('title/タイトル:', validators=[DataRequired(message="参考文献のタイトルは必須です")])
    magazine = StringField('magazine/研究名:')
    publisher = StringField('publisher/発行機関・運営社名:')
    volume = StringField('volume/巻:')
    issue = StringField("issue/号:")
    page = StringField('page/ページ:')
    url = URLField('URL or doi:')
    submit = SubmitField('reflect')

    # def validate_title(self, title):
    #     """バリデーション内容
    #     - 「」をタイトルのところで使用するので、禁止
    #     """
    #     if "「" in title.data or "」" in title.data:
    #         raise ValidationError("サブタイトルは「」ではなく『』を使用して下さい")

    # def validate_year(self, year):
    #     """バリデーション内容
    #     - ()を日付のところで使用するので、禁止
    #     """
    #     if "(" in year.data or "（" in year.data:
    #         raise ValidationError("()もしくは()を含める必要はありません")
class CiniiSearch(FlaskForm):
    #url_form.htmlの方のFlaskForm
    url_name = URLField('CiNii論文URL入力欄',
                        validators=[DataRequired(message="必須です")])
    def validate_url(self, url_name):
        'URLにマッチしなかった場合、ValidationError'
        url_pattern = re.compile("(https://cir.nii.ac.jp/crid/)+")
    #https://cir.nii.ac.jp/crid/1390001205712913152
    #https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+
        if not url_pattern.match(url_name):
            return False
        return True
            # raise ValidationError('*現在CiNiiのURLのみのご使用をお願いしております。')