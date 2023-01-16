# from TranslationApp.app import create_app
import requests
from requests.exceptions import Timeout
from flask import Markup, flash

class auto:
    def __init__(self):
        import re
        self.pattern = re.compile(r'^[A-Z]{1}[A-Z|1-2]{1}-')
        self.prefix_word_dict = {}
        self.prefix_word_list = ['TY','AU','PY','TI','PB','T2','VL','IS','SP','UR','DO']
        self.url = ''
    def seturl(self, form_data:str) -> requests.models.Response:
        'this function is independent of flow of programm. This is used in try-catch syntax with url.raise_for_status'
        self.url = requests.get(form_data, timeout= (3.0,7.5))#https://docs.python-requests.org/en/latest/user/advanced/#timeout
        return self.url

    def toRISResponse(self, str:str)-> requests.models.Response:

        str = str+'.ris'
        ris_response = requests.get(str)
        return ris_response
    def hasValidresponse(self, url_response:requests.models.Response) -> bool:
        if url_response.ok:
            return True
        else:
            return False
    def getRISTextfromResponse(self, response:requests.models.Response) -> str:
        return response.text
    def getTestValue(self) -> str:
        'テストのtextを取得する'
        self.test_text = """TY  - JOUR
                 AU  - 伊藤, 滉彩
                 AU  - 池内, 宏維
                 AU  - 稲坂, まりな
                 AU  - 高木, みき
                 AU  - 中川, 純
                 AU  - 松山, 洋一
                 AU  - 田辺, 新一
                 TI  - 非対面環境におけるコミュニケーションに必要なアウェアネスに関する調査
                 T2  - 日本建築学会環境系論文集
                 SN  - 1348-0685
                 PB  - 日本建築学会
                 PY  - 2022
                 DA  - 2022-12
                 VL  - 87
                 IS  - 802
                 SP  - 907-913
                 UR  - https://cir.nii.ac.jp/crid/1390012801498788352
                 DO  - 10.3130/aije.87.907
                 ER  -"""
        return self.test_text
    def splitCreateList(self,response_text:str) -> list:
        """
        文書に対して、スペースが開いているところを改行し、一行一行を各要素としてリストに代入する
        example:
        >>> a aa/nb bb/nc cc
        [aaa, bbb, ccc]
        """
        auto_list = response_text.replace(' ','').split('\n')
        #AUがMultipleならthrough pattern　→
        return auto_list
    def makeAuthorUsable(self, auto_list:list) ->None:
        """複数の場合がある著者を、辞書に7使いやすいようにフォーマットを整えてから、リストに戻してそのリストを返す
        >>>makeAUthorUsable(list) #['AU-aaa','AU-bbb','AU-ccc', …]
        list #['AU-aaa, bbb, ccc', …]
        """
        added_text = ''
        for num ,text in enumerate(auto_list[:]):
            if text.startswith('AU-'):
                auto_list.remove(text)
                text = text.replace(',','')
                if num <2:
                    added_text += text
                else:
                    added_text += self.pattern.sub(', ',text)
        auto_list.insert(1, added_text)
    def createDict(self, auto_list:list) -> dict:
        """
        リスト1つとselfのリストをitertool.produxtで全組みあわせを出力し、predixをもつtextだけを抽出し、dictを作成
        >>>createDict(test_list)
        test_dict
        """
        import itertools
        for prefix, tmp_text in itertools.product(self.prefix_word_list, auto_list):
            if tmp_text.startswith(prefix):
                tmp_text= self.pattern.sub('',tmp_text)
                if prefix == 'T2':
                    'T2にはaaa=aaaとなっていることがあり、後半部分を削除'
                    tmp_text =tmp_text[:tmp_text.find('=')]
                self.prefix_word_dict[prefix]=tmp_text
        return self.prefix_word_dict
    def hasDOIsinDictionary(self, dic:dict) ->None:
        'do not use'
        if dic.get('DO'):
            print(dic.get('DO'))
            return 'doi'
        elif dic.get('DO') is None and dic.get('UR'):
            print('DOisNone, but UR exists')
            return 'url'
        elif dic.get('DO') is None and dic.get('UR') is None:
            print('DOisNone, and UR is None')
            return 'doi_and_url_none'
        else:
            pass
    def hasVLorISinDictionary(self, dic:dict) ->None:
        pass
    def get_result(self, dic:dict) -> Markup:
        "URLやDOIをチェック + VOLUMEとISSUEを出力"
        #FIXME NOT READABLE dic.getを何回も使用するため、ifを多用
        #TODO 対応 本
        if dic.get('DO') is None and dic.get('UR'):
            'DOIはないが、URLはある'
            if dic.get('VL') is None:
                'URLONLY+ VL(ボリューム/巻)がない場合 = issue Number exists'
                # VOVUMEがない場合、発行年数PYを代わりに入れ、PY(IS)の場合もあるため変更の可能性 
                # https://libguides.wintec.ac.nz/APA7/faqs/missing
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("IS")}, {dic.get("SP")}.<br>{dic.get("UR")}')
                return result
            elif dic.get('IS') is None:
                'URLONLY+ IS(イシュー/号)がない場合　= Volume Number exsits'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}, {dic.get("SP")}.<br>{dic.get("UR")}')
                return result
            else:
                'URLONLY + volume と issueが両方が存在'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}({dic.get("IS")}), {dic.get("SP")}.<br>{dic.get("UR")}')
                return result
        elif dic.get('DO'):
            'DOIがある場合、URLの有無にかかわらずhttps:~を追加しDOIを出力'
            if dic.get('VL') is None:
                'doiが存在 + VL(ボリューム/巻)がない場合 = issue Number exists'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("IS")}, {dic.get("SP")}.<br>https://doi.org/{dic.get("DO")}')
                return result
            elif dic.get('IS') is None:
                'doiが存在 + IS(イシュー/号)がない場合　= Volume Number exsits'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}, {dic.get("SP")}.<br>https://doi.org/{dic.get("DO")}')
                return result
            else:
                'doiが存在 = volume と issueが存在 = '
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}({dic.get("IS")}), {dic.get("SP")}.<br>https://doi.org/{dic.get("DO")}')
                return result
        else:
            'DOIとURLがない場合'
            if dic.get('VL') is None:
                'DOIとURLがない場合 + VL(ボリューム/巻)がない場合 = issue Number exists'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("IS")}, {dic.get("SP")}.')
                return result
            elif dic.get('IS') is None:
                'DOIとURLがない場合 + IS(イシュー/号)がない場合　= Volume Number exsits'
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}, {dic.get("SP")}.')
                return result
            else:
                'DOIとURLがない場合 + volume と issueが存在 = '
                result = Markup(f'{dic.get("AU")}. ({dic.get("PY")}). {dic.get("TI")}. {dic.get("PB")}. <i>{dic.get("T2")}</i>, {dic.get("VL")}({dic.get("IS")}), {dic.get("SP")}.')
                return result
    def callCreateresultFunctions(self, resp):
        """
        call methods form getting response to generating result that is Marked up. 
        This function is called after checked if url and response are valid.
        """
        text = self.getRISTextfromResponse(resp)
        text_list = self.splitCreateList(text)
        self.makeAuthorUsable(text_list)
        auto_dict = self.createDict(text_list)
        current_result = self.get_result(auto_dict)
        return current_result