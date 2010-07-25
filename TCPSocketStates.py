# sd-tcpsocketstates - TCP Socket Status Graph for Server Density
# ---------------------------------------------------------------
# (c) 2010 Chris Boulton <chris.boulton@interspire.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import csv
import re

class TCPSocketStates:
	def __init__(self, agentConfig, checksLogger):
		self.agentConfig = agentConfig
		self.checksLogger = checksLogger
		self.statMatch = re.compile("0[0-9A-B]")
		self.stateTable = {
			'O1': 'established',
			'02': 'syn_sent',
			'03': 'syn_recv',
			'04': 'fin_wait1',
			'05': 'fin_wait2',
			'06': 'time_wait',
			'07': 'close',
			'08': 'close_wait',
			'09': 'last_ack',
			'0A': 'listen',
			'0B': 'closing'
		}

	def run(self):
		fp = open('/proc/net/tcp')
		tcpStats = csv.reader(fp, delimiter=' ', skipinitialspace=True)
		data = {}
		for state in self.stateTable.values():
			data[state] = 0

		for row in tcpStats:
			if self.statMatch.match(row[3]) and row[3] in self.stateTable:
				data[self.stateTable[row[3]]] += 1

		fp.close()
		return data
