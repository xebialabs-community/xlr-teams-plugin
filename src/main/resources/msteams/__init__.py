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
import sys

def postMessage(url, user, icon, proxyUrl, channel, message):
    # Configuration validations
    if url in ["", None]:
        raise Exception('Server configuration url undefined\n')
    if user in ["", None]:
        raise Exception('Server configuration user name undefined\n')
    if channel in ["", None]:
        raise Exception('The task parameter _channel_ is undefined\n')
    if message in ["", None]:
        raise Exception('The task parameter _message_ undefined\n')

    # Call MS Teams Incoming WebHook
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

    printMessage(channel, message)

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

def printMessage(channel, message):
    # Print output
    print 'Teams message to channel %s sent successfully' % channel
    print '```'
    print message
    print '```'
