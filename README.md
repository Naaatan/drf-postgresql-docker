# DRF-PostgreSQL-Docker
DRF x PostgreSQL x nginx x gunicorn をDocker上に構築するためのテンプレート  

以下ファイルは適宜変更すること  

- apiv1/models.py
- apiv1/serializers.py
- apiv1/views.py
- docker.env
- docker.prod.env
- containers/postgres/init.sql
    - 'postgres'

## Development container

```
$ docker-compose up -d
```

## Production container

```
$ docker-compose -f docker-compose.prod.yml up -d
```

## Creating an administrator site login user
初回起動時、DRFコンテナ上でスーパーユーザーを作成  

```
$ docker exec -it DRF /bin/bash
root@XXX:/code# python manage.py createsuperuser
```

## Option
DRFコンテナ上で手動マイグレーション  

```
$ docker exec -it DRF /bin/bash  
root@XXX:/code# python manage.py makemigrations  
root@XXX:/code# python manage.py migrate  
```
