#!/usr/bin/env python

"""
A simple bencoding implementation in pure Python.

Consult help(encode) and help(decode) for more info.

>>> encode(42) == b'i42e'
True
>>> decode(b'i42e')
42
"""

import re
import string
import itertools as it

def encode(obj):
    """
    bencodes given object. Given object should be a int,
    bytes, list or dict. If a str is given, it'll be
    encoded as ASCII.

    >>> [encode(i) for i in (-2, 42, b"answer", b"")] \
            == [b'i-2e', b'i42e', b'6:answer', b'0:']
    True
    >>> encode([b'a', 42, [13, 14]]) == b'l1:ai42eli13ei14eee'
    True
    >>> encode({b'bar': b'spam', b'foo': 42, b'mess': [1, b'c']}) \
            == b'd3:bar4:spam3:fooi42e4:messli1e1:cee'
    True
    """

    if isinstance(obj, int):
        return b"i" + str(obj).encode() + b"e"
    elif isinstance(obj, bytes):
        return str(len(obj)).encode() + b":" + obj
    elif isinstance(obj, str):
        return encode(obj.encode("ascii"))
    elif isinstance(obj, list):
        return b"l" + b"".join(map(encode, obj)) + b"e"
    elif isinstance(obj, dict):
        if all(isinstance(i, bytes) for i in obj.keys()):
            items = list(obj.items())
            items.sort()
            return b"d" + b"".join(map(encode, it.chain(*items))) + b"e"
        else:
            raise ValueError("dict keys should be bytes")
    raise ValueError("Allowed types: int, bytes, list, dict; not %s", type(obj))

def decode(s):
    """
    Decodes given bencoded bytes object.

    >>> decode(b'i-42e')
    -42
    >>> decode(b'4:utku') == b'utku'
    True
    >>> decode(b'li1eli2eli3eeee')
    [1, [2, [3]]]
    >>> decode(b'd3:bar4:spam3:fooi42ee') == {b'bar': b'spam', b'foo': 42}
    True
    """
    def decode_first(s, i):
        if s.startswith(b"i", i):
            match = re.compile(b"i(-?\\d+)e").match(s, i)
            return int(match.group(1)), match.end()
        elif s.startswith(b"l", i) or s.startswith(b"d", i):
            start = i
            l = []
            i += 1
            while not s.startswith(b"e", i):
                elem, i = decode_first(s, i)
                l.append(elem)
            i += 1
            if s.startswith(b"l", start):
                return l, i
            else:
                return {i: j for i, j in zip(l[::2], l[1::2])}, i
        elif any(s.startswith(d.encode(), i) for d in string.digits):
            m = re.compile(b"(\\d+):").match(s, i)
            length = int(m.group(1))
            i = m.end()
            end = i + length
            return s[i:end], end
        else:
            raise ValueError("Malformed input.")

    if isinstance(s, str):
        s = s.encode("ascii")

    ret, i = decode_first(s, 0)
    if i != len(s):
        raise ValueError("Malformed input.")
    return ret

if __name__ == "__main__":
   import doctest
   doctest.testmod()
