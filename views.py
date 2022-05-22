from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .forms import SignupForm

# Create your views here.

#クラスベースビュー、フォームを指定してレコードを作成できる
class SignUp(CreateView):
    #Form指定
    form_class = SignupForm
    #Formページのテンプレート指定
    template_name = "useradmin/signup.html"
    #レコード作成後のリダイレクト先のURL指定、reverse_lazyで名前からURLに変更
    success_url = reverse_lazy('top')

    #自動で実行されるバリデーションの結果がvalidのとき実行される関数
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        #success_urlへリダイレクト
        return HttpResponseRedirect(self.get_success_url())

@login_required(login_url='login')
def top(request):
    loginuser = request.user
    params={'head':'TOP', 'msg':str(loginuser.username)+', Welcome to the community of Deep Learning(image processing)', }
    return render(request, 'useradmin/standard.html', params)
