from firebase_admin import credentials,initialize_app,storage
import urllib.request
from urllib.parse import urlencode


#firebase認証
cred = credentials.Certificate("loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json")
initialize_app(cred,{'storageBucket': 'gs://loadimage-9bac0.appspot.com'})

bucket = storage.bucket('loadimage-9bac0.appspot.com')
#アップロード用
filenameup = 'hanba-gu6321.png'
path = '/Users/yuto_shinohara/Documents/Programming/python/textdata/python firebase/'
#ダウンロード用
filenamedown = "Item"

#urlクエリパラメータ
q_data = {
    'q': 'Pythonでクエリパラメータを作成',
    'option': [1, 3, 5],
    'lang': 'jp',
}

#アップロード
def upload_blob(filenameup, path):
    blob = bucket.blob(filenameup)
    blob.upload_from_filename(path + filenameup)
    blob.make_public()
    print(blob.public_url)  

#ダウンロード
def download_blob(filenamedown, path):
    blob = bucket.blob(filenamedown)
    blob.download_to_filename(path + filenamedown)
    blob.make_public()
    print(blob.public_url) 
    # qs = urlencode(q_data)
    # firebasedownloadurl = blob.public_url + qs
    # print(firebasedownloadurl)
    urllib.request.urlretrieve(blob.public_url)
    print("ダウンロード完了")
    
#実行
if __name__ == '__main__':
    download_blob(filenamedown,path)

