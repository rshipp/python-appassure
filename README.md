python-appassure
================

A Python wrapper for the [AppAssure 5](http://www.appassure.com/) [Core
API](http://docs.appassure.com/display/AA50D/Core+API+Reference).

## Installation

    git clone https://github.com/george2/python-appassure.git
    git submodule --init --recursive
    # TODO: Create setup.py for installation

## Usage

    from appassureapi.appassureapi import AppAssureAPI
    from appassureapi.ITemplate import ITemplate
    from appassuresession import AppAssureSession
    s = AppAssureSession('myappassure5coreserver', 8006, 'Username',
            'password')
    a = ITemplate(s)
    a.DoSomethingOnTheServer()

## Implementing New Interfaces
AppAssure has quite a few of what it calls
[interfaces](http://docs.appassure.com/display/AA50D/Core+API+Reference)
available, and I don't feel like implementing all of them. If you want
to add an interface that is not already implemented, it is fairly simple
to do so. In the [appassureapi](appassureapi) folder, there is a bash
script that will pull from the AppAssure documentation and automate most
of the implementation process. You will, however, still need to enter
the wrapper XML tag for the XML request body, if that exists. 

![xml tag](http://i.imgur.com/HNsxslV.png)

If there is no XML request body for a method, just press enter. You will
not be prompted for request bodies for methods that use the `GET` HTTP
verb. 

If you wish to implement an interface manually, that is also possible.
Just take a look at some of the existing interfaces to get an idea of
how to do so.
