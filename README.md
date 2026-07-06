# FastAPI Todo API on AWS EC2 (Docker + Terraform)

FastAPIでCRUD APIを作成し、Dockerでコンテナ化しました。
インフラはTerraformでAWS EC2とSecurity Groupを構築し、クラウド上にデプロイしています。
Swagger UIを公開し、外部からAPIの動作確認が可能な構成にしています。

## 公開URL

* Swagger UI: http://13.113.6.129/docs

---

## 概要

このプロジェクトでは以下を実施しました。

* FastAPIによるCRUD APIの開発
* Dockerによるコンテナ化
* GitHubによるソースコード管理
* TerraformによるAWSインフラ構築
* Security Groupによる通信制御
* AWS EC2（Ubuntu Server）へのデプロイ
* Dockerコンテナとしてアプリケーションを公開
* Swagger UIによるAPIドキュメント公開

---

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

---

## API一覧

| Method | Endpoint         | Description |
| ------ | ---------------- | ----------- |
| GET    | /health          | ヘルスチェック     |
| GET    | /items           | Todo一覧取得    |
| POST   | /items           | Todo作成      |
| GET    | /items/{item_id} | Todo詳細取得    |
| PUT    | /items/{item_id} | Todo更新      |
| DELETE | /items/{item_id} | Todo削除      |

---

## インフラ構成

```text
Internet
    ↓
Security Group (80, 443, 22)
    ↓
EC2 (Ubuntu Server)
    ↓
Docker Container
    ↓
FastAPI Application
```

---

## 構築手順

1. TerraformでEC2とSecurity Groupを作成
2. EC2へSSH接続
3. GitHubからアプリケーションを取得
4. Dockerをインストール
5. Dockerイメージをビルド
6. Dockerコンテナを起動
7. Swagger UIで動作確認

---

## ディレクトリ構成

```text
.
├── Dockerfile
├── main.py
├── requirements.txt
├── main.tf
├── provider.tf
├── .terraform.lock.hcl
├── .gitignore
└── README.md
```
