from packaging.utils import canonicalize_name,canonicalize_version,parse_wheel_filename, parse_sdist_filename
from packaging.tags import Tag
from packaging.version import Version
name, ver, build, tags = parse_wheel_filename("foo-1.0-py3-none-any.whl")
print(name)
print(ver == Version('1.0'))

print(tags == {Tag("py3", "none", "any")})
print(not build)
print(canonicalize_name("Django"))
print(canonicalize_name("oslo.concurrency"))
print(canonicalize_name("requests"))
name, ver = parse_sdist_filename("foo-1.0.tar.gz")
print(name)
print(ver == Version('1.0'))