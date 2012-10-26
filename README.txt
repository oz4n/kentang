kentang, Simple Network Monitoring application
(c) Noprianto <nop@tedut.com>
2010 
GPL


SCREENSHOTS: https://github.com/nopri/kentang/wiki


FEATURES:
- protocols: http, https, ftp, smtp, imap4, imap4ssl, pop3, pop3ssl
- multi threaded
- multi platform
- command line interface
- simple event handler (ok/fail)
- simple configuration file (INI file)


REQUIREMENTS:
- python


CONFIGURATION:
- Single .ini file
- Configuration section
  [<host>[,optional tag]]
  protocol = <supported protocol>
  port = [optional, port]
  ok = [optional, execute this command if ok]
  fail = [optional, execute this command if fails]
- Arguments passed to event handler:
  - time
  - hostname
  - port


EXAMPLES:
- examples directory
- *.ini: config
- *.py: handler


RUN:
- python kentang.py <config_file>
- python kentang.py examples/1.ini


THANK YOU :)
