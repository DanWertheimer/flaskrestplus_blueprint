class LDAPConfig(object):
    LDAP_HOST = ''
    LDAP_BASE_DN = ''
    LDAP_USERNAME = ''
    LDAP_PASSWORD = ''
    LDAP_USER_OBJECT_FILTER = '(&(objectclass=user)(sAMAccountName=%s))'
    LDAP_OBJECTS_DN = 'dn'
    LDAP_OPENLDAP = True
    LDAP_LOGIN_VIEW = 'login'
    LDAP_GROUP_MEMBERS_FIELD = "member"
    LDAP_GROUP_OBJECT_FILTER = "(&(objectclass=group)(cn=%s))"
    LDAP_GROUP_MEMBER_FILTER = "(&(cn=*)(objectclass=group)(member=%s))"
    LDAP_GROUP_MEMBER_FILTER_FIELD = "cn"
    LDAP_USE_TLS = True
