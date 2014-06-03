python-appassure
================

A Python wrapper for the [AppAssure 5](http://www.appassure.com/) [REST
API](http://docs.appassure.com/display/AA50D/AppAssure+5+API+Reference).

[![Build Status](https://travis-ci.org/george2/python-appassure.svg?branch=development)](https://travis-ci.org/george2/python-appassure)
[![Coverage Status](https://coveralls.io/repos/george2/python-appassure/badge.png?branch=development)](https://coveralls.io/r/george2/python-appassure?branch=development)

## AppAssure

### Features

> Backup, replication and disaster recovery in a single solution
>
> *  Restore your entire server and retrieve all of your data in seconds
> *  Protect your workloads on VMs, physical servers and in the cloud
> *  Restore to dissimilar systems, physical or virtual
> *  Recover Microsoft® Exchange, SQL Server® and SharePoint® applications
> *  Ensure built-in disaster recovery with hot standby VMs

 -- *[Dell.com](http://software.dell.com/products/appassure/)*

### AppAssure and Dell

> First acquired by Dell in 2012, AppAssure is now a part of Dell
> Software. Dell AppAssure products (including the DL and DR family of
> backup appliances) are already a key part of the Dell's award-wining
> data protection portfolio which includes NetVault Backup and vRanger.
> With Dell data protection software and appliances, you can match your
> backup needs to your business and build the most efficient and
> effective solution for your business.

 -- *[Dell.com](http://software.dell.com/acquisitions/appassure.aspx)*

## Installation

    git clone https://github.com/george2/python-appassure.git
    cd python-appassure
    python setup.py install

## Usage

This library is well documented using Python docstrings, so if at any
point you get lost, try reading the documentation using Python's
built-in `help()` function, or simply browsing the source code.

The usual method of using the library is:

1. Import the required modules and classes
2. Set up a session object.
3. Pass the session into a new API interface.
4. Use the interface.

Because the API uses a non-standard time format, a few time-related
methods are included in the `appassure.api.AppAssureAPI` class that
might come in handy.

### Examples

Here's a simple example using the
[ILocalMountManagement](http://docs.appassure.com/display/AA50D/ILocalMountManagement)
Core interface.

```python
# Import the interface(s) you want to work with, and the session
# manager.
from appassure.core.ILocalMountManagement import ILocalMountManagement
from appassure.session import AppAssureSession

# Set up a session. The same session can be used for multiple
# interfaces.
session = AppAssureSession('myappassure5coreserver', 8006, 'Username',
        'password')

# Pass the session to the interface(s) on creation.
mounts = ILocalMountManagement(session)

# Call methods from the interface. Response data can be accessed
# with object or dictionary syntax.
mounts.getMounts().mountInfo
mounts.getMounts()['mountInfo']
```

Some methods take simple parameters.

```python
mounts.dismount('my_named_mount')
```

Others must be passed in either valid XML data, or a dictionary
object that will be converted to XML by the the library. Here's an
example using raw XML.

```python
mountData = """
  <agentIds>
    <agentId>1627aea5-8e0a-4371-9022-9b504344e724</agentId>
    <agentId>1627aea5-8e0a-4371-9022-9b504344e724</agentId>
  </agentIds>
  <force>true</force>
  <isNightlyJob>true</isNightlyJob>
  <jobId>1627aea5-8e0a-4371-9022-9b504344e724</jobId>
  <jobStartsCount>4294967295</jobStartsCount>
  <nightlyJobTransactionId>1627aea5-8e0a-4371-9022-9b504344e724</nightlyJobTransactionId>
  <mountPoint>String content</mountPoint>
  <recoveryPoint>String content</recoveryPoint>
  <shareAllowedGroup>String content</shareAllowedGroup>
  <shareName>String content</shareName>
  <type>None</type>
  <volumeImagesToMount>
    <string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">String content</string>
    <string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">String content</string>
  </volumeImagesToMount>
"""
mounts.startMount(mountData)
```

Some API methods require data to be in a certain order- in these
cases, Python's `collections.OrderedDict` must be used instead of
the built-in `dict` type. Another example identical to the one above,
but using an `OrderedDict` object:

```python
from collections import OrderedDict

mountData = OrderedDict([
    ('agentIds', {
        'agentId': [
            '1627aea5-8e0a-4371-9022-9b504344e724',
            '1627aea5-8e0a-4371-9022-9b504344e724',
        ],
    }),
    ('isNightlyJob', 'true'),
    ('jobId', '1627aea5-8e0a-4371-9022-9b504344e724'),
    ('mountPoint', 'String content'),
    ('recoveryPoint', 'String content'),
    ('shareAllowedGroup', 'String content'),
    ('shareName', 'String content'),
    ('type', 'None'),
    ('volumeImagesToMount', {
        'string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"': [
            'String content', 'String content'
        ],
    }),
])
mounts.startMount(mountData)
```

You might find that you need to pass in or read timestamps from the API.
Using the methods built in to the time module of this library can help
make that easier. The `formatTime(time)`, `deformatTime(string)`, and
`reformatTime(string)` methods all use Python's `datetime` module to
make dealing with timestamps in the format expected by the AppAssure API
easier. Note that all timestamps sent to or recieved from the AppAssure
API should be UTC.

```python
import datetime
from appassure import time

time.formatTime(datetime.datetime.utcnow())
```

## Contributing

AppAssure has quite a few of what it calls
[interfaces](http://docs.appassure.com/display/AA50D/Core+API+Reference)
available, all of which have been implemented (but not fully tested) at
this time. Most of these were semi-automatically generated by the bash
script in the [tools](tools) folder that will pull from the AppAssure
documentation and automate most of the implementation process. (You do,
however, still need to enter the wrapper XML tag for the XML request
body, if that exists.)

![xml tag](http://i.imgur.com/HNsxslV.png)

If there is no XML request body for a method, just press enter. You will
not be prompted for request bodies for methods that use the `GET` or
`DELETE` HTTP verbs.

Pull requests and issues are welcomed; if you find a bug, please report
it!
