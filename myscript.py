import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite4.settings")
    import django

    django.setup()

    # 创建三百条数据
    from school import models

    ret = [models.Classes(name="美容美发{}班".format(i), addr='沙河于辛庄{}号'.format(i)) for i in range(300)]

    models.Classes.objects.bulk_create(ret)
