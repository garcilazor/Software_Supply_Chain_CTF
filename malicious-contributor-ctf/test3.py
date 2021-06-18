from packaging.markers import Marker, UndefinedEnvironmentName
marker = Marker("python_version>'2'")
print(marker)
 # We can evaluate the marker to see if it is satisfied
print(marker.evaluate())

 # We can also override the environment
env = {'python_version': '1.5.4'}
print(marker.evaluate(environment=env))

 # Multiple markers can be ANDed
and_marker = Marker("os_name=='a' and os_name=='b'")
print(and_marker)

 # Multiple markers can be ORed
or_marker = Marker("os_name=='a' or os_name=='b'")
print(or_marker)
 # Markers can be also used with extras, to pull in dependencies if
 # a certain extra is being installed
extra = Marker('extra == "bar"')
 # Evaluating an extra marker with no environment is an error
try:
    extra.evaluate()
except UndefinedEnvironmentName:
    pass
extra_environment = {'extra': ''}
print(extra.evaluate(environment=extra_environment))

extra_environment['extra'] = 'bar'
print(extra.evaluate(environment=extra_environment))