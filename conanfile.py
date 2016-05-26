#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os

class MyConanFile(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    #Conan dependencies
    requires = (

        "WafGenerator/0.0.1@paulobrizolara/experimental"
    )

    generators = "Waf"

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

    def build(self):
        #Change to wscript dir
        os.chdir(self.conanfile_directory)
        waf = os.path.join(self.conanfile_directory, 'waf')
        self.run('%s configure build' % waf)
