# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose, require, request
#from tg import redirect, validate, flash

# third party imports
#from pylons.i18n import ugettext as _
from repoze.what import predicates

# project specific imports
from tinvent.lib.base import BaseController
from tinvent.model import DBSession, metadata, Category


class ItemsController(BaseController):
    #Uncomment this line if your controller requires an authenticated user
    #allow_only = authorize.not_anonymous()

    @expose('tinvent.templates.items.index')
    @require( predicates.not_anonymous("This page is only accessible by registered users!") )
    def index(self):
        identity = request.environ.get( 'repoze.who.identity' )
        user= identity['user']
        return dict( page='index', user=user, categories=DBSession.query(Category) )
