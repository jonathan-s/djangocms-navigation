from django.utils.translation import ugettext_lazy as _

from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, PlaceholderToolbar
from cms.toolbar_pool import toolbar_pool
from .utils import get_model, reverse_admin_name

MenuContent = get_model('MENU_MODEL')


class NavigationToolbar(PlaceholderToolbar):
    def _add_navigation_menu(self):
        app_label = MenuContent._meta.app_label
        model_name = MenuContent._meta.model_name

        change_permission = '{}.change_{}'.format(app_label, model_name)
        if not self.request.user.has_perm(change_permission):
            return
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER)
        url = reverse_admin_name(MenuContent, 'changelist')
        admin_menu.add_sideframe_item(_("Navigation"), url=url, position=4)

    def post_template_populate(self):
        self._add_navigation_menu()


toolbar_pool.register(NavigationToolbar)
