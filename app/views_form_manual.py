from flask import Markup
from .forms import FormatDisplay
from flask import Blueprint, render_template, redirect, url_for, flash, request, session

bp_manuform = Blueprint('bp_manuform', __name__, url_prefix='')

@bp_manuform.route('/manual/', methods=['GET'])
def createManualTemplates():
    form = FormatDisplay(request.form)
    return render_template("manual_form.html", form= form)

@bp_manuform.route('/manual/', methods=['POST'])
def sendManualTemplates():
    form = FormatDisplay(request.form)
    reference_info_dic = {
                         "form_type":request.form.get('form-select'),
                         "website_type":request.form.get('website-select'),
                         "author":request.form.get('author'),
                         "year":request.form.get('year'),
                         "title":request.form.get('title'),
                         "magazine":request.form.get('magazine'),
                         "is_publisher":request.form.get('IsPublisher'),
                         "publisher":request.form.get('publisher'),
                         "is_volume":request.form.get('IsVolume'),
                         "volume":request.form.get('volume'),
                         "is_issue":request.form.get('IsIssue'),
                         "issue":request.form.get('issue'),
                         "url":request.form.get('url'),
                         "page":request.form.get('page')
                          }
    manual = ManualFormatter(reference_info_dic)
    current_result= manual.funcAll()
    print('BEGINING WITH :',session)
    if session.get('results') is None:
        print('session.clear-------')
        session.clear()
    if not 'results' in session:
        session['results'] = []
        session['results'].append(current_result)
        session['results'] = session['results']
        print('result_nameをcreated')
        print(type(session.get('results')))
        return render_template("manual_form.html", form= form, current_result=current_result)
    if 'results' in session and current_result in session.get('results'):
        print("おなじ")
        return render_template("manual_form.html", form= form, current_result=current_result)
    if 'results' in session and not current_result in session.get('results'):
        if len(session['results']) == 6:
            session['results'].pop(0)
            session['results'].append(current_result)
            session['results'] = session['results']
            print('len 発動!!!!\n',session)
            return render_template("manual_form.html", form= form, current_result=current_result)
        print('count+1')
        session['results'].append(current_result)
        print(session)
        session['results'] = session['results']
        return render_template("manual_form.html", form= form, current_result=current_result)
    print('ERROR session.clear method conducted')
    session.clear()
    return render_template("manual_form.html", form= form, current_result=current_result)

class ManualFormatter:
    ref_dict = {}
    format_result = ''
    
    def __init__(self, arg_dict:dict) -> None:
        self.ref_dict = arg_dict
    # def changeEmptytoNone(self):
    #     'いらなくね？判断に必要なやつは全部GETしてる'
    #     for x,y in self.ref_dict.items():
    #         if y == '':
    #             self.ref_dict[x] = None
    #     self.ref_dict
    def get_JP_BOOK(self):
        '1)日本語 & 書籍'
        return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. {self.ref_dict.get('publisher')}. 全pp.{self.ref_dict.get('page')}.")
    def get_JP_JOURNAL(self, param_vol, param_iss):
        '2)日本語 & 雑誌'
        # 受け取ったis_~はすべて'true'(str)か、Noneになるため注意
        if param_vol == "true" and param_iss == "true":
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('volume')}({self.ref_dict.get('issue')}), {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        elif param_vol == "true" and param_iss == None:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('volume')}, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        elif param_vol == None and param_iss == "true": 
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('issue')}, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        else:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
    def get_JP_WEBSITE(self, param_webtype, param_pub):
        '3)日本語 & ウェブサイト'
        if param_webtype == "newspaper" and param_pub == 'true':
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. <em>{self.ref_dict.get('publisher')}</em>. <br>{self.ref_dict.get('url')}")
        elif param_webtype == "newspaper" and param_pub == None:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. <br>{self.ref_dict.get('url')}")
        elif param_webtype == "newssitearticle" and param_pub == 'true':
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. {self.ref_dict.get('publisher')}. <br>{self.ref_dict.get('url')}")
        else:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. <br>{self.ref_dict.get('url')}")
    def get_EN_BOOK(self):
        '4)英語 & 書籍'
        return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. {self.ref_dict.get('publisher')}. pp.{self.ref_dict.get('page')}.")

    def get_EN_JOURNAL(self, param_vol, param_iss):
        '5)英語 & 雑誌'
        if param_vol == 'true' and param_iss == 'true':
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('volume')}({self.ref_dict.get('issue')}), {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        elif param_vol == 'true' and param_iss == None:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('volume')}, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        elif param_vol == None and param_iss == 'true': 
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('issue')}, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
        else:
        #reference:https://uow.libguides.com/uow-harvard-guide/journals-no-volume
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. {self.ref_dict.get('publisher')}. <em>{self.ref_dict.get('magazine')}</em>, {self.ref_dict.get('page')}. <br>{self.ref_dict.get('url')}")
    def get_EN_WEBSITE(self, param_webtype, param_pub):
        '6)英語 & ウェブサイト　出版社の有無によってイタリックになる部分が変化'
        if param_webtype == "newspaper" and param_pub == 'true':
            '出版社が強調される'
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). {self.ref_dict.get('title')}. <em>{self.ref_dict.get('publisher')}</em>. <br>{self.ref_dict.get('url')}")
        elif param_webtype == "newspaper" and param_pub == None:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. <br>{self.ref_dict.get('url')}")
        elif param_webtype == "newssitearticle" and param_pub == 'true':
            'タイトルが協調'
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. {self.ref_dict.get('publisher')}. <br>{self.ref_dict.get('url')}")
        else:
            return Markup(f"{self.ref_dict.get('author')}. ({self.ref_dict.get('year')}). <em>{self.ref_dict.get('title')}</em>. <br>{self.ref_dict.get('url')}")

    def createFormatResult(self):
        form_type = self.ref_dict['form_type']
        website_type = self.ref_dict['website_type'] 
        is_volume = self.ref_dict['is_volume']
        is_issue = self.ref_dict['is_issue']
        is_publisher = self.ref_dict['is_publisher']
        
        if (form_type=="1"):
            self.format_result = self.get_JP_BOOK()
        elif(form_type=="2"):
            self.format_result = self.get_JP_JOURNAL(param_vol=is_volume, param_iss=is_issue)
        elif(form_type=="3"):
            self.format_result = self.get_JP_WEBSITE(param_webtype=website_type, param_pub=is_publisher)
        elif(form_type=="4"):
            self.format_result = self.get_EN_BOOK()
        elif(form_type=="5"):
            self.format_result = self.get_EN_JOURNAL(param_vol=is_volume, param_iss=is_issue)
        else:
            self.format_result = self.get_EN_WEBSITE(param_webtype=website_type, param_pub=is_publisher)
        return self.format_result
    # def getParam(arg:str) -> str or None:
    def funcAll(self) -> str:
        result = self.createFormatResult()
        return result
# @bp_manuform.route('/manual', methods=['GET', 'POST'])
# def manualGenerate():
# #TODO selectedvalueを取得し、結果を表示させると、書籍に戻る現象がある。
#     form = FormatDisplay()
# #dropdown_menu = ["日本語の書籍", "日本語の論文", "日本語のWEBサイト", "英語の書籍","英語の論文","英語のWEBサイト"]
#     if request.method == 'GET':
#         flash('Give us reference')
#         return render_template("manual_form.html", form= form)
#     else:
#         if form.validate_on_submit():
#             get_format_value = getFormatselectValue()
#             result = FormatGenerator(get_format_value)
#             print(result)
#             return render_template("manual_form.html", form=form, generate_data=result)
#         else:
#             flash("Invalid")
#             return render_template("manual_form.html", form=form)