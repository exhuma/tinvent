# -*- coding: utf-8 -*-
"""
Contacts Controller
"""

# turbogears imports
from tg import expose, require, request, validate
from formencode import validators
#from tg import redirect, flash

# third party imports
#from pylons.i18n import ugettext as _
from repoze.what import predicates, authorize

# project specific imports
from tinvent.lib.base import BaseController
from tinvent.model import DBSession, metadata, Contact, Item


class ContactsController(BaseController):

    # Only allow this to be visible by registered users
    allow_only = authorize.not_anonymous()

    @expose('tinvent.templates.contacts.index')
    def index(self):
        identity = request.environ.get( 'repoze.who.identity' )
        user = identity['user']
        return dict( page='index', user=user )

    @expose('tinvent.templates.contacts.view')
    def view(self, contact_id):
        identity = request.environ.get( 'repoze.who.identity' )
        user = identity['user']
        me_contact = Contact.find_by_user(user)

        contact_query = DBSession.query( Contact )
        contact_query = contact_query.filter_by( user_id=user.user_id )
        contact_query = contact_query.filter_by( contact_id=contact_id )
        contact = contact_query.first()

        your_items_query = DBSession.query( Item )
        your_items_query = your_items_query.filter_by( holder_id=contact.contact_id )
        your_items_query = your_items_query.filter_by( owner_id=me_contact.contact_id )

        his_items_query = DBSession.query( Item )
        his_items_query = his_items_query.filter_by( holder_id=me_contact.contact_id )
        his_items_query = his_items_query.filter_by( owner_id=contact.contact_id )

        return dict( page='index', user=user, contact=contact,
              his_items_query=his_items_query,
              your_items_query=your_items_query )

