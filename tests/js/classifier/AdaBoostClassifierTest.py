# -*- coding: utf-8 -*-

import unittest

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn_porter import Porter

from ..JavaScriptTest import JavaScriptTest


class AdaBoostClassifierTest(JavaScriptTest, unittest.TestCase):

    def setUp(self):
        super(AdaBoostClassifierTest, self).setUp()
        base_estimator = DecisionTreeClassifier(max_depth=4, random_state=0)
        mdl = AdaBoostClassifier(
            base_estimator=base_estimator, n_estimators=100, random_state=0)
        self._port_model(mdl)

    def tearDown(self):
        super(AdaBoostClassifierTest, self).tearDown()
