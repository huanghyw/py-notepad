from contextlib import contextmanager


class Connection:
    def conn(self):
        print("conn")
        return "conn"

    def close(self):
        print("close")

    def commit(self):
        print("commit")

    def rollback(self):
        print("rollback")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
        return True

    def __enter__(self):
        return self.conn()


@contextmanager
def conn():
    try:
        print("conn")
        yield "conn"
        print("commit")
    except Exception:
        print("rollback")
    finally:
        print("close")


connection = Connet = Connection


if __name__ == "__main__":
    """
    模拟数据库操作场景，代码执行成功，则提交事务，否则回滚事务。
    不管执行是否成功，最后关闭连接。
    """

    # 传统方式，自己维护上下文
    c = Connection()
    try:
        print("GET:", c.conn())
        raise Exception
        c.commit()
    except Exception:
        c.rollback()
    finally:
        c.close()
    print("=" * 60)

    # 定义Class进入和退出时的动作
    with connection() as c:
        print("GET:", c)
        raise Exception
    print("=" * 60)

    # 使用contextlib包中封装好的@contextmanager进行上下文管理
    with conn() as c:
        print("GET:", c)
        raise Exception
