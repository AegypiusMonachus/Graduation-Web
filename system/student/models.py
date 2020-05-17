# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A(models.Model):
    a_table = models.CharField(primary_key=True, max_length=50)
    a_auth = models.CharField(max_length=5)
    a_target = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'a'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    b_name = models.CharField(max_length=100, blank=True, null=True)
    b_price = models.FloatField(blank=True, null=True)
    b_editor = models.CharField(max_length=200, blank=True, null=True)
    b_publish_agent = models.CharField(max_length=20, blank=True, null=True)
    b_publish_time = models.CharField(max_length=50, blank=True, null=True)
    b_publishno = models.CharField(db_column='b_publishNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b_use_teacher = models.CharField(max_length=50, blank=True, null=True)
    b_award = models.CharField(max_length=200, blank=True, null=True)
    b_amount = models.CharField(max_length=200, blank=True, null=True)
    b_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Class(models.Model):
    class_name = models.CharField(max_length=50, blank=True, null=True)
    class_student_num = models.IntegerField(blank=True, null=True)
    class_chief = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Course(models.Model):
    course_name = models.CharField(max_length=50, blank=True, null=True)
    course_category1 = models.CharField(max_length=20, blank=True, null=True)
    course_category2 = models.CharField(max_length=20, blank=True, null=True)
    course_category3 = models.CharField(max_length=20, blank=True, null=True)
    course_score = models.CharField(blank=True,max_length=50, null=True)
    course_learn_hours = models.CharField(blank=True, max_length=50,null=True)
    course_teach_hours = models.CharField(blank=True, max_length=50,null=True)
    course_lab_hours = models.CharField(blank=True, max_length=50,null=True)
    course_computer_hours = models.CharField(blank=True, max_length=50,null=True)
    course_other_hours = models.CharField(blank=True, max_length=50,null=True)
    course_week_hours = models.CharField(blank=True, max_length=50,null=True)
    course_continue_num = models.CharField(blank=True, max_length=50,null=True)
    course_test_method = models.CharField(max_length=10, blank=True, null=True)
    course_teacher1 = models.CharField(max_length=50, blank=True, null=True)
    course_teacher2 = models.CharField(max_length=50, blank=True, null=True)
    course_teacher3 = models.CharField(max_length=50, blank=True, null=True)
    course_teacher4 = models.CharField(max_length=50, blank=True, null=True)
    course_teach_method = models.CharField(max_length=10, blank=True, null=True)
    course_class = models.CharField(max_length=20, blank=True, null=True)
    course_class_name = models.CharField(max_length=50, blank=True, null=True)
    course_adapt_gender = models.CharField(max_length=5, blank=True, null=True)
    course_class_num = models.CharField(max_length=20, blank=True, null=True)
    course_choose_num = models.CharField(blank=True, max_length=50,null=True)
    course_merge_class_info = models.CharField(max_length=200, blank=True, null=True)
    course_class_group = models.CharField(max_length=20, blank=True, null=True)
    course_lab_weeks = models.CharField(max_length=10, blank=True, null=True)
    course_theory_weeks = models.CharField(max_length=10, blank=True, null=True)
    course_double_or_single_week = models.CharField(max_length=10, blank=True, null=True)
    course_arangable_hours = models.CharField(blank=True, max_length=50,null=True)
    course_confirm = models.CharField(max_length=10, blank=True, null=True)
    course_department = models.CharField(max_length=20, blank=True, null=True)
    course_area = models.CharField(max_length=20, blank=True, null=True)
    course_classroom_type = models.CharField(max_length=20, blank=True, null=True)
    course_building = models.CharField(max_length=20, blank=True, null=True)
    course_classroom = models.CharField(max_length=20, blank=True, null=True)
    course_require_class_num = models.CharField(max_length=20, blank=True, null=True)
    course_require_not_class_num = models.CharField(max_length=20, blank=True, null=True)
    course_remarks = models.TextField(blank=True, max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Message(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Student(models.Model):
    student_no = models.CharField(db_column='student_NO', primary_key=True, max_length=15)  # Field name made lowercase.
    student_name = models.CharField(max_length=20, blank=True, null=True)
    student_gender = models.CharField(max_length=10, blank=True, null=True)
    student_class = models.CharField(max_length=50, blank=True, null=True)
    student_phone_num = models.CharField(max_length=20, blank=True, null=True)
    student_password = models.CharField(max_length=100, blank=True, null=True ,default="123456")

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    teacher_name = models.CharField(max_length=20, blank=True, null=True)
    teacher_gender = models.CharField(max_length=5, blank=True, null=True)
    teacher_course = models.CharField(max_length=20, blank=True, null=True)
    teacher_phone_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class Usebook(models.Model):
    usebook_course = models.CharField(db_column='useBook_course', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usebook_course_type = models.CharField(db_column='useBook_course_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_test_method = models.CharField(db_column='useBook_test_method', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_teacher1 = models.CharField(db_column='useBook_teacher1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usebook_teacher2 = models.CharField(db_column='useBook_teacher2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usebook_teacher3 = models.CharField(db_column='useBook_teacher3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usebook_teacher4 = models.CharField(db_column='useBook_teacher4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usebook_teach_method = models.CharField(db_column='useBook_teach_method', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_class = models.CharField(db_column='useBook_class', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_class_name = models.CharField(db_column='useBook_class_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_adapt_gender = models.CharField(db_column='useBook_adapt_gender', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usebook_class_num = models.CharField(db_column='useBook_class_num', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usebook_choose_num = models.CharField(db_column='useBook_choose_num', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usebook_merge_class_info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usebook'

# 教材的购物车
class Bookscart(models.Model):
    # 学生id  教材isbn
    stu_no = models.CharField(max_length=30)
    isbn = models.ForeignKey(to='Book',to_field="id",on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table='bookscart'

# 教材订购记录变化表
class Bookscartchange(models.Model):
    # 学生id  教材isbn
    stu_no = models.CharField(max_length=30)
    b_isbn = models.ForeignKey(to='Book',to_field="id",on_delete=models.CASCADE)
    b_name = models.CharField(max_length=100)
    b_price = models.FloatField()
    time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table='bookscartchange'

# 学生教材订单表
class Booksorder(models.Model):
    # 学生id  教材isbn
    stu_no = models.CharField(max_length=30)
    b_isbn = models.CharField(max_length=50)
    b_name = models.CharField(max_length=100)
    b_price = models.FloatField()
    b_time = models.DateTimeField(blank=True, null=True)
    # 教材状态：0 (在规定时间内)可以变更 ， 1或者其他数字 已经确定订购，不可变更
    status = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table='booksorder'