\# LLMニュース分類アプリ



Gemini APIを活用して、RSSフィードから取得したニュースを自動的にカテゴリ分類するWebアプリケーションです。



!\[アプリのスクリーンショット](screenshot.png)



\## 📋 目次



\- \[概要](#概要)

\- \[機能](#機能)

\- \[システム構成](#システム構成)

\- \[技術スタック](#技術スタック)

\- \[セットアップ手順](#セットアップ手順)

\- \[使い方](#使い方)

\- \[ファイル構成](#ファイル構成)

\- \[カテゴリ変更から表示までのロジック](#カテゴリ変更から表示までのロジック)

\- \[トラブルシューティング](#トラブルシューティング)



---



\## 概要



このアプリケーションは、複数のRSSフィードからニュース記事を取得し、Gemini API（Google の生成AI）を使って各記事を「エンタメ」「テクノロジー」「ライフスタイル」の3つのカテゴリに自動分類します。



ユーザーはカテゴリボタンをクリックすることで、見たいカテゴリのニュースだけを表示できます。



---



\## 機能



\- ✅ 複数のRSSフィードから最新ニュースを自動取得

\- ✅ Gemini APIによる自動カテゴリ分類

\- ✅ カテゴリ別フィルタリング機能

\- ✅ レスポンシブデザイン（スマホ対応）

\- ✅ リアルタイム表示切り替え



---



\## システム構成



```

┌─────────────┐

│   RSS Feed  │ ← ニュース取得

└──────┬──────┘

&nbsp;      │

&nbsp;      ↓

┌─────────────┐

│  Backend    │

│  (Python)   │ → feedparserでRSS解析

│             │ → Gemini APIでカテゴリ分類

└──────┬──────┘

&nbsp;      │

&nbsp;      ↓ JSON形式でデータ送信

┌─────────────┐

│  Frontend   │

│ (HTML/JS)   │ → カテゴリボタンでフィルタリング

│             │ → ニュース一覧を動的表示

└─────────────┘

```



\### データフロー



1\. \*\*ニュース取得\*\*: バックエンドがRSSフィードから記事タイトル・リンク・日時を取得

2\. \*\*AI分類\*\*: 各記事タイトルをGemini APIに送信し、カテゴリを判定

3\. \*\*データ送信\*\*: 分類されたニュースをJSON形式でフロントエンドに送信

4\. \*\*表示\*\*: フロントエンドがカテゴリボタンに応じてニュースをフィルタリング表示



---



\## 技術スタック



\### バックエンド

\- \*\*Python 3.8+\*\*

\- \*\*Flask\*\*: 軽量Webフレームワーク

\- \*\*feedparser\*\*: RSSフィード解析

\- \*\*google-generativeai\*\*: Gemini API利用



\### フロントエンド

\- \*\*HTML5/CSS3\*\*

\- \*\*JavaScript (Vanilla)\*\*: フレームワーク不使用

\- \*\*Fetch API\*\*: 非同期通信



\### API

\- \*\*Gemini API (gemini-pro)\*\*: 自然言語処理・分類



---



\## セットアップ手順



\### 1. 必要なソフトウェアのインストール



\#### Python

\- \[Python公式サイト](https://www.python.org/downloads/)から3.8以上をダウンロード

\- インストール時に「Add Python to PATH」にチェックを入れる



\#### Git

\- \[Git公式サイト](https://git-scm.com/)からダウンロードしてインストール



\### 2. プロジェクトのクローン



```bash

git clone https://github.com/あなたのユーザー名/news-classifier.git

cd news-classifier

```



\### 3. 仮想環境の作成と有効化



\*\*Windows:\*\*

```bash

python -m venv venv

venv\\Scripts\\activate

```



\*\*Mac/Linux:\*\*

```bash

python3 -m venv venv

source venv/bin/activate

```



\### 4. 必要なライブラリのインストール



```bash

pip install -r requirements.txt

```



\### 5. Gemini APIキーの取得



1\. \[Google AI Studio](https://aistudio.google.com/app/apikey)にアクセス

2\. Googleアカウントでログイン

3\. 「Create API Key」をクリックしてAPIキーを取得



\### 6. 環境変数の設定



プロジェクトルートに `.env` ファイルを作成し、以下を記述：



```

GEMINI\_API\_KEY=あなたのAPIキーをここに貼り付け

```



\*\*⚠️ 重要\*\*: `.env` ファイルは絶対にGitにコミットしないでください！



\### 7. アプリケーションの起動



```bash

python app.py

```



成功すると以下のように表示されます：



```

&nbsp;\* Running on http://127.0.0.1:5000

```



\### 8. ブラウザでアクセス



ブラウザで `http://127.0.0.1:5000` を開いてください。



---



\## 使い方



\### 基本操作



1\. \*\*ページを開く\*\*: アプリが自動的にニュースを取得・分類します

2\. \*\*全てのニュースを見る\*\*: 「全て」ボタンをクリック（デフォルト）

3\. \*\*カテゴリ別に見る\*\*: 「エンタメ」「テクノロジー」「ライフスタイル」ボタンをクリック

4\. \*\*記事を読む\*\*: ニュースタイトルをクリックすると元記事が開きます



\### 読み込み時間について



\- 初回読み込み時、Gemini APIで各記事を分類するため \*\*10〜30秒\*\* かかります

\- 「ニュースを読み込み中...」と表示されている間お待ちください



---



\## ファイル構成



```

news-classifier/

├── app.py                 # メインプログラム（Flask）

├── .env                   # 環境変数（APIキー）※Gitで管理しない

├── .gitignore             # Git除外ファイル設定

├── requirements.txt       # 依存ライブラリ一覧

├── README.md              # このファイル

├── static/

│   └── style.css         # CSSスタイルシート

└── templates/

&nbsp;   └── index.html        # HTMLテンプレート

```



\### 各ファイルの役割



\#### `app.py`

\- Flaskサーバーの起動

\- RSSフィードからニュース取得

\- Gemini APIによるカテゴリ分類

\- JSON APIエンドポイントの提供



\#### `index.html`

\- ユーザーインターフェース

\- カテゴリボタンの表示

\- ニュース一覧の動的表示

\- フィルタリング機能



\#### `style.css`

\- デザイン・レイアウト

\- レスポンシブ対応

\- ホバーエフェクト



\#### `.env`

\- Gemini APIキーを保存

\- \*\*絶対に公開しない\*\*



\#### `requirements.txt`

```

flask==3.0.0

feedparser==6.0.11

google-generativeai==0.3.2

python-dotenv==1.0.0

```



---



\## カテゴリ変更から表示までのロジック



\### 1. ページ読み込み時



```javascript

window.addEventListener('DOMContentLoaded', async () => {

&nbsp;   await fetchNews();  // ニュース取得開始

});

```



\- ページが開かれると自動的に `/api/news` エンドポイントにリクエスト

\- バックエンドが全RSSフィードからニュースを取得

\- 各ニュースタイトルをGemini APIに送信して分類

\- 分類結果を含むJSONデータを返却



\### 2. ニュース取得（`fetchNews()`）



```javascript

async function fetchNews() {

&nbsp;   const response = await fetch('/api/news');

&nbsp;   allNews = await response.json();  // 全ニュースを保存

&nbsp;   displayNews(allNews);  // 表示

}

```



\- 取得した全ニュースをグローバル変数 `allNews` に保存

\- 初回は「全て」カテゴリで表示



\### 3. カテゴリボタンクリック時



```javascript

btn.addEventListener('click', () => {

&nbsp;   currentCategory = btn.dataset.category;  // カテゴリ更新

&nbsp;   displayNews(allNews);  // 再表示

});

```



\- クリックされたボタンの `data-category` 属性を取得

\- `currentCategory` を更新

\- `displayNews()` を呼び出して表示を更新



\### 4. ニュース表示（`displayNews()`）



```javascript

function displayNews(news) {

&nbsp;   const filteredNews = currentCategory === 'all' 

&nbsp;       ? news 

&nbsp;       : news.filter(item => item.category === currentCategory);

&nbsp;   

&nbsp;   // フィルタリングされたニュースをDOM に追加

}

```



\- `currentCategory` が「all」なら全て表示

\- それ以外なら、`category` プロパティが一致するニュースのみ表示

\- \*\*再取得はしない\*\*（クライアント側でフィルタリング）



\### 5. バックエンド分類処理（`classify\_news\_with\_gemini()`）



```python

def classify\_news\_with\_gemini(title):

&nbsp;   prompt = f"""

&nbsp;   タイトル: {title}

&nbsp;   このニュースを以下から1つ選んで分類:

&nbsp;   - エンタメ

&nbsp;   - テクノロジー

&nbsp;   - ライフスタイル

&nbsp;   """

&nbsp;   response = model.generate\_content(prompt)

&nbsp;   category = response.text.strip()

&nbsp;   return category

```



\- 各ニュースタイトルをプロンプトに埋め込み

\- Gemini APIに送信

\- 返却されたカテゴリ名をニュースオブジェクトに付与



---



\## トラブルシューティング



\### Q1: 「ModuleNotFoundError」が出る



\*\*原因\*\*: 必要なライブラリがインストールされていない



\*\*解決策\*\*:

```bash

pip install -r requirements.txt

```



\### Q2: 「API key not valid」エラー



\*\*原因\*\*: `.env` ファイルの設定が間違っている



\*\*解決策\*\*:

1\. `.env` ファイルにAPIキーが正しく記載されているか確認

2\. APIキーに余計なスペースや改行がないか確認

3\. Gemini APIキーが有効か確認



\### Q3: カテゴリ別でニュースが表示されない



\*\*原因\*\*: Gemini APIの分類結果がカテゴリ名と完全一致していない



\*\*解決策\*\*:

`app.py` の `classify\_news\_with\_gemini()` 関数でデバッグ出力を確認：

```python

print(f"分類結果: '{category}'")

```



\### Q4: ニュースの取得が遅い



\*\*原因\*\*: Gemini APIは各記事ごとに呼び出すため時間がかかる



\*\*対策\*\*:

\- `fetch\_news\_from\_rss()` の `limit` パラメータを減らす（現在5件）

\- キャッシュ機能を実装する（応用）



\### Q5: ポート5000が使用中



\*\*原因\*\*: 他のアプリケーションがポート5000を使用している



\*\*解決策\*\*:

`app.py` の最後を変更：

```python

app.run(debug=True, port=5001)  # ポート番号を変更

```



---



\## ライセンス



このプロジェクトはMITライセンスの下で公開されています。



---



\## 作成者



\- \*\*氏名\*\*: \[あなたの名前]

\- \*\*所属\*\*: \[学校名・学科名]

\- \*\*作成日\*\*: 2025年12月



---



\## 参考資料



\- \[Flask公式ドキュメント](https://flask.palletsprojects.com/)

\- \[Gemini API ドキュメント](https://ai.google.dev/docs)

\- \[feedparser ドキュメント](https://pythonhosted.org/feedparser/)

\- \[README書き方ガイド](https://qiita.com/mzmz\_\_02/items/b219c1592404abda52d)

