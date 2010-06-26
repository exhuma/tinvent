# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose, require, request, validate
from formencode import validators
#from tg import redirect, flash

# third party imports
#from pylons.i18n import ugettext as _
from repoze.what import predicates, authorize

# project specific imports
from tinvent.lib.base import BaseController
from tinvent.model import DBSession, metadata, Category, Contact, Item


class ItemsController(BaseController):
    # Only allow this to be visible by registered users
    allow_only = authorize.not_anonymous()

    @expose('tinvent.templates.items.index')
    @validate( validators={
       "categories": validators.Set(),
       "status": validators.Int()
       } )
    def index(self, categories=None, status=None ):
        identity = request.environ.get( 'repoze.who.identity' )
        user = identity['user']

        me_contact = Contact.find_by_user( user )

        if not me_contact:
           raise ValueError( "Unable to retrieve user-to-contact mapping. For some reason the contact mapping the current user to a contact_id has vanished." )

        return dict( page='index', user=user,
              me_contact = me_contact,
              categories=DBSession.query(Category) )


    @expose('tinvent.templates.items.view')
    def view(self, item_id):
        identity = request.environ.get( 'repoze.who.identity' )
        user = identity['user']
        me_contact = Contact.find_by_user( user )
        item = DBSession.query(Item)\
              .filter_by( item_id=item_id )\
              .first()
        if not item:
           raise ValueError( "Item not found!" )
        if item.holder_id != me_contact.contact_id and item.owner_id != me_contact.contact_id:
           raise ValueError( "You neither own nor hold this item! Access Denied!" )

        return dict( item=item )


