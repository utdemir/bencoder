# bencoder

[![Build Status](https://travis-ci.org/utdemir/bencoder.svg?branch=master)](https://travis-ci.org/utdemir/bencoder)

A simple up-to-date bencode decoder-encoder library on pure Python.

I wrote this simple implementation because of the lack of bencoding libraries compatible with Python 3.

*Bencode (pronounced like B encode) is the encoding used by the peer-to-peer file sharing system BitTorrent for storing and transmitting loosely structured data.*

## Installation

You can install the package directly from PyPI using pip.

    pip install bencoder

Or you can use this source

    git clone git@github.com:utdemir/bencoder.git
    cd bencoder 
    python setup.py install

## Usage

    >>> import bencoder

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
        >>> encode({b'bar': b'spam', b'foo': 42, b'mess': [1, b'c']}) \
                   == b'd3:bar4:spam3:fooi42e4:messli1e1:cee'
        True

### Real Life Scenario

    >>> import bencoder
    >>> f = open("archlinux-2014.05.01-dual.iso.torrent", "rb")
    >>> d = bencoder.decode(f.read())
    >>> del d[b"info"][b"pieces"] # That's a long hash
    >>> from pprint import pprint
    >>> pprint(d)
    {b'announce': b'http://tracker.archlinux.org:6969/announce',
    b'comment': b'Arch Linux 2014.05.01 (www.archlinux.org)',
    b'created by': b'mktorrent 1.0',
    b'creation date': 1398921725,
    b'info': {b'length': 565182464,
            b'name': b'archlinux-2014.05.01-dual.iso',
            b'piece length': 524288},
    b'url-list': [b'http://mirror.aarnet.edu.au/pub/archlinux/iso/2014.05.01/',
                b'http://ftp.iinet.net.au/pub/archlinux/iso/2014.05.01/',
                ....
                b'http://mirror-fpt-telecom.fpt.net/archlinux/iso/2014.05.01/']}

