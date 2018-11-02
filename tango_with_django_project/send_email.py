import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'tango_with_django_project.settings'

if __name__ == '__main__':
    # send_mail('from www.xiaoyunliu.pro test email',
    #           'welcome visit www.xiaoyunliu.pro',
    #           '787773580@qq.com',
    #           ['helovecandy@gmail.com'],
    #           )

    subject, from_email, to = 'from www.xiaoyunliu.pro test email', '787773580@qq.com', 'helovecandy@gmail.com'
    text_content = 'welcome www.xiaoyunliu.pro,this is xiaoyunliu blog and python tutorial'#text_content是用于当html内容无效时的替代文本
    html_content = '<p>welcome to visit <a href="http://www.xiaoyunliu.pro" target=blank>www.xiaoyunliu.pro</a>,this is xiaoyunliu blog</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()