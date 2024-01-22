from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import datetime
import json

# config.jsonからappidを読み込む
with open('config.json', 'r') as file:
    config = json.load(file)

query = 'pokemon'
try:
    # Findingクラスのインスタンスを作成し、APIに接続
    api = Finding(appid=config['appid'], config_file=None)
    # 'findItemsAdvanced' APIメソッドを実行し、キーワード'pokemon'で商品を検索
    response = api.execute('findItemsAdvanced', {'keywords': query})

    # レスポンスが成功であることを確認
    assert(response.reply.ack == 'Success')
    # タイムスタンプがdatetimeオブジェクトであることを確認
    assert(type(response.reply.timestamp) == datetime.datetime)
    # 検索結果がリストであることを確認
    assert(type(response.reply.searchResult.item) == list)

    # 検索結果の各商品について、タイトルと現在価格を出力
    for item in response.reply.searchResult.item:
        print(item.title, item.sellingStatus.currentPrice.value)

except ConnectionError as e:
    # ConnectionErrorが発生した場合、エラーとそのレスポンスの辞書を出力
    print(e)
    print(e.response.dict())
    
