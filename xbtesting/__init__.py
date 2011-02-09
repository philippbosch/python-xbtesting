from .xbtesting import XBTesting, XBTest, XBTestVersion, XBTestVersionResult

VERSION = ('0', '1', '2')

__version__ = ".".join(VERSION)
__all__ = ['XBTesting', 'XBTest', 'XBTestVersion', 'XBTestVersionResult']
