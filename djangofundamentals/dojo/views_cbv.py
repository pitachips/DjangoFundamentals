
# Chapter 4
from django.views.generic import View
from django.http import HttpResponse

class PostlistView(View):
    'CBV: 직접 문자열로 HTML형식 응답하기'

    def get(self, request):
        # html =  '''
        #         <h1>Django Fundamentals</h1>
        #         <p>{chapter}</p>
        #         <p>뷰에 대한 오버뷰</p>'''.format(chapter='Ch.4')  이렇게 해도 괜찮고 따로 함수로 빼도 괜찮음
        html = self.get_template_string().format(chapter='Ch.4')
        return HttpResponse(html)

    def get_template_string(self):
        return '''
                <h1>Django Fundamentals</h1>
                <p>{chapter}</p>
                <p>뷰에 대한 오버뷰</p>'''

# as_view()의 리턴값이 대입되는 post_list1은 urls.py에서 지정된 callable의 이름과 동일
post_list1 = PostlistView.as_view()


from django.views.generic import TemplateView

class PostlistView2(TemplateView):
     'CBV: 템플릿을 통해 HTML형식 응답하기'

     template_name = 'dojo/post_list.html'

     def get_context_data(self):
         context = super().get_context_data() #TemplateView가 가지고 있는 context까지 쓰기 위해 함수 호출. 
         context['name'] = '공유'
         return context

post_list2 = PostlistView2.as_view()


from django.http import JsonResponse

class PostlistView3(View):
    'CBV: JSON 형식 응답하기'

    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message':'Django Fundamentals',
            'items': ['파이썬', '장고', 'celery', 'AWS'],
        }

post_list3 = PostlistView3.as_view()


import os
from django.conf import settings


class ExcelDownloadView(View):
    'CBV: 엑셀 다운로드 응답하기'

    filepath = os.path.join(settings.BASE_DIR, 'dojo/others/Book1.xls')
    
    def get(self, request):
        filename = os.path.basename(self.filepath)
        # 인스턴스 변수 호출 시 self.변수 로 호출해야함을 항상 기억할 것
        with open(self.filepath, 'rb') as f:     
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            # filename은 인스턴스 변수가 아니므로 self 불필요
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response

excel_download = ExcelDownloadView.as_view()


# 실제 CBV를 사용할 때에는 View를 직접 상속받기보다
# View를 한차례 상속한 TemplateView, ListView, UpdateView, CreateView 등을 사용함