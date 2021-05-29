import docker
import os

this_directory = os.path.dirname(os.path.realpath(__file__))
webserver_dir = os.path.join(this_directory, "webserver")
randomclient_dir = os.path.join(this_directory, "randomclient")

class CDWLevel:
    NETWORK_NAME = "ctf-cdw-net"
    WEBSERVER_IMAGE_NAME = "ctf-cdw-codetrov"
    RANDOMCLIENT_IMAGE_NAME = "ctf-cdw-randomclient"

    def __init__(self):
        self.client = docker.from_env()
        self.network = None
        self.webserver_image = None
        self.webserver_container = None
        self.randomclient_image = None
        self.randomclient_container = None
        self.is_setup = False

    def setup_level(self):
        self.teardown_level()
        self.build_necessary_images()
        self.network = self.client.networks.create(self.NETWORK_NAME, check_duplicate=True)
        self.webserver_container = self.client.containers.run(image=self.WEBSERVER_IMAGE_NAME, 
            name=self.WEBSERVER_IMAGE_NAME, 
            ports={80: 80},
            network=self.NETWORK_NAME, 
            detach=True, 
            auto_remove=True)
        self.randomclient_container = self.client.containers.run(image=self.RANDOMCLIENT_IMAGE_NAME, name=self.RANDOMCLIENT_IMAGE_NAME, network=self.NETWORK_NAME, detach=True, auto_remove=True)
        #client.containers.run("ubuntu", tty=True, stdin_open=True, detach=True, name="bash")   # TODO Make a container for user to play in.
        self.is_setup = True

    def build_necessary_images(self):
        self.webserver_image = self.client.images.build(path=webserver_dir, tag=self.WEBSERVER_IMAGE_NAME, rm=True)
        self.randomclient_image = self.client.images.build(path=randomclient_dir, tag=self.RANDOMCLIENT_IMAGE_NAME, rm=True)

    def play_level(self):
        # Start the level for the player. In our case, put them in a docker image.
        os.system('docker run -it --rm ubuntu bash')

    def teardown_level(self, remove_images=False):
        # Delete the ctf-cd-net and stop the levels. 
        self.is_setup = False
        self._ensure_container_is_stopped_and_removed(self.WEBSERVER_IMAGE_NAME)
        self._ensure_container_is_stopped_and_removed(self.RANDOMCLIENT_IMAGE_NAME)
        networks = self.client.networks.list(self.NETWORK_NAME)
        for network in networks:  # Should only be 0 or 1 network, but this will gaurantee all copies are eliminated.
            network.remove()
        if remove_images:
            self._ensure_image_is_removed(self.WEBSERVER_IMAGE_NAME)
            self._ensure_image_is_removed(self.RANDOMCLIENT_IMAGE_NAME)

    def _ensure_container_is_stopped_and_removed(self, name):
        try:
            container = self.client.containers.get(name)
        except docker.errors.NotFound:
            return
        container.stop()

    def _ensure_image_is_removed(self, name):
        try:
            self.client.images.remove(name)
        except docker.errors.ImageNotFound:
            pass

if __name__ == "__main__":
    l = CDWLevel()
    l.setup_level()
    # l.player_level()
    input("Press enter to stop running level")
    l.teardown_level()