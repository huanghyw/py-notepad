from concurrent.futures import ProcessPoolExecutor

"""
这是一段在VSCode中无法Debug的代码，目前VSCode版本不支持Python多进程项目调试
系统版本：Ubuntu 18.04，64bit
VSCode版本：1.42.1
Python版本：3.7.5
Python插件提供商：Microsoft
Python插件版本：2020.2.64397 (21 February 2020)
"""

def test_method():
    print("test_method")


if __name__ == "__main__":
    with ProcessPoolExecutor(4) as pool:
        for i in range(4):
            pool.submit(test_method)
