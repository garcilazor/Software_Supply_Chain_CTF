from packaging.tags import Tag, sys_tags
import sys
looking_for = Tag("py{major}".format(major=sys.version_info.major), "none", "any")
supported_tags = list(sys_tags())
print(looking_for in supported_tags)
really_old = Tag("py1", "none", "any")
wheels = {really_old, looking_for}
best_wheel = None
for supported_tag in supported_tags:
    for wheel_tag in wheels:
        if supported_tag == wheel_tag:
            best_wheel = wheel_tag
            break
print(best_wheel == looking_for)