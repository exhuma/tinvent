.. _user:

User
===============================================================================

A user a real-world person of the system (think: login/password). A user has
represents one ore more :ref:`owners <owner>`. A user has automatically one
"owner" assigned: Him/Herself. In addition to this, the user can have access to
other owners. This is typically a :ref:`group`.

User Properties
-------------------------------------------------------------------------------

id
   internal unique ID

name
   A simple string (i.e.: username, login-name, ...)

openid
   A OpenID-Link

sechash
   A security hash (i.e. password hash)
