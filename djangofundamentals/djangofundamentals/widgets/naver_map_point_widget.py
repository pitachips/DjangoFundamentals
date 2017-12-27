import re
from django import forms
from django.conf import settings # 이는 django/conf/global_settings.py (베이스) + djangofundamentals.settings.py (재정의) 를 조합해서 가지고 있으므로 이렇게 사용
from django.template.loader import render_to_string


class NaverMapPointWidget(forms.TextInput):
    BASE_LNG, BASE_LAT  = '127.027636', '37.497921'  # 강남역 LNG 경도, LAT 위도

    def render(self, name, value, attrs):
        width = str(self.attrs.get('width', 800))
        height = str(self.attrs.get('height', 800))
        if width.isdigit(): width += 'px'
        if height.isdigit(): height += 'px'
        # 굳이 str 이후 isdigit()을 확인하는 이유는 width, height가 100, 2em, 80% 등으로 다양하게 정의되기 때문

        context = {
            'naver_client_id': settings.NAVER_CLIENT_ID,
            'id': attrs['id'],   # id_폼필드명 으로 생성되는 id 값임. 유일성 구분을 위해 필요
            'width': width,
            'height': height,
            'base_lng': self.BASE_LNG, # 경도
            'base_lat': self.BASE_LAT, # 위도
        }

        # 글을 수정하는 경우, 마커는 기존의 value에 해당하는 자리에 찍혀있어야 하므로 다음 코드 작성
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lng':lng, 'base_lat':lat})                
            except (IndexError, ValueError):
                pass

        html = render_to_string('widgets/naver_map_point_widget.html', context)
        # HttpResponse가 아닌 HTML 스트링을 리턴해야하므로 render_to_string 이용
       
        attrs['readonly'] = 'readonly'
        parent_html = super().render(name, value, attrs)
        # class Widget에 정의된 render함수는 위젯을 표현하는 HTML '스트링'을 리턴함

        return parent_html + html
        # TextInput 위젯이 렌더하는 텍스트인풋창을 아예 대체하는 것이 아니라,
        # 해당 텍스트인풋창은 그대로 두고 바로 그 밑에 네이버 지도가 보완적으로 그려지도록 함
        '''
        <input type="text" name="lnglat" maxlength="50" id="id_lnglat" />  # parent_html의 렌더
        <div style="width:100px; height:100px; background-color:red;">  # widgets/naver_map_point_widget.html 렌더
            네이버 지도를 그려봅시다.
        </div>
        '''

