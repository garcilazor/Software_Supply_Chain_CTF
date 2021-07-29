#
`mysoft_log` is a company internal library, to be placed in 
the private package repository. It is a basic logging library that (within
the canon of the level) logs to a proprietary central logging server.
In reality, our library just mocks the actual network traffic with constants.

`userwidget_serv` is a small dummy application that uses the package. 
Within the canon of the level, it is just some simple web server that
uses a logger from `mysoft_log`.

