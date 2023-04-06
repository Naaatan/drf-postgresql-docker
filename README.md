# DRF-PostgreSQL-Docker
DRF x PostgreSQL x nginx をDocker上に構築するためのテンプレート  

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

初回起動時、DRFコンテナ上でスーパーユーザーを作成  
```
$ docker exec -it DRF /bin/bash
root@XXX:/code# python manage.py createsuperuser
```

DRFコンテナ上で手動マイグレーション  
```
$ docker exec -it DRF /bin/bash  
root@XXX:/code# python manage.py makemigrations  
root@XXX:/code# python manage.py migrate  
```