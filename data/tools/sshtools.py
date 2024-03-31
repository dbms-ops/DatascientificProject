import sys

import paramiko


class DbmsSSH:

    def __init__(self, host, username, password=None, timeout=5, key_filename=None):
        self.timeout = timeout
        self.host = host
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def do_command(self, command):
        """
        Connect to a remote host and execute a command.

        Args:
            command: The command to be executed on the remote host.

        Returns:
            A tuple containing stdin, stdout, and stderr of the executed command.
        """

        self.client.connect(
            hostname=self.host,
            username=self.username,
            timeout=5,
            key_filename=self.key_filename,
        )
        return self.client.exec_command(command, self.timeout)

    def __str__(self) -> str:
        format_str = """
        {'-'*50}
        {stdout}
        {stderr}
        {'-'*50}
        """
        _, stdout, stderr = self.do_command()
        return format_str.format(stdout=stdout.read(), stderr=stderr.read())

    def __del__(self):
        self.client.close()


if __name__ == "__main__":
    ssh = DbmsSSH(
        host=sys.argv[1], username="ops", key_filename="/home/ops/.ssh/id_rsa.pub"
    )
    stdin, stdout, stderr = ssh.do_command(sys.argv[2])
    print(stdout.read())
    print(stderr.read())
