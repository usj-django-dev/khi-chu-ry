#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
# $PORT =    LDAP::LDAP_PORT
# $SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind



#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind




#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind
#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind
#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind













#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
# $PORT =    LDAP::LDAP_PORT
# $SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind



#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind




#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind
#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind

#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind
#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind


#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind



#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind







#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind









#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind








#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind












#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind







#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind









#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind








#/usr/bin/ruby -w

require 'ldap'

$HOST =    'localhost'
$PORT =    LDAP::LDAP_PORT
$SSLPORT = LDAP::LDAPS_PORT

conn = LDAP::Conn.new($HOST, $PORT)
conn.bind('cn = root, dc = localhost, dc = localdomain','secret')

conn.perror("bind")
entry1 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','domain']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'o',['TTSKY.NET']),
   LDAP.mod(LDAP::LDAP_MOD_ADD,'dc',['localhost']),
]

entry2 = [
   LDAP.mod(LDAP::LDAP_MOD_ADD,'objectclass',['top','person']),
   LDAP.mod(LDAP::LDAP_MOD_ADD, 'cn', ['Zara Ali']),
   LDAP.mod(LDAP::LDAP_MOD_ADD | LDAP::LDAP_MOD_BVALUES, 'sn', 
                     ['ttate','ALI', "zero\000zero"]),
]

begin
   conn.add("dc = localhost, dc = localdomain", entry1)
   conn.add("cn = Zara Ali, dc = localhost, dc =  localdomain", entry2)
rescue LDAP::ResultError
   conn.perror("add")
   exit
end
conn.perror("add")
conn.unbind









