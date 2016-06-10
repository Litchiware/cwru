import unittest
from cwru import CWRU


class TestCWRUData(unittest.TestCase):

    def setUp(self):
        self.data = CWRU("12DriveEndFault", '1797', 384)

    def test_x(self):
        s = self.data.X_train.shape
        self.assertEqual(len(s), 2, 'incorrect X_train format')
        self.assertTrue(s[0] > 0, 'at least 1 training sample is expected')
        self.assertEqual(s[1], 384, 'incorrect X_train sequence length')

        s = self.data.X_test.shape
        self.assertEqual(len(s), 2, 'incorrect X_test format')
        self.assertTrue(s[0] > 0, 'at least 1 test sample is expected')
        self.assertEqual(s[1], 384, 'incorrect X_test sequence length')

    def test_y(self):
        self.assertTrue(isinstance(self.data.y_train, tuple), 'y_train should be tuple')
        self.assertEqual(set(self.data.y_train), set(range(16)), 'y_train has wrong values')

        self.assertTrue(isinstance(self.data.y_test, tuple), 'y_test should be tuple')
        self.assertEqual(set(self.data.y_test), set(range(16)), 'y_test has wrong values')

        self.assertEqual(self.data.X_train.shape[0], len(self.data.y_train), 'X_train and y_train should have equal lengths')
        self.assertEqual(self.data.X_test.shape[0], len(self.data.y_test), 'X_test and y_test should have equal lengths')

    def test_labels(self):
        labels = {'0.007-Ball',
                  '0.007-InnerRace',
                  '0.007-OuterRace12',
                  '0.007-OuterRace3',
                  '0.007-OuterRace6',
                  '0.014-Ball',
                  '0.014-InnerRace',
                  '0.014-OuterRace6',
                  '0.021-Ball',
                  '0.021-InnerRace',
                  '0.021-OuterRace12',
                  '0.021-OuterRace3',
                  '0.021-OuterRace6',
                  '0.028-Ball',
                  '0.028-InnerRace',
                  'Normal'
                  }
        self.assertEqual(set(self.data.labels), labels, 'incorrect labels')

    def test_length(self):
        self.assertEqual(self.data.length, 384, 'CWRU object has wrong length attribute')

    def test_nclasses(self):
        self.assertEqual(self.data.nclasses, 16, 'CWRU object has wrong nclasses attribute')

if __name__ == '__main__':
    unittest.main()
