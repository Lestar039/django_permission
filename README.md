# django_permission

**ТЗ**

Дано:

3 пользователя: user_1, user_2, user_3.

3 пункта меню: Menu 1, Menu 2, Menu 3.

3 таблицы с данными: Тable 1 (ДФО, ЦФО, ДФО, УФО, ЦФО), Тable 1 (ЦФО, ДФО, ЦФО, СФО, СЗФО, ДФО), Тable 1 (СФО, ЦФО, СФО, УФО, СЗФО).

Реализовать:

Нажатие по Menu 1 отображает данные из Тable 1, по Menu 2 из Тable 2, по Menu 3 из Тable 3.

user_1 видит Menu 1, Menu 2, Menu 3 и все данные.

user_2 видит Menu 1, Menu 2 и данные, ограниченные ДФО.

user_3 видит Menu 2, Menu 3 и данные, ограниченные СФО.

**Инструкция по запуску**

1. git clone https://github.com/Lestar039/django_permission.git
2. pip install -r requirements.txt
3. ./manage.py migrate
4. ./manage.py createsuperuser
5. ./manage.py runserver
6. http://127.0.0.1:8000/admin
7. Создать 3 groups: 'group_1', 'group_2', 'group_3'
8. Создать 3 users: 'user_1', 'user_2', 'user_3' 
9. Добавить юзеров в группы: user_1 -> group_1, user_2 -> group_2, user_3 -> group_3
10. Добавить данные в Table 1 (ДФО, ЦФО, ДФО, УФО, ЦФО)
11. Добавить данные в Table 2 (ЦФО, ДФО, ЦФО, СФО, СЗФО, ДФО)
12. Добавить данные в Table 3 (СФО, ЦФО, СФО, УФО, СЗФО)
13. Выходим из admin
14. http://127.0.0.1:8000 -> login
