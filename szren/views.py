# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from szren import models


class ProfessionalListViews(APIView):
    """专业列表"""
    def get(self, request):
        data = models.Professional.objects.all().values('id', 'name')
        return Response({"code": 0, "data": data})


class SubjectsListViews(APIView):
    """通过专业查科目列表"""

    def get(self, request):
        pro_id = request.GET.get('pro_id')
        data = models.Subjects.objects.filter(pro_id=pro_id).values('id', 'name')
        return Response({"code": 0, "data": data})


class AddChoiceViews(APIView):
    """添加选择题"""

    def post(self, request):
        title = request.data.get('title').strip
        exist = models.MultipleChoice.objects.filter(title=title)
        if exist:
            return Response({"code": 1, "msg": "该题目已有"})
        request.data['title'] = title
        models.MultipleChoice.objects.create(**request.data)
        return Response({"code": 0, "msg": "新建成功"})




