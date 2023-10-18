from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from django.db import IntegrityError
from users.models import Article
from users.serializers import ArtisSerializer
from rest_framework import generics
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.models import Article
from users.serializers import ArtisSerializer
global_author =''
class ApiUser(viewsets.ViewSet):
    # 只有两个参数，默认路由后缀为方法名，可以添加第三个参数url_path='login'指定
    @action(methods=['post'], detail=False)
    def login(self, request):
        global global_author
        # 对象使用.获取，字典使用['key']获取
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        result = {
            "code": 200,
            "msg": "登录成功",
            "body": ""
        }
        if user is not None:
            global_author = username
            result = {
                "code": 200,
                "msg": "登录成功",
                "body": ""
            }
            return Response(result)
        else:
            result = {
                "code": -1,
                "msg": "登陆失败",
                "body": ""
            }
            return Response(result)
    
    @action(methods=['post'], detail=False)
    def register(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            password = make_password(password) 
            User.objects.create(username=username, password=password)
            result = {
                "code": 200,
                "msg": "注册成功",
                "body": ""
            }
            return Response(result)
        except IntegrityError as e:
            # 如果用户名重复，返回用户名重复的错误响应
            result = {
                "code": -1,
                "msg": "用户名已经被注册，请尝试不同的用户名。",
                "body": ""
            }
            return Response(result)
        except Exception as e:
            # 如果出现其他错误，返回自定义的错误响应
            result = {
                "code": -1,
                "msg": "注册失败，请联系管理员。",
                "body": ""
            }
            return Response(result)
    
    @action(methods=['post'], detail=False)
    def writeArticle(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        author = global_author
        if title and content:
            article = Article(title=title, content=content, author=author)
            article.save()
            print('qwe')
            result = {
                "code": 200,
                "msg": "已经保存",
                "body": ""
            }
            return Response(result)
        else:
            # 处理未经身份验证的用户，例如返回错误响应
                result = {
                "code": -1,
                "msg": "有空格",
                "body": ""
                }
                return Response(result)
    queryset = Article.objects.all()
    serializer_class = ArtisSerializer
    @action(methods=['post'], detail=False)
    def getin(self, request):
        deid = request.data.get('de_id')
        print(deid)
        deid = int(deid)
        article = get_object_or_404(Article, id=deid)
        serializer = ArtisSerializer(article)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=False)
    def delete(self, request):
        deid = request.data.get('de_id')
        print(deid)
        deid = int(deid)
        article = get_object_or_404(Article, id=deid)
        article.delete()
        result = {
                "code": 200,
                "message": "已经保存",
                "body": ""
            }
        return Response(result)

    @action(methods=['post'], detail=False)
    def xiugai(self,request):
        iid = request.data.get('i_id')
        ttitle =request.data.get('title')
        ccontent = request.data.get('content')
        article = get_object_or_404(Article, id=iid)
        article.title = ttitle
        article.content = ccontent 
        article.save()
        result = {
            "code": 200,
            "msg": "修改成功",
            "body": ""
        }
        return Response(result)



    


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArtisSerializer

class my(viewsets.ViewSet):
    queryset = Article.objects.all()
    serializer_class = ArtisSerializer
    @action(methods=['post'], detail=False)
    def get_queryset(self,request):
        global global_author
        queryset = Article.objects.filter(author=global_author)
        serializer = ArtisSerializer(queryset,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    