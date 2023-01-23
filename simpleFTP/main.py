from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("paulthomas", "12345")

portal = Portal(FTPRealm("./public"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()

