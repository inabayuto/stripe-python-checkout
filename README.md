# 簡易Stripe Checkoutアプリケーション

## 概要

このアプリケーションは、FlaskフレームワークとStripe APIを使用して、簡単な商品の購入フロー（チェックアウトセッションの作成から成功/キャンセルページへのリダイレクト）を実装したものです。

## 機能

- Stripe Checkoutを利用した簡単な支払い処理
- 簡易的な商品情報の表示
- 支払い成功/キャンセル時のページ表示

## 必要なもの

- Docker
- Docker Compose
- Stripe アカウント

## セットアップ

1. リポジトリをクローンします。

   ```bash
   git clone <リポジトリのURL>
   cd <クローンしたディレクトリ>
   ```

2. Stripe API キーを設定します。

   `app` ディレクトリ内に `.env` ファイルを作成し、以下の内容を記述します。

   ```env
   STRIPE_SECRET_KEY=sk_test_********************
   STRIPE_PUBLISHABLE_KEY=pk_test_********************
   ```

   `sk_test_` および `pk_test_` で始まるテスト用のAPIキーは、Stripeダッシュボードで取得できます。

## Dockerを使った起動方法

1. プロジェクトのルートディレクトリで以下のコマンドを実行し、Dockerコンテナをビルドして起動します。

   ```bash
   docker compose up --build -d
   ```

   ```bash
   docker exec -it CONTAINER ID bash
   ```

   初めての実行時はイメージのビルドに時間がかかる場合があります。

2. アプリケーションにアクセスします。

   Dockerコンテナが正常に起動したら、以下のURLにブラウザでアクセスしてください。

   ```
   http://localhost:4242/
   ```

3. アプリケーションの停止

   コンテナを停止するには、ターミナルで `Ctrl+C` を押すか、別のターミナルから以下のコマンドを実行します。

   ```bash
   docker-compose down
   ```

## ファイル構成

- `app/main.py`: Flaskアプリケーションのメインファイル。Stripe連携ロジックが含まれます。
- `app/templates/`: HTMLテンプレートが配置されます。
- `app/.env`: 環境変数（Stripe APIキー）を設定するファイル。
- `Dockerfile`: アプリケーションのDockerイメージをビルドするための定義ファイル。
- `docker-compose.yml`: Docker Composeを使ってコンテナを管理するための定義ファイル。
