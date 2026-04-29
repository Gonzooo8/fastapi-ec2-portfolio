# FastAPI Todo API on AWS EC2 (Docker)

FastAPIで作成したCRUD APIをDocker化し、AWS EC2（Amazon Linux 2023）上にデプロイしたポートフォリオです。  
Swagger UI を外部公開し、ブラウザからAPIの動作確認ができます。

- 公開URL: `http://13.211.123.75/docs#/`
- API仕様: OpenAPI（FastAPI自動生成）

---

## 概要

このプロジェクトでは、以下を実施しました。

- FastAPIでCRUD APIを作成
- Dockerでコンテナ化
- GitHubでソースコード管理
- AWS EC2（Amazon Linux 2023）にSSH接続
- EC2上でDockerをセットアップ
- コンテナ起動して外部公開（HTTP 80）

---

## 使用技術

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- AWS EC2 (Amazon Linux 2023)
- Git / GitHub
- Ubuntu (WSL) / PowerShell（ローカル作業）

---

## API一覧

- `GET /health` - ヘルスチェック
- `GET /items` - 一覧取得
- `POST /items` - 作成
- `GET /items/{item_id}` - 詳細取得
- `PUT /items/{item_id}` - 更新
- `DELETE /items/{item_id}` - 削除

Swagger UI:
- `/docs`

OpenAPI JSON:
- `/openapi.json`

---

## ディレクトリ構成

```text
.
├── Dockerfile
├── main.py
├── requirements.txt
└── .gitignore
