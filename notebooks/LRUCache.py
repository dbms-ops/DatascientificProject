import time
from collections import OrderedDict


class LRUCacheDict(object):

    def __init__(self, max_size=1024, expiration=60):
        self.max_size = max_size
        self.expiration = expiration

        self._cache = {}
        self._access_records = OrderedDict()  # 记录访问时间
        self._expire_records = OrderedDict()  # 记录失效时间

    def __setitem__(self, key, value):
        now = int(time.time())
        self.__delete__(key)
        self._cache[key] = value
        self._access_records[key] = now
        self._expire_records[key] = now + (self.expiration)

        self.cleanup()

    def __getitem__(self, key):
        now = int(time.time())
        del self._access_records[key]
        self._access_records[key] = now

        self.cleanup()

        return self._access_records[key]

    def __delete__(self, key):
        if key in self._cache:
            del self._access_records[key]
            del self._expire_records[key]
            del self._cache[key]

    def __contains__(self, key):
        self.cleanup()
        return key in self._cache

    def cleanup(self):
        """
        Remove 过期的 key
        :return:
        """
        now = int(time.time())
        if self._access_records is None:
            return None

        pending_delete_key = []
        for k, v in self._access_records.items():
            if now - v > self.expiration:
                pending_delete_key.append(k)

        for del_k in pending_delete_key:
            self.__delete__(del_k)

        while (len(self._cache) > self.max_size):
            for k in self._access_records:
                self.__delete__(k)
                break


if __name__ == '__main__':
    cache = LRUCacheDict(max_size=2, expiration=20)
    cache['a'] = 'bar'
    cache['b'] = 'ss'
    cache['c'] = 'ss'
    cache['d'] = 'ss'

    print('a' in cache)
    print('b' in cache)
    print('c' in cache)
    print('d' in cache)

    print(cache)