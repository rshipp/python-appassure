python-appassure
================

A Python wrapper for the AppAssure 5 Core API.

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
to do so. Take a look at
[appassureapi/ITemplate.py](appassureapi/ITemplate.py) for an example of
what an interface might look like, and a little documentation to get you
started.


