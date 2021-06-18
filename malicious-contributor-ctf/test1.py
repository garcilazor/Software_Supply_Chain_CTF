from packaging.version import Version, parse, LegacyVersion
v1 = parse("1.0a5")
v2 = Version("1.0")

print(v1)
print(v2)
print(v1<v2)
print(v1.epoch)
print(v1.release)
print(v1.pre)
print(v1.is_prerelease)

print(v2.is_prerelease)

print(Version("1.0").post)
print(Version("1.0").is_postrelease)

print(Version("1.0.post0").post)
print(Version("1.0.post0").is_postrelease)

v3 = LegacyVersion("1.3")
print(v1>v3)

v1 = parse('0.9.8a')
v2 = parse('0.9.8beta')
v3 = parse('0.9.8r')
v4 = parse('0.9.8rev')
v5 = parse('0.9.8t')
print (v1)
print (v1.is_prerelease)

print (v2)

print (v2.is_prerelease)

print (v3)

print (v3.is_postrelease)

print (v4)

print (v4.is_postrelease)

print (v5)

print (v5.is_prerelease)

print (v5.is_postrelease)