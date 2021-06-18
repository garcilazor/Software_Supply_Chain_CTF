from packaging.requirements import Requirement
simple_req = Requirement("name")
print(simple_req)
print(simple_req.name)
print(simple_req.url is None)
print(simple_req.extras)
print(simple_req.specifier)
print(simple_req.marker is None)
# Requirements can be specified with extras, specifiers and markers
req = Requirement('name[foo]>=2,<3; python_version>"2.0"')
print(req.name)
print(req.extras)
print(req.specifier)
print(req.marker)
# Requirements can also be specified with a URL, but may not specify
# a version.
url_req = Requirement('name @ https://github.com/pypa ;os_name=="a"')
print(url_req.name)
print(url_req.url)

print(url_req.extras)
print(url_req.marker)