import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '来自zmy',
        '欢迎你来访问',
        '123@sina.com',
        ['13469124614@qq.com'],
    )