#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from telefone import Telefone

class TestTelefone(unittest.TestCase):
    def setUp(self):
        self.telefone = Telefone()

    def tearDown(self):
        pass

    def test_classe_telefone_existe(self):
        self.assertTrue(self.telefone)

    def test_entrada_telefone(self):
        self.assertEqual(
            "ABC",
            self.telefone.ler_entrada("ABC")
        )


if __name__ == '__main__':
    unittest.main()