#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import msteams

targetTask = taskApi.searchTasksByTitle(
    taskTitle,
    phaseTitle,
    releaseId
)
if len(targetTask) < 1:
    raise Exception("No tasks meet the specified release, phase, and task specification")
if len(targetTask) > 1:
    raise Exception("Multiple tasks meet the specified release, phase, and task specification - disambiguate with unique task and phase titles")
targetTask = targetTask[0]

if started == False and str(targetTask.status) not in ["PLANNED, PENDING"]:
    url = server['url']
    user = server['userName']
    icon = server['userIcon']
    proxyUrl = server['proxyUrl']
    releaseUrl = releaseApi.getRelease(releaseId).url
    message = "Initial Notification for Digital.ai Release Task: {}\n\n".format(targetTask.title)
    if status:
        message += "Status: {}\n\n".format(targetTask.status)
    if owner:
        message += "Owner: {}\n\n".format(targetTask.owner)
    if team:
        message += "Team: {}\n\n".format(targetTask.team)
    if releaseLink:
        message += "[Release Link]({})\n\n".format(releaseUrl)
    if taskLink:
        message += "[Task Link]({})\n\n".format(targetTask.url)
    msteams.postMessage(url, user, icon, proxyUrl, channel, message)
    started = True

if str(targetTask.status) not in ["COMPLETED", "COMPLETED_IN_ADVANCE", "SKIPPED", "SKIPPED_IN_ADVANCE", "FAILED", "ABORTED"]:
    task.setStatusLine('Task: {}...'.format(str(targetTask.status).replace("_", " ").title()))
    task.schedule('msteams/NotificationTaskStatus.py', pollFrequency)
else:
    task.setStatusLine('Task: {}'.format(str(targetTask.status).replace("_", " ").title()))
    url = server['url']
    user = server['userName']
    icon = server['userIcon']
    proxyUrl = server['proxyUrl']
    releaseUrl = releaseApi.getRelease(releaseId).url
    message = "Final Notification for Digital.ai Release Task: {}\n\n".format(targetTask.title)
    if status:
        message += "Status: {}\n\n".format(targetTask.status)
    if owner:
        message += "Owner: {}\n\n".format(targetTask.owner)
    if team:
        message += "Team: {}\n\n".format(targetTask.team)
    if releaseLink:
        message += "[Release Link]({})\n\n".format(releaseUrl)
    if taskLink:
        message += "[Task Link]({})\n\n".format(targetTask.url)
    msteams.postMessage(url, user, icon, proxyUrl, channel, message)
