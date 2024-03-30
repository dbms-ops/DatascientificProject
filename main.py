#!/bin/env python3

import paramiko


class DbmsSSH:

    def __init__(self, host, username, password, timeout=5, key_filename=None):
        self.timeout = timeout
        self.host = host
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko)

    def connect(self, command):
        """
        Connect to a remote host and execute a command.

        Args:
            command: The command to be executed on the remote host.

        Returns:
            A tuple containing stdin, stdout, and stderr of the executed command.
        """

        connect = self.client.connect(hostname=self.host, username='', timeout=5, key_filename=self.key_filename)
        return connect.exec_command(command, self.timeout)


def main():
    pass


if __name__ == "__main__":
    main()
