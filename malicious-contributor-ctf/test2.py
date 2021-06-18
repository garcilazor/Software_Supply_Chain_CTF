from packaging.specifiers import SpecifierSet
from packaging.version import Version
spec1 = SpecifierSet("~=1.0")
print(spec1)

spec2 = SpecifierSet(">=1.0")
print(spec2)

# We can combine specifiers
combined_spec = spec1 & spec2
print(combined_spec)

# We can also implicitly combine a string specifier
combined_spec &= "!=1.1"
print(combined_spec)

# Create a few versions to check for contains.
v1 = Version("1.0a5")
v2 = Version("1.0")
 # We can check a version object to see if it falls within a specifier
print(v1 in combined_spec)

print(v2 in combined_spec)

 # We can even do the same with a string based version
print("1.4" in combined_spec)

 # Finally we can filter a list of versions to get only those which are
 # contained within our specifier.
print(list(combined_spec.filter([v1, v2, "1.4"])))