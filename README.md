# xbtesting

A Python library to talk to the API provided by [CrossBrowserTesting.com](http://crossbrowsertesting.com/).

Disclaimer: I am in no way associated with CrossBrowserTesting.com, LLC.


## Installation

    $ pip install -e git+http://github.com/philippbosch/xbtesting.git#egg=xbtesting


## Usage

### Setup

    >>> from xbtesting import XBTesting
    >>> XBTesting.username = "your username"
    >>> XBTesting.password = "your password"
    >>> xbt = XBTesting()


### Retrieving tests
    
    >>> tests = xbt.get_tests()
    >>> tests
    [<xbtesting.xbtesting.XBTest object at 0x1011a3850>,
     <xbtesting.xbtesting.XBTest object at 0x1011a39d0>,
     <xbtesting.xbtesting.XBTest object at 0x1011a3a50>,
     <xbtesting.xbtesting.XBTest object at 0x1011a3b50>,
     <xbtesting.xbtesting.XBTest object at 0x1011a3b90>]
    >>> tests[0].id
    98765
    >>> tests[0].url
    'http://your-website.com/'
    >>> tests[0].test_date
    datetime.datetime(2010, 12, 13, 8, 4, 28)

For all available properties consult the [API docs](http://crossbrowsertesting.com/apidocs#129).


### Retrieving versions of a test

    >>> versions = test[0].get_versions()
    >>> versions
    [<xbtesting.xbtesting.XBTestVersion object at 0x1011b8150>,
     <xbtesting.xbtesting.XBTestVersion object at 0x1011b8190>
    ]
    >>> versions[0].id
    876543
    >>> versions[0].version_date
    datetime.datetime(2010, 12, 13, 8, 4, 28)
    
    