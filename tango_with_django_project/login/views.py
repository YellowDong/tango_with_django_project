from django.shortcuts import render, redirect, reverse
from login.models import User, Confirm
from login.forms import LoginForm, RegisterForm
import hashlib
import datetime
from django.conf import settings
from django.utils import timezone


def hash_code(s, salt='mysite'):
    hash = hashlib.sha256()
    s += salt
    hash.update(s.encode())
    code = hash.hexdigest()
    return code


def fonfirm_email_code(user):
    now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    Confirm.objects.create(code=code, user=user)  # 把生成的确认码和对应的用户存到确认模型中，等待用户到接收的邮件中确认对比确认码
    return code


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '来自xiaoyunliu.pro博客注册确认信息'
    text_content = '欢迎注册xiaoyunliu的博客，本博客专注于Python和Django技术的分享！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员'
    html_content = '''
                    <p>感谢注册<a href="http://{0}/user/confirm/?code={1}" target=blank>www.xiaoyunliu.pro</a>，\
                    这里是xiaoyunliu的博客和教程站点，专注于Python和Django技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{2}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm_obj = Confirm.objects.get(code=code)
        if confirm_obj:
            c_time = confirm_obj.c_time
            now = timezone.now()
            if now > c_time + datetime.timedelta(days=settings.CONFIRM_DAYS):
                message = '注册信息已经过期，请重新注册'
                confirm_obj.user.delete()
                return render(request, 'login/confirm.html', locals())
            else:
                confirm_obj.user.has_confrimed = True
                confirm_obj.user.save()
                confirm_obj.delete()
                message = '感谢确认， 请使用账户登录'
                return render(request, 'login/confirm.html', locals())
    except Confirm.DoesNotExist as e:
        message = '无效的确认请求'
        return render(request, 'login/confirm.html', locals())


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect(reverse('user:index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        message = "所有字段都必须填写"
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(name=username)
                if not user.has_confrimed:
                    message = '该用户还未通过邮件确认！'
                    return render(request, 'login/login.html', locals())
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect(reverse('user:index'))
                else:
                    message = "password error"
            except:
                message = "user is no exit"
        return render(request, 'login/login.html', locals())
    form = LoginForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect(reverse('user:index'))
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = fonfirm_email_code(new_user)
                send_email(email, code)
                message = '请到你的邮箱中确认注册信息'
                return render(request, 'login/confirm.html', locals())

    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login'):
        return redirect(reverse('user:index'))
    request.session.flush()
    return redirect(reverse('user:index'))
