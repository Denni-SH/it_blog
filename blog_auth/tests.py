from django.test import TestCase
from .forms import UserCreation
from .models import Category, Post, CustomUser

class BlogTest(TestCase):

    def create_category(self):
        name_category = 'python'
        return Category.objects.create(title=name_category)

    def create_post(self):
        n_category = self.create_category()
        n_title = 'title-qwerty'
        n_text = 'some text'
        return Post.objects.create(title=n_title, text=n_text, category=n_category)

    def test_post_create(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)
        self.assertEqual(post.title, 'title-qwerty')
        self.assertEqual(post.text, 'some text')
        self.assertEqual(post.likes, 0)

    def test_add_like(self):
        post = self.create_post()
        post.likes += 1
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.likes, 1)

    def create_form(self):
        username12 = 'admin'
        password12 = 'Zaqxsw123'
        return CustomUser.objects.create(username=username12,password = password12)

    def test_false_user_create(self):
        c_user = self.create_form()
        data = {'username': c_user.username, 'password1': c_user.password,'password2': c_user.password}
        form = UserCreation(data=data)
        self.assertFalse(form.is_valid())
