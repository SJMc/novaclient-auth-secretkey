#!/usr/bin/env python
# example.py
# ==========
#
# This shows how to authenticate to HP Cloud's REST API with a user's access
# key ID and secret key instead of their username and password.  This could be
# used to authenticate to any OpenStack implementation that also uses
# ``apiAccessKeyCredentials`` in the JSON body of the authentication request.
from novaclient.client import Client


ACCESS_KEY_ID = 'FIBVLEKFOSIFJS68FI8L'
SECRET_KEY = 'Mu8E/fsleibv8f2j7G97pzqKusive8ofieFkeNs1'
TENANT_NAME = 'myuser@mydomain.com-tenant1'
AUTH_URL = 'https://region-a.geo-1.identity.hpcloudsvc.com:35357/v2.0/'
REGION_NAME = 'az-3.region-a.geo-1'

nova = Client('2', 'dummyvalue', 'dummyvalue', TENANT_NAME,
        auth_system='secretkey', auth_url=AUTH_URL, region_name=REGION_NAME)

# the constructor does not accept the plugin values, so the plugin just
# looks for them as attributes of the nova.client object
nova.client.os_access_key_id = ACCESS_KEY_ID
nova.client.os_secret_key = SECRET_KEY

nova.authenticate()

print nova.servers.list()
