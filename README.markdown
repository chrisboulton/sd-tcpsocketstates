sd-tcpsocketstates
==================

Introduction
------------

Plugin for Server Density <http://www.serverdensity.com/> that graphs the
status of TCP sockets (`fin_wait`, `syn_sent` etc) on a Linux system by
reading `/proc/net/tcp`.

![The graph](http://img.skitch.com/20100725-je9kemqkc5e2xsh7ixhr8g8yjs.jpg)

Installation
------------

* Login to your Server Density account, click **Plugins**, then **Add new plugin**
and enter **TCP Socket States** as the name of the plugin. Click **Add**.

* If you haven't already, create a directory to drop Server Density plugins
in on the hosts you monitor. Configure that directory in `/etc/sd-agent/config.cfg`:

		plugin_directory: /directory/here/without/trailing/slash

* Drop TCPSocketStates.py in to the above directory.

* Restart sd-agent.

* Watch for the graph.

License
-------

(c) 2010 Chris Boulton <chris.boulton@interspire.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.