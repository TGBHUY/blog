from django.db import models

class Article(models.Model):
    """
    类名：文章
        blog的模型：
        包含参数：
        １．'标题'
        ２．'正文'
        ３．'创建时间'
        ４．'修改时间'
        ５．'文章状态'
        ６．'摘要'
        ７．'浏览量'
        ８．'点赞数'
        ９．'地址'
        １０．标题图片地址
        １１．头像图片地址
    """
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    # 在 status 时说明

    title = models.CharField('标题', max_length=70)
    # 文章标题，CharField 表示对应数据库中表的列是用来存字符串的，'标题'是一个位置参数
    #（verbose_name），主要用于 django 的后台系统，不多做介绍。
    # max_length 表示能存储的字符串的最大长度

    body = models.TextField('正文')
    # 文章正文，TextField 用来存储大文本字符

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 文章创建时间，DateTimeField用于存储时间，设定auto_now_add参数为真，
    # 则在文章被创建时会自动添加创建时间

    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # 文章最后一次编辑时间，auto_now=True表示每次修改文章时自动添加修改的时间

    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    # STATUS_CHOICES，field 的 choices 参数需要的值，choices选项会使
    # 该field在被渲染成form时被渲染为一个select组件，这里我定义了两个状态，
    # 一个是Draft（草稿），一个是Published（已发布），
    # select组件会有两个选项：Draft 和 Published。
    # 但是存储在数据库中的值分别是'd'和'p'，这就是 choices的作用。

    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    # 文章摘要，help_text 在该 field 被渲染成 form 是显示帮助信息

    views = models.PositiveIntegerField('点击量', default=0)
    # 阅览量，PositiveIntegerField存储非负整数

    likes = models.PositiveIntegerField('点赞', default=0)
    # 点赞数

    address = models.CharField('地址', max_length=20)
    #创建的地址

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    # 文章的分类，ForeignKey即数据库中的外键。外键的定义是：
    # 如果数据库中某个表的列的值是另外一个表的主键。外键定义了一个一对多的关系，
    # 这里即一篇文章对应一个分类，而一个分类下可能有多篇
    # on_delete=models.SET_NULL表示删除某个分类（category）后
    # 该分类下所有的Article的外键设为null（空）


    portrait_img = models.ImageField(upload_to='portrait')
    #头像地址

    title_img = models.ImageField(upload_to='title')
    #标题地址


    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.title

    class Meta:
        # Meta 包含一系列选项，这里的 ordering 表示排序，- 号表示逆序。即当从数据库中取出文章时，其是按文章最后一次修改时间逆序排列的。
        ordering = ['-last_modified_time']


class Category(models.Model):
    """
    类名：类别
    另外一个表，存储文章的分类信息
    """
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    """
    类名：评论
    另外一个表，存储对应博客的评论
    """
    name = models.CharField('评论名字',max_length=70)
    created_time = models.DateTimeField('评论创建时间', auto_now_add=True)
    comment_con = models.TextField('评论内容')
    blog_id = models.IntegerField('博客id')

    def __str__(self):
        return self.name

