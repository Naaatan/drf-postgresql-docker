# DRF-PostgreSQL-Docker
DRF x PostgreSQL をDocker上に構築するためのテンプレート  

以下ファイルは適宜変更すること  

- apiv1/models.py
- apiv1/serializers.py
- apiv1/views.py
- docker.env
- docker.prod.env

## コンテナの作成と起動

Dockerファイルのビルド/起動  
```
$ docker-compose up -d
```

DRFコンテナ上でマイグレーション  
```
$ docker exec -it DRF /bin/bash
root@XXX:/code# python manage.py makemigrations
root@XXX:/code# python manage.py migrate
```