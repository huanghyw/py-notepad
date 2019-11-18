import unittest


class StringUtils:
    """字符串工具类"""

    def get_len(self, str):
        """
        获取字符串长度
        :param str: 要处理的字符串
        :return: 长度
        """
        return len(str)


class StringUnitTest(unittest.TestCase):
    """字符串工具单元测试"""

    __string_utils = StringUtils()

    @classmethod
    def setUpClass(cls) -> None:
        """进入测试类前执行"""
        print("\nEnter Class:", cls.__name__)

    @classmethod
    def tearDownClass(cls) -> None:
        """离开测试类前执行"""
        print("\nExit Class:", cls.__name__)

    def setUp(self) -> None:
        """进入测试方法前执行"""
        print("\nEnter Method:", self._testMethodName)

    def tearDown(self) -> None:
        """离开测试方法前执行"""
        print("\nExit Method:", self._testMethodName)

    def test_len(self):
        """单元测试类中，以“test”开头的方法为单元测试要执行的方法"""
        self.assertEqual(self.__string_utils.get_len("ABC"), 3, "长度不一致！")

    def test_len_values(self):
        """
        使用with调用subTest方法进行子测试单元的使用
        适用于更细粒度的场景覆盖测试，发生断言后不影响后续单元运行
        """
        for i in range(0, 5):
            with self.subTest(i=i):
                self.assertEqual(self.__string_utils.get_len("ABC"), i, "长度不一致！")

    @unittest.skip("直接跳过")
    def test_skip(self):
        """直接跳过"""
        print("test_skip")

    @unittest.skipIf(1 == 1, "等式成立跳过")
    def test_skip_if(self):
        """条件成立时跳过，条件可以是变量、方法"""
        print("test_skip")

    @unittest.skipUnless(1 == 2, "等式不成立跳过")
    def test_skip_unless(self):
        """条件不成立时跳过"""
        print("test_skip")

    @unittest.expectedFailure
    def test_fail(self):
        """已知单元测试无法通过"""
        self.assertEqual(1, 0, "这个目前是失败的")


if __name__ == '__main__':
    """
    启动单元测试

    注意：
    1、Pycharm开发工具中运行，确认下当前单元测试执行器，默认为pytest，需要修改为unittest
    2、命令行运行，使用“python PythonUnittest.py”
    3、命令行运行，指定unittest模块，使用“python -m unittest PythonUnittest”。如果需要详细输出
    报告，使用“python -m unittest PythonUnittest”
    """
    unittest.main()
