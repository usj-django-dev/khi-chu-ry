#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind



#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind
#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbindv#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbind#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

base = 'dc = localhost,dc = localdomain'
# scope = LDAP::LDAP_SCOPE_SUBTREE
filter = '(objectclass = person)'
attrs = ['sn', 'cn']
# 
# conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
begin
   # conn.search(base, scope, filter, attrs) { |entry|
      # print distinguished name
      p entry.dn
      # print all attribute names
      p entry.attrs
      # print values of attribute 'sn'
      p entry.vals('sn')
      # print entry as Hash
      p entry.to_hash
   }
rescue LDAP::ResultError
   conn.perror("search")
   exit
end
conn.perror("search")
conn.unbindv