from datetime import datetime
import re
import simplejson
import urllib2


class XBTestingBase(object):
    api_base_url = "http://crossbrowsertesting.com/api%(path)s?format=json"
    required_attrs = ()
    datetime_attrs = ()
    attrs = {}
    
    def __init__(self, attrs):
        self.attrs = attrs
        for name in self.required_attrs:
            if name not in self.attrs:
                raise KeyError, "required attribute '%s' missing" % name
        for name in self.datetime_attrs:
            if (name in self.attrs) and (type(self.attrs[name]) == str):
                date_string = self.attrs[name]
                if len(date_string) == 16:
                    # the 'finished_date' attribute of a test version result lacks seconds somehow. let's add them.
                    date_string += ':00'
                self.attrs[name] = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    
    
    def __getattr__(self, name):
        if name in self.attrs:
            return self.attrs[name]
        else:
            raise AttributeError, "'%s' object has no attribute '%s'" % (self.__class__.__name__, name)
    
    def _api_request(self, path):
        url = self.api_base_url % {'path': path}
        pwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        pwd_mgr.add_password(None, url, XBTesting.username, XBTesting.password)
        auth_handler = urllib2.HTTPBasicAuthHandler(pwd_mgr)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        u = urllib2.urlopen(url)
        json = u.read()
        u.close()
        return self.decode_json(json)
    
    def decode_json(self, json):
        json = self.sanitize_json(json)
        data = simplejson.loads(json)
        return data
    
    def sanitize_json(self, json):
        """
        Needed because the crossbrowsertesting.com API currently (2011-02-09) returns incorrect JSON.
        http://twitter.com/philippbosch/status/35300397857902593
        """
        return re.sub(r'html_(\d+)', '\\1', json)


class XBTesting(XBTestingBase):
    username = None
    password = None
    
    def __init__(self, attrs={}):
        if not XBTesting.username:
            raise ValueError, '%s.username not set' % self.__class__.__name__
        if not XBTesting.password:
            raise ValueError, '%s.password not set' % self.__class__.__name__
    
    def get_tests(self):
        data = self._api_request('/screenshots/show')
        tests = []
        for test in data['tests']:
            attrs = test['test']
            tests.append(XBTest(attrs=attrs))
        return tests


class XBTest(XBTestingBase):
    required_attrs = ('id',)
    datetime_attrs = ('test_date',)
    
    def get_versions(self):
        data = self._api_request('/screenshots/%s/show' % self.id)
        versions = []
        for version in data['test']['versions']:
            attrs = version['version']
            attrs['test'] = self
            versions.append(XBTestVersion(attrs=attrs))
        return versions


class XBTestVersion(XBTestingBase):
    required_attrs = ('test', 'id',)
    datetime_attrs = ('version_date',)
    
    def get_results(self):
        data = self._api_request('/screenshots/%s/version/%s/show' % (self.test.id, self.id))
        results = []
        for result in data['test']['versions'][0]['version']['results']:
            attrs = result['result']
            attrs['testversion'] = self
            results.append(XBTestVersionResult(attrs=attrs))
        return results


class XBTestVersionResult(XBTestingBase):
    required_attrs = ('testversion', 'id',)
    datetime_attrs = ('start_date', 'finished_date',)
