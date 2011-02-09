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

#### Available attributes of XBText instances

* `id` (int)
* `url` (str)
* `test_date` (datetime)


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

#### Available attributes of XBTestVersion instances

* `id` (int)
* `test` (XBTest)
* `version_date` (datetime)
* `count_successful` (int)
* `count_not_finished` (int)
* `version_public_url` (str)
* `version_ui_url` (str)
* `version_zip` (str)
* `w3c_css_errors` (int)
* `w3c_html_errors` (int)
* `w3c_html_warnings` (int)


### Retrieving results of a version of a test

    >>> results = versions[0].get_results()
    >>> results
    [<xbtesting.xbtesting.XBTestVersionResult object at 0x100750650>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750190>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x1007501d0>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750290>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750310>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750350>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750390>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x1007503d0>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750410>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750450>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x1007504d0>,
     <xbtesting.xbtesting.XBTestVersionResult object at 0x100750510>]
    >>> results[0].id
    7654321
    >>> results[0].finished_date
    datetime.datetime(2011, 1, 18, 8, 34)
    >>> results[0].full_page
    'http://media.crossbrowsertesting.com/users/12345/screenshots/full/z02129bb861061d1a052.png'
    >>> results[0].browser
    'Firefox 3.5'
    >>> results[0].os
    'Mac OSX 10.5.8'
    >>> results[0].resolution
    '1024x768'

#### Available attributes of XBTestVersionResult instances

* `id` (int)
* `testversion` (XBTestVersion)
* `start_date` (datetime)
* `finished_date` (datetime)
* `status` (str)
* `os` (str)
* `browser` (str)
* `resolution` (str)
* `windowed` (str)
* `windowed_thumb` (str)
* `full_page` (str)
* `full_page_thumb` (str)
* `live_test_url` (str)

