# -*- coding: utf-8 -*-

import unittest

from sklearn.svm.classes import LinearSVC
from sklearn_porter import Porter

from ..JavaTest import JavaTest


class LinearSVCTest(JavaTest, unittest.TestCase):

    def setUp(self):
        super(LinearSVCTest, self).setUp()
        mdl = LinearSVC(C=1., random_state=0)
        self._port_model(mdl)

    def tearDown(self):
        super(LinearSVCTest, self).tearDown()
