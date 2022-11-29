# API_YATUBE - АПИ сервис для Ятуб

Апи для сервиса ятуб. Создавайте посты, регистрируйтесь, подписывайтесь, оставляйте комментарии, загружайте фото!



## Технологии

- Django==4.1.3
- django-filter==22.1
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- djoser==2.1.0
- Pillow
- SimplJwt
- 
со всем остальным можете ознакомиться в файлу requirements.txt

## Installation

```sh
git clone ####
```
```sh
python3 -m ven venv
```
```sh
python3 source venv/bin/activate <--for mac
python source venv/sctipts/activate <--for Windows
```
```sh
pip install -r requirements.txt
```


## Тестовые запросы

To see all Endpoints


```sh
GET 127.0.0.1:8000/api/v1/
```

Get all posts
```sh
GET 127.0.0.1:8000/api/v1/posts/
```
Get specific post
```sh
GET 127.0.0.1:8000/api/v1/posts/<post_id:int>
```

Create Post
```sh
POST 127.0.0.1:8000/api/v1/posts/

JSON
{
    "text": "text of your post"
}
```

PUT, PATH post
```sh
POST 127.0.0.1:8000/api/v1/posts/<post_id:int>

JSON
{
    "text": "putted, patched"
}
```

Delette post
```sh
DELETTE 127.0.0.1:8000/api/v1/posts/<post_id:int>
```
Register new user
```sh
POST 127.0.0.1:8000/api/v1/users/

JSON

{
    "username": "Ivan",
    "password": "password"
}
```

CREATE JWT TOKEN
```sh
POST 127.0.0.1:8000/api/v1/jwt/create/

JSON

{
    "username": "Ivan",
    "password": "password"
}
```


## License

MIT
