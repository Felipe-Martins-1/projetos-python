from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask import url_for, redirect, flash
from flask_login import current_user
from ..blueprints.database import User, Post, db


def init_app(app):
    admin = Admin(
        app, index_view=MyAdminIndexView(), name="Blog", template_mode="bootstrap3"
    )
    admin.add_view(UserView(User, db.session))
    admin.add_view(PostView(Post, db.session))
    admin.add_link(MenuLink(name="Ínicio", url="/", category="Links"))
    admin.add_link(
        MenuLink(name="Minhas Postagens", url="/minhas-postagens", category="Links")
    )
    admin.add_link(MenuLink(name="Sair", url="/sair", category="Links"))


class UserView(ModelView):
    page_size = 50
    can_create = False
    can_edit = True
    column_searchable_list = ["name", "name_user"]
    column_exclude_list = ["password"]
    form_excluded_columns = ["password"]
    column_editable_list = ["name", "name_user", "admin"]


class PostView(ModelView):
    page_size = 50
    can_create = False
    can_edit = True
    column_searchable_list = ["title", "created_date_time", "updated_date_time"]
    column_editable_list = ["title", "created_date_time", "updated_date_time"]


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.admin

    def inaccessible_callback(self, name, **kwargs):
        flash("Acesso negado!")
        return redirect(url_for("authentication.login"))
