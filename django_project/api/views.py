from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Post
from api.models import Reaction
from api.models import Comment
from django.contrib.auth.models import User
from django.utils import timezone
class PostList(APIView):
    def get(self, request, *args, **kwargs):
        user_id = self.request.query_params.get('user_id')
        if user_id is None:
            user_post_list = Post.objects.all().order_by('-id')
        else:
            user_post_list = Post.objects.filter(user_id=user_id).order_by('-id')
        post_list = []
        for user_post in user_post_list:
            comment_list = Comment.comment_list(Comment, user_post.id, Comment.objects)
            reaction_list = Reaction.reaction_list(Reaction, user_post.id, Reaction.objects)
            post_list.append({
                'id':user_post.id,
                'user_id':user_post.user_id,
                'username':Post.get_user(user_post).username,
                'content':user_post.content,
                'image':user_post.image,
                'created_datetime':user_post.created_datetime.strftime("%Y年%m月%d日 %H:%M"),
                'updated_datetime':user_post.updated_datetime.strftime("%Y年%m月%d日 %H:%M"),
                'comment_list': comment_list,
                'reaction_list': reaction_list,
                'new_comment': {}
            })
        user_list_all = User.objects.all().order_by('-id')
        user_list =[]
        for user in user_list_all:
            user_list.append({
                    'id':user.id,
                    'username':user.username,
                })
        rt = {'post_list': post_list, 'user_list': user_list}
        return JsonResponse(rt)
    def post(self, request, *args, **kwargs):
        #user_id = request.POST.get('user_id')
        #content = request.POST.get('content')
        user_id = self.request.data['user_id']
        content = self.request.data['content']
        created = Post.objects.create(content=content, user_id=user_id)
        rt = {'id': created.id}
        return JsonResponse(rt)

class CommentList(APIView):
    def get(self, request, *args, **kwargs):
        post_id = self.request.query_params.get('post_id')
        comment_list = Comment.comment_list(Comment, post_id, Comment.objects)
        rt = {'comment_list': comment_list}
        return JsonResponse(rt)

    def post(self, request, *args, **kwargs):
        user_id = self.request.data['user_id']
        post_id = self.request.data['post_id']
        content = self.request.data['content']
        created = Comment.objects.create(post_id=post_id, content=content, user_id=user_id)
        rt = {'id': created.id}
        return JsonResponse(rt)

class ReactionList(APIView):
    def get(self, request, *args, **kwargs):
        post_id = self.request.query_params.get('post_id')
        reaction_list = Reaction.reaction_list(Reaction, post_id, Reaction.objects)
        rt = {'reaction_list': reaction_list}
        return JsonResponse(rt)

    def put(self, request, *args, **kwargs):
        user_id = self.request.data['user_id']
        post_id = self.request.data['post_id']
        reaction_type = self.request.data['reaction_type']
        obj, created = Reaction.objects.update_or_create(post_id=post_id, user_id=user_id, defaults={
            'reaction_type': reaction_type
        })
        rt = {'id': obj.id}
        return JsonResponse(rt)