novaclient-auth-secretkey
=========================


This is an authentication plugin for python-novaclient.  It allows
novaclient users to specify an API key+secret key as credentials to
the Keystone authentication service instead of the normal
username+password.

Plugin users can specify the credentials either programmatically as
attributes of the httpclient object, or using environment variables (e.g.
when using the command-line nova client).


Quick Start
-----------
- Set your environment variables in your shell::

    # this plugin uses these values:
    export OS_AUTH_SYSTEM="secretkey
    export OS_ACCESS_KEY_ID="FIBVLEKFOSIFJS68FI8L"
    export OS_SECRET_KEY="Mu8E/fsleibv8f2j7G97pzqKusive8ofieFkeNs1"


    # this is standard python-novaclient stuff.  these values would connect to
    # hpcloud's us west az3:
    export OS_REGION_NAME="az-3.region-a.geo-1"
    export OS_AUTH_URL=https://region-a.geo-1.identity.hpcloudsvc.com:35357/v2.0/
    export OS_TENANT_NAME=myuser@mydomain.com-tenant1


    # you still have to trick python-novaclient into instantiating the objects
    # correctly, but you do *not* have to use your actual username and password
    # here:
    export OS_PASSWORD=useapikey
    export OS_USERNAME=useapikey

- Test it out::

    nova list


Library Usage
-------------
If you're using `python-novaclient
<https://github.com/openstack/python-novaclient>`_ as a library, instead of
letting the library use values from the environment, you probably want to
control what values you pass to the objects you instantiate.  This is how you
would use the API key and secret with a ``novaclient.client.Client`` object::

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

In case both the environment variables *and* the object attributes are
specified, the values from the object attributes take precedence.
