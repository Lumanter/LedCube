from unittest import TestCase

from Compiler.Utils import createCube


class TestUtils(TestCase):
    def test_createCube2by2by2(self):
        expectedCube = [[[False, False], [False, False]], [[False, False], [False, False]]]
        actualResult = createCube(3, 2)
        self.assertListEqual(expectedCube, actualResult)

    def test_createCube3by3by3(self):
        expectedCube = [[[False, False, False], [False, False, False], [False, False, False]],
                        [[False, False, False], [False, False, False], [False, False, False]],
                        [[False, False, False], [False, False, False], [False, False, False]]]
        actualResult = createCube(3, 3)
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

        actualResult = createCube(3, 6)
        self.assertListEqual(expectedCube, actualResult)
