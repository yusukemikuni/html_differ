import urllib.request
from bs4 import BeautifulSoup
import datetime
import codecs
import difflib
import os
import re

def get_html(url):
    # URLからHTTPレスポンスを取得
    html = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    return html

def save_as_file(html):
    #今日の日付の取得
    today = datetime.date.today()
    #ファイル名の指定
    file_name = 'src/{}.html'.format(str(today))
    #ファイルの作成
    with codecs.open(file_name,'wb','cp932', 'ignore') as f:
        f.write(str(html))

def print_diff(before_html, today_html):
    #HTMLファイルの差分の解析
    result = difflib.ndiff(before_html, today_html)
    #HTMLファイルの差分の解析
    result_list = list(result)
    #HTMLファイルの差分と行数のみを出力
    for Index, i in enumerate(result_list, 1):
        if '?' == i[0] or ' ' == i[0]:
            continue
        elif '+' or '-' == i[0]:
            print(str(Index)+'行|'+i)

def main():
    #今日の日付を取得
    today = datetime.date.today()
    #昨日の日付を取得
    yesterday = today - datetime.timedelta(days=1)

    #HTTPレスポンスを取得するURLの指定
    url = 'https://docs.python.jp/3/library/difflib.html'

    #HTMLファイルを作成するディレクトリへ移動
    os.chdir('C:\\Users\YUSUKE\Downloads')
    save_as_file(get_html(url))

    #今日のHTMLファイルの読み込み
    today_file = 'src/{}.html'.format(str(today))
    with open(today_file, 'r', encoding='cp932') as today_f:
        today_html = today_f.readlines()

    #昨日のHTMLファイルの読み込み
    try:
        yesterday_file = 'src/{}.html'.format(str(yesterday))
        with open (yesterday_file,'r', encoding='cp932') as yesterday_f:
            yesterday_html = yesterday_f.readlines()
    #昨日のファイルがない場合
    except FileNotFoundError:
        #HTMLファイルがあるディレクトリへ移動
        os.chdir('C:\\Users\YUSUKE\Downloads\src')
        #カレントディレクトリのパスを取得
        dir = os.getcwd()
        #ファイルのリストの取得
        files = os.listdir(dir)
        #カウンターの初期化
        count = 0
        #カレントディレクトリのファイル数をカウントする
        for file in files:
            index = re.search('.html',file)
            if index:
                count += 1

        #今日のHTMLファイルしかない場合
        if count <= 1:
            print('比較するファイルがありません。')

        #比較するHTMLファイルがある場合
        else:
            num = 1
            while num < 30:
                #遡る日付の指定
                day = yesterday - datetime.timedelta(days=num)
                before_file = '{}.html'.format(str(day))
                #ファイルの中に指定した日のファイルが存在するか確認
                if before_file in files:
                    with open (before_file,'r',encoding='cp932') as before_f:
                        before_html = before_f.readlines()
                        break
                #ファイルの中に指定した日のファイルが存在しない
                else:
                    num += 1
        print_diff(before_html, today_html)

if __name__ == '__main__':
    main()
