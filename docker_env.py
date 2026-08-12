import docker
import os

class DockerSandbox:
    """
    Provides an isolated Docker environment for the autonomous agent to safely 
    compile, run, and test code without compromising the host system.
    """
    def __init__(self, image: str = "python:3.11-slim"):
        self.client = docker.from_env()
        self.image = image
        self.container = None

    def start_sandbox(self, workspace_path: str):
        print(f"[DockerSandbox] Starting container from {self.image}...")
        try:
            self.container = self.client.containers.run(
                self.image,
                command="sleep infinity",
                volumes={os.path.abspath(workspace_path): {'bind': '/workspace', 'mode': 'rw'}},
                working_dir="/workspace",
                detach=True,
                network_mode="none" # Max isolation
            )
            print(f"[DockerSandbox] Sandbox active: {self.container.short_id}")
        except Exception as e:
            print(f"[DockerSandbox] Failed to start container: {e}")

    def execute_code(self, command: str) -> tuple[int, str]:
        if not self.container:
            raise RuntimeError("Sandbox is not running.")
        
        print(f"[DockerSandbox] Executing: {command}")
        exit_code, output = self.container.exec_run(command)
        return exit_code, output.decode('utf-8')

    def teardown(self):
        if self.container:
            print(f"[DockerSandbox] Tearing down container {self.container.short_id}...")
            self.container.stop()
            self.container.remove()
