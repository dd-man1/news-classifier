import os
import feedparser
import google.generativeai as genai
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# Flaskアプリの初期化
app = Flask(__name__)

# Gemini APIの設定
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# RSSフィードのURL
RSS_FEEDS = {
    'エンタメ': 'https://natalie.mu/music/feed/news',
    'テクノロジー': 'https://rss.itmedia.co.jp/rss/2.0/news_bursts.xml',
    'ライフスタイル': 'https://www.lifehacker.jp/feed/index.xml'
}

# カテゴリ定義
CATEGORIES = ['エンタメ', 'テクノロジー', 'ライフスタイル']


def fetch_news_from_rss(rss_url, limit=5):
    """RSSフィードからニュースを取得"""
    feed = feedparser.parse(rss_url)
    news_list = []
    
    for entry in feed.entries[:limit]:
        news_list.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.get('published', '日時不明')
        })
    
    return news_list


def classify_news_with_gemini(title):
    """Gemini APIでニュースを分類"""
    prompt = f"""
以下のニュース記事のタイトルを、次のカテゴリのいずれか1つに分類してください。

【カテゴリ】
- エンタメ
- テクノロジー
- ライフスタイル

【タイトル】
{title}

【回答形式】
カテゴリ名のみを1つ回答してください。余計な説明は不要です。
上記3つのカテゴリのいずれかを必ず選んでください。
"""
    
    try:
        response = model.generate_content(prompt)
        category = response.text.strip()
        
        # カテゴリ名の正規化（余計な文字を削除）
        category = category.replace('**', '').replace('*', '').replace('「', '').replace('」', '').strip()
        
        print(f"APIレスポンス: '{category}'")  # デバッグ用
        
        # カテゴリが正しいか確認
        if category in CATEGORIES:
            return category
        # 部分一致で検索
        for cat in CATEGORIES:
            if cat in category:
                return cat
        
        # どれにも該当しない場合
        return 'その他'
    except Exception as e:
        print(f"分類エラー: {e}")
        return 'その他'


@app.route('/')
def index():
    """トップページ"""
    return render_template('index.html', categories=CATEGORIES)


@app.route('/api/news')
def get_news():
    """全ニュースを取得してカテゴリ分類"""
    all_news = []
    
    # 各RSSフィードからニュースを取得
    for category, rss_url in RSS_FEEDS.items():
        news_list = fetch_news_from_rss(rss_url, limit=5)
        
        # 各ニュースをGemini APIで分類
        for news in news_list:
            classified_category = classify_news_with_gemini(news['title'])
            news['category'] = classified_category
            print(f"タイトル: {news['title'][:30]}... → 分類結果: {classified_category}")  # デバッグ用
            all_news.append(news)
    
    return jsonify(all_news)


if __name__ == '__main__':
    app.run(debug=True, port=5000)