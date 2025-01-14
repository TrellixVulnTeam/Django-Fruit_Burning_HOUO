import re
from django import forms
from django.contrib.auth import get_user_model




User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={"requeired": "请填写用户名"})
    password = forms.CharField(required=True, error_messages={"requeired": "请填写密码"})



# class PasswordChangeForm(forms.Form):
#
#     password = forms.CharField(
#         required=True,
#         min_length=6,
#         max_length=20,
#         error_messages={
#             "required": u"密码不能为空"
#         })
#
#     confirm_password = forms.CharField(
#         required=True,
#         min_length=6,
#         max_length=20,
#         error_messages={
#             "required": u"确认密码不能为空"
#         })
#
#     def clean(self):
#         cleaned_data = super(PasswordChangeForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password != confirm_password:
#             raise forms.ValidationError("两次密码输入不一致")
#
# #
# # # 重置密码(提交重置密码)
# # class ModifyPwdForm(forms.Form):
# #     password1 = forms.CharField(required=True, min_length=5)
# #     password2 = forms.CharField(required=True, min_length=5)
# #
# #
#
#
#
#
#
# class UserCreateForm(forms.ModelForm):
#     password = forms.CharField(
#         required=True,
#         min_length=3,
#         max_length=20,
#         error_messages={
#             "required": "密码不能为空",
#             "min_length": "密码长度最少3位数",
#         }
#     )
#
#     confirm_password = forms.CharField(
#         required=True,
#         min_length=3,
#         max_length=20,
#         error_messages={
#             "required": "确认密码不能为空",
#             "min_length": "密码长度最少3位数",
#         }
#     )
#
#     class Meta:
#         model = User
#         fields = [
#             'username', 'mobile', 'email',
#             'department', 'post', 'is_active', 'roles', 'password'
#         ]
#
#         error_messages = {
#             "name": {"required": "姓名不能为空"},
#             "username": {"required": "用户名不能为空"},
#             "email": {"required": "邮箱不能为空"},
#             "mobile": {
#                 "required": "手机号码不能为空",
#                 "max_length": "输入有效的手机号码",
#                 "min_length": "输入有效的手机号码"
#             }
#          }
#
#     def clean(self):
#         cleaned_data = super(UserCreateForm, self).clean()
#         username = cleaned_data.get("username")
#         mobile = cleaned_data.get("mobile", "")
#         email = cleaned_data.get("email")
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if User.objects.filter(username=username).count():
#             raise forms.ValidationError('用户名：{}已存在'.format(username))
#
#         if password != confirm_password:
#             raise forms.ValidationError("两次密码输入不一致")
#
#         if User.objects.filter(mobile=mobile).count():
#             raise forms.ValidationError('手机号码：{}已存在'.format(mobile))
#
#         REGEX_MOBILE = "^1[3578]\d{9}$|^147\d{8}$|^176\d{8}$"
#         if not re.match(REGEX_MOBILE, mobile):
#             raise forms.ValidationError("手机号码非法")
#
#         if User.objects.filter(email=email).count():
#             raise forms.ValidationError('邮箱：{}已存在'.format(email))
#
#
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username', 'mobile', 'email',
#             'department', 'post','is_active', 'roles'
#         ]
#
#
# class PasswordChangeForm(forms.Form):
#
#     password = forms.CharField(
#         required=True,
#         min_length=3,
#         max_length=20,
#         error_messages={
#             "required": u"密码不能为空"
#         })
#
#     confirm_password = forms.CharField(
#         required=True,
#         min_length=3,
#         max_length=20,
#         error_messages={
#             "required": u"确认密码不能为空"
#         })
#
#     def clean(self):
#         cleaned_data = super(PasswordChangeForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password != confirm_password:
#             raise forms.ValidationError("两次密码输入不一致")