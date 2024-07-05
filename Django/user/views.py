from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class RegisterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([username, email, password]):
            return JsonResponse({'error': '所有字段均为必填项'}, status=400)

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': '用户名已存在'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': '电子邮件地址已存在'}, status=400)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()
        return JsonResponse({'message': '注册成功'}, status=201)