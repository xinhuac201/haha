import xadmin
from xadmin import views
from . import models
from user.adminx import GlobalSettings

# class GlobalSettings(object):
#     """xadmin的全局配置"""
#     site_title = "路飞学城"  # 设置站点标题
#     site_footer = "路飞学城有限公司"  # 设置站点的页脚
#     menu_style = "accordion"  # 设置菜单折叠


# xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(models.Banner, GlobalSettings)
xadmin.site.register(models.Category, GlobalSettings)
xadmin.site.register(models.Area, GlobalSettings)
xadmin.site.register(models.Country, GlobalSettings)
xadmin.site.register(models.Holiday, GlobalSettings)
xadmin.site.register(models.Overview, GlobalSettings)
xadmin.site.register(models.Route, GlobalSettings)
xadmin.site.register(models.FocusTag, GlobalSettings)
