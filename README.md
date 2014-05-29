bencoder
========
[![Build Status](https://travis-ci.org/utdemir/bencoder.svg?branch=master)](https://travis-ci.org/utdemir/bencoder)

A simple up-to-date bencode decoder-encoder library on Python.

I wrote this simple implementation because of the lack of bencoding libraries compatible with Python 3.

*Bencode (pronounced like B encode) is the encoding used by the peer-to-peer file sharing system BitTorrent for storing and transmitting loosely structured data.*

Usage
-----

    >>> import bencoder
    >>> help(bencoder.decode)

    >>> print(bencoder.decode.__doc__)

        Decodes given bencoded bytes object.
    
        >>> decode(b'i-42e')
        -42
        >>> decode(b'4:utku') == b'utku'
        True
        >>> decode(b'li1eli2eli3eeee')
        [1, [2, [3]]]
        >>> decode(b'd3:bar4:spam3:fooi42ee') == {b'bar': b'spam', b'foo': 42}
        True
        
    >>> print(bencoder.encode.__doc__)

        bencodes given object. Given object should be a int,
        bytes, list or dict.

        >>> [encode(i) for i in (-2, 42, b"answer", b"")]             
                   == [b'i-2e', b'i42e', b'6:answer', b'0:']
        True
        >>> encode([b'a', 42, [13, 14]]) == b'l1:ai42eli13ei14eee'
        True
        >>> encode({b'bar': b'spam', b'foo': 42, b'mess': [1, b'c']}) i
                   == b'd3:bar4:spam3:fooi42e4:messli1e1:cee'
        True

