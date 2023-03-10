from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    image = models.TextField(max_length=500)
    created_datetime = models.DateTimeField(default=timezone.now)
    updated_datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
      return self.content
    def get_user(self):
      return self.user
    class Meta:
      ordering= ["id"]

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_datetime = models.DateTimeField(default=timezone.now)
    updated_datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
      return self.content
    def comment_list(self, post_id, objs):
        comment_post_list = objs.filter(post_id=post_id,).order_by('id')
        comment_list = [
            {
                'id':comment_post.id,
                'user_id':comment_post.user_id,
                'username':comment_post.user.username,
                'post_id':comment_post.post_id,
                'content':comment_post.content,
                'created_datetime':comment_post.created_datetime.strftime("%Y年%m月%d日 %H:%M"),
                'updated_datetime':comment_post.updated_datetime.strftime("%Y年%m月%d日 %H:%M"),
            } for comment_post in comment_post_list
        ]
        return comment_list

    class Meta:
      ordering= ["id"]

class Reaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    reaction_type = models.IntegerField(default=0)
    created_datetime = models.DateTimeField(default=timezone.now)
    updated_datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
      return str(self.post.id)
    def reaction_list(self, post_id, objs):
        reaction_post_list = objs.filter(post_id=post_id,reaction_type=0).order_by('id')
        reaction_list = [
            {
                'id':reaction_post.id,
                'user_id':reaction_post.user_id,
                'post_id':reaction_post.post_id,
                'reaction_type':reaction_post.reaction_type,
                'created_datetime':reaction_post.created_datetime,
                'updated_datetime':reaction_post.updated_datetime,
            } for reaction_post in reaction_post_list
        ]
        return reaction_list
    class Meta:
      ordering= ["id"]