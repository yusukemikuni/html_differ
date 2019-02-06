import datetime
import difflib

#今日の日付を取得
today = datetime.date.today()

#昨日の日付を取得
yesterday = today - datetime.timedelta(days=1)

#今日のHTMLファイルの読み込み
today_file = 'C:\\Users\YUSUKE\Downloads\{}.html'.format(str(today))
with open(today_file, 'r') as today_f:
    t = today_f.readlines()

#昨日のHTMLファイルの読み込み
yesterday_file = 'C:\\Users\YUSUKE\Downloads\{}.html'.format(str(yesterday))
with open (yesterday_file,'r') as yesterday_f:
    y = yesterday_f.readlines()

#HTMLファイルの差分の解析
result = difflib.Differ().compare(t, y)
diff = list(result)

#HTMLファイルの差分のみを取得
for i in diff:
    if "+" or "-"in i:
        print(i)
