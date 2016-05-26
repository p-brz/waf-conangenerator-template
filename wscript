#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

def options(opt):
    #Load options from waf tools (c++ compiler)
    # Execute ./waf --help to see current options
    opt.load('compiler_cxx')

def configure(conf):
    #Load waf tools (c++ compiler), see waf docs for others
    conf.load('compiler_cxx')

    # Load references to conan dependencies.
    # This file (conanbuildinfo_waf.py) will be generated
    # on
    conf.load('conanbuildinfo_waf', tooldir=".");

def build(bld):
    # Change this list 'conan_deps' to add the dependencies included on conanfile
    # Use the name of the conan package.
    #   Ex.: for the package 'Poco/1.7.1@lasote/stable', you should use:
    #        conan_deps = ['Poco']
    # Note that this list will be used as 'use' argument below.
    # Check Waf book (https://waf.io/book/#_library_interaction_use) for
    # detailed documentation.
    conan_deps = []

    #Compile an executable from cpp files on source dir
    srcdir = 'src'
    bld.program(
        target   = 'program',
        source   = glob(bld, path.join('src', '**', '*.cpp')),
        includes = [srcdir],
        use      = conan_deps)

def glob(bld, *k, **kw):
    '''Helper to execute an ant_glob search.
        See documentation at: https://waf.io/apidocs/Node.html?#waflib.Node.Node.ant_glob
    '''

    return bld.path.ant_glob(*k, **kw)
