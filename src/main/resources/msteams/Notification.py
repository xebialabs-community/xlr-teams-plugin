#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json
import urllib2


def printData(url, data):
    print
    print 'URL:'
    print '```'
    print url
    print '```'
    print 'Data:'
    print '```'
    print data
    print '```'

# Initialize variables & check parameters
response = ''
url = server['url']
user = server['userName']
icon = server['userIcon']
proxyUrl = server['proxyUrl']
if url in ["", None]:
    print 'Server configuration url undefined\n'
    sys.exit(1)
if user in ["", None]:
    print 'Server configuration user name undefined\n'
    sys.exit(1)
if channel in ["", None]:
    print 'The task parameter _channel_ is undefined\n'
    sys.exit(1)
if message in ["", None]:
    print 'The task parameter _message_ undefined\n'
    sys.exit(1)


# Call MSTeams Incoming WebHook
try:
    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')
    postdata = {}
    if icon:
        postdata = {'channel': channel.strip(), 'username': user.strip(), 'icon_emoji': icon.strip(), 'text': message.strip(), 'mrkdwn': True}
    else:
        postdata = {'channel': channel.strip(), 'username': user.strip(), 'text': message.strip(), 'mrkdwn': True}
    data = json.dumps(postdata)

    if proxyUrl:
        proxy = urllib2.ProxyHandler({'http': proxyUrl, 'https': proxyUrl})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

    response = urllib2.urlopen(request, data)
except urllib2.HTTPError as error:
    print 'HTTP %s error!' % error.code
    print 'Reason: %s' % error.read()
    printData(url, data)
    sys.exit(300)
except urllib2.URLError as error:
    print 'Network error!'
    print 'Reason: %s' % error.reason
    printData(url, data)
    sys.exit(400)

# Print output
print 'Teams message to channel %s sent successfully' % channel
print '```'
print message
print '```'
sys.exit(0)
