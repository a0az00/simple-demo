import xadmin
from goods.models import Category, GoodsProfile
from xadmin import views


class GlobalSetting:
    site_title = '后台管理系统'
    site_footer = '史振涛'


class GoodsProfileAdmin:
    list_display = ['name', 'price', 'category', 'add_time']
    search_fields = ['name', 'price', 'add_time']
    list_filter = ['name', 'price', 'category', 'add_time']


class CategoryAdmin:
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


xadmin.site.register(GoodsProfile, GoodsProfileAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
