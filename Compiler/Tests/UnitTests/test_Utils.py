import sys
sys.path.append("..")

from unittest import TestCase

from Semantic.Utils import createCube


class TestUtils(TestCase):
    def test_createCube2by2by2(self):
        expectedCube = [[[False, False], [False, False]], [[False, False], [False, False]]]
        actualResult = createCube(3, 2, False)
        self.assertListEqual(expectedCube, actualResult)

    def test_createCube3by3by3(self):
        expectedCube = [[[False, False, False], [False, False, False], [False, False, False]],
                        [[False, False, False], [False, False, False], [False, False, False]],
                        [[False, False, False], [False, False, False], [False, False, False]]]
        actualResult = createCube(3, 3, False)
        self.assertListEqual(expectedCube, actualResult)

    def test_createCube6by6by6(self):
        expectedCube = [[[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]],
                        [[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]],
                        [[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]],
                        [[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]],
                        [[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]],
                        [[False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False],
                         [False, False, False, False, False, False], [False, False, False, False, False, False]]]

        actualResult = createCube(3, 6, False)
        self.assertListEqual(expectedCube, actualResult)
