import unittest
from unittest.mock import MagicMock
from task import AppModel, AppControl

class TestMo(unittest.TestCase):
    
    def setUp(self):
        self.view = MagicMock()
        self.view.resultString = {}
        self.model = AppModel(self.view)
        self.control = AppControl(self.model)

    def set_coefficients(self, a, b, c):
        self.view.aString.get = MagicMock(return_value=a)
        self.view.bString.get = MagicMock(return_value=b)
        self.view.cString.get = MagicMock(return_value=c)
        
    def test_0_init(self):
        assert self.model.view is self.view
        assert self.control.model is self.model

    def test_1_call(self):
        self.model(self.control)
        self.view.assert_called_once_with(self.control)
        self.assertEqual(self.view.resultString['text'], "Enter all coefficients")

    def test_2_onlySomeCoefInit(self):
        self.model(self.control)
        self.view.aString.get = MagicMock(return_value=3)
        self.view.bString.get = MagicMock(return_value='')
        self.view.cString.get = MagicMock(return_value='')
        self.control.calculate()
        self.assertEqual(self.view.resultString['text'], "Enter all coefficients")

    def test_3_twoRoot(self):
        self.model(self.control)
        self.set_coefficients(1, -3, -4)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], (-1.0, 4.0))
        
        self.set_coefficients(1, 2, -3)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], (-3.0, 1.0))

    def test_4_oneRoot(self):
        self.model(self.control)
        self.set_coefficients(1, -6, 9)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], 3.0)
        self.model(self.control)
        
        self.set_coefficients(1, 6, 9)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], -3.0)

        self.set_coefficients(0, 6, 9)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], -1.5)


    def test_5_noRoot(self):
        self.model(self.control)
        self.set_coefficients(5, 2, 3)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], '∅')

        self.set_coefficients(0, 0, 3)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], '∅')

    def test_6_infRoot(self):
        self.model(self.control)
        self.set_coefficients(0, 0, 0)
        self.control.calculate()
        self.view.aString.get.assert_called_once()
        self.view.bString.get.assert_called_once()
        self.view.cString.get.assert_called_once()        
        self.assertEqual(self.view.resultString['text'], '∞')

    def test_7_wrongInput(self):
        self.model(self.control)
        self.set_coefficients("abc", "number", "five")
        self.control.calculate()
        self.assertEqual(self.view.resultString['text'], "could not convert string to float: 'abc'")

        self.set_coefficients("7", "number", "five")
        self.control.calculate()
        self.assertEqual(self.view.resultString['text'], "could not convert string to float: 'number'")

        self.set_coefficients("5", "6", "7five")
        self.control.calculate()
        self.assertEqual(self.view.resultString['text'], "could not convert string to float: '7five'")

