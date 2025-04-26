from django.shortcuts import render
from django.http import JsonResponse # 추가
from django.shortcuts import get_object_or_404 #추가
from django.views.decorators.http import require_http_methods # 추가
from .models import * # 추가
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 방명록 생성, 전체 조회
@csrf_exempt
@require_http_methods(["POST","GET"])
def guestbook_list(request):

    if request.method == "POST":

        body = json.loads(request.body.decode('utf-8'))

        #새로운 데이터 생성
        new_guestbook = GuestBook.objects.create(
            title = body['title'],
            guest = body['guest'],
            content = body['content'],
            password = body['password'],
        )
        # Json 형태 반환 데이터 생성
        new_guestbook_json = {
            "title" : new_guestbook.title,
            "guest" : new_guestbook.guest,
            "content" : new_guestbook.content,
            "password" : new_guestbook.password,
        }

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 생성 성공',
            'data' : new_guestbook_json
        })
    if request.method == "GET":
        guestbook_all = GuestBook.objects.all()

        guestbook_json_all = []

        for guestbook in guestbook_all:
            guestbook_json = {
                "title" : guestbook.title,
                "guest" : guestbook.guest,
                "content" : guestbook.content,
                "password" : guestbook.password
            }
            guestbook_json_all.append(guestbook_json)

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 목록 조회 성공',
            'data' : guestbook_json_all
        })

# 방명록 단일 조회, 단일 삭제
@csrf_exempt
@require_http_methods(["GET","DELETE"])
def guestbook_detail(request, guestbook_id): #이건 URL 경로 변수

    # guestbook_id에 해당하는 단일 방명록 조회
    if request.method == "GET":
        guestbook = get_object_or_404(GuestBook, pk=guestbook_id)

        guestbook_json = {
            "title" : guestbook.title,
            "guest" : guestbook.guest,
            "content" : guestbook.content,
            "password" : guestbook.password
        }

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 단일 조회 성공',
            'data' : guestbook_json
        })
    if request.method == "DELETE":
        delete_guestbook = get_object_or_404(GuestBook, pk=guestbook_id)
        
        #비밀번호 가져오기
        body = json.loads(request.body.decode('utf-8'))
        input_password = body.get('password')

        if not input_password:
            return JsonResponse({
                'status' : 400,
                'message' : '비밀번호가 입력되지 않았습니다.',
                'data' : None
            })
        
        if input_password != delete_guestbook.password:
            return JsonResponse({
                'status' : 403,
                'message' : '비밀번호가 일치하지 않습니다.',
                'data' : None
            })
        
        delete_guestbook.delete()

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 삭제 성공',
            'data' : None
        })
