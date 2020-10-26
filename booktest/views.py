from django.shortcuts import render
from django.views import View
from booktest.models import HeroInfo
from django.http import JsonResponse, HttpResponse


# Create your views here.


class TestView(View):

    def get(self, request):
        try:
            heros = HeroInfo.objects.all()
        except:
            return HttpResponse('请求错误')
        else:
            heros_list = []
            for hero in heros:
                heros_list.append({
                    "id": hero.id,
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle
                })
            return JsonResponse({
                "code": "200",
                "message": "OK",
                "heros": heros_list
            })

    def post(self, request):

        import json
        req_dict = json.loads(request.body)
        hname = req_dict.get('hname')
        hgender = req_dict.get('hgender')
        hcomment = req_dict.get('hcomment')
        hbook_id = req_dict.get('hbook_id')
        try:
            HeroInfo.objects.get(hname=hname)

            # hero.save()
        except HeroInfo.DoesNotExist:
            HeroInfo.objects.create(hname=hname, hgender=hgender, hcomment=hcomment, hbook_id=hbook_id)
            hero = HeroInfo.objects.get(hname=hname)
            json_ = {
                "code": "200",
                "message": "OK",
                "heros": {
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle
                }
            }

            return JsonResponse(json_)
        else:
            return HttpResponse('输入有误')


class HeroView(View):
    def get(self, request, id):
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return HttpResponse('查无此人')
        else:
            json_ = {
                "code": "200",
                "message": "OK",
                "heros": {
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle
                }
            }
            return JsonResponse(json_)

    def put(self,request,id):
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return HttpResponse('查无此人')
        else:
            import json
            req_dict = json.loads(request.body)
            hname = req_dict.get('hname')
            hgender = req_dict.get('hgender')
            hcomment = req_dict.get('hcomment')
            hbook_id = req_dict.get('hbook_id')
            hero.hname = hname
            hero.hgender = hgender
            hero.hcomment = hcomment
            hero.hbook_id = hbook_id
            hero.save()
            json_ = {
                "code": "200",
                "message": "OK",
                "heros": {
                    "id": hero.id,
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle
                }
            }

            return JsonResponse(json_)

    def delete(self, request, id):
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return HttpResponse('查无此人')
        else:
            hero.delete()
            json_ = {
                "code": 0,
                "message": "OK"
            }
            return JsonResponse(json_)
