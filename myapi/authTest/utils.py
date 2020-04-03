# #!D:/workplace/python
# # -*- coding: utf-8 -*-
# # @File  : utils.py
# # @Author: WangJun
# # @Date  : 2020/3/3
#
# from authTest.models import App
# from django.contrib.auth.backends import ModelBackend
#
#
# class MyAuthenticationBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if username is None:
#             username = kwargs.get(App.USERNAME_FIELD)
#         try:
#             user = App.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#             else:
#                 return None
#
#         except Exception as e:
#             return None
#
#
# # class MyAuthenticationBackend(ModelBackend):
# #     """根据username查找 user对象, 在使用user对象的check_password对比密码是否正确"""
# #     def authenticate(self, request, username=None, password=None, **kwargs):
# #         if username is None:
# #             username = kwargs.get(App.USERNAME_FIELD)
# #         try:
# #             user = App.get_by_natural_key(username=username)
# #
# #         except App.DoesNotExist:
# #             # Run the default password hasher once to reduce the timing
# #             # difference between an existing and a nonexistent user (#20760).
# #             App().set_password(password)
# #         else:
# #             if user.check_password(password) and self.user_can_authenticate(user):
# #                 return user
