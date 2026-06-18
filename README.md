# FastAPI Todo API on AWS EC2 (Docker + Terraform)

FastAPIで作成したCRUD APIをDockerコンテナとして構築し、Terraformで作成したAWS EC2上へデプロイしたポートフォリオです。

Swagger UIを外部公開しており、ブラウザからAPIの動作確認が可能です。

## 公開URL

Swagger UI
http://13.113.6.129/docs


## 概要

このプロジェクトでは以下を実施しました。

* FastAPIによるCRUD API開発
* Dockerによるコンテナ化
* GitHubによるソースコード管理
* TerraformによるAWSインフラ構築
* Security Group設定による通信制御
* AWS EC2（Ubuntu Server）へのデプロイ
* Dockerコンテナとしてアプリケーションを公開
* Swagger UIによるAPIドキュメント公開

## 使用技術

* Python 3.11
* FastAPI
* Uvicorn
* Docker
* Terraform
* AWS EC2
* AWS Security Group
* Git / GitHub
* Ubuntu (WSL)

## API一覧

* GET /health - ヘルスチェック
* GET /items - 一覧取得
* POST /items - 作成
* GET /items/{item_id} - 詳細取得
* PUT /items/{item_id} - 更新
* DELETE /items/{item_id} - 削除

## 構成

1. TerraformでEC2とSecurity Groupを作成
2. GitHubからアプリケーションを取得
3. Dockerイメージをビルド
4. Dockerコンテナを起動
5. FastAPIを外部公開

## ディレクトリ構成

.
├── Dockerfile
├── main.py
├── requirements.txt
└── .gitignore
