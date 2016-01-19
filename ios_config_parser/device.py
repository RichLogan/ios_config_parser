import os
import io


class IOSDevice(object):
    """Represents a Cisco IOS Device"""
    def __init__(self, config_file):
        """Creates a new Device. config_file should be a string e.g output from
        `sh run` or `$ cat configuration_file`
        """
        self.details = None
        self.host_name = None

        f = io.StringIO(unicode(str(config_file), "utf-8"))
        device = {}
        device["interfaces"] = {}
        lines = f.readlines()
        for index, line in enumerate(lines):
            if line.startswith("hostname"):
                self.host_name = line.split("hostname ")[1].rstrip()
            if line.startswith("interface"):
                interface = {}
                interface_name = line.split(" ", 1)[1].rstrip()
                if interface_name == "Null0":
                    continue
                index += 1
                while (lines[index].startswith(" ")):
                    if lines[index].startswith("description"):
                        description = lines[index].split("description ", 1)[1]
                        interface["description"] = description.rstrip()
                    if lines[index].startswith(" shutdown"):
                        interface["shutdown"] = True
                    index += 1
                if "shutdown" not in interface:
                    interface["shutdown"] = False
                device["interfaces"][interface_name] = interface
        self.details = device

    def audit_interfaces(self, simple=True):
        """Reports on interface setup, namely use of descriptions. Simple=True
        will give a True (pass) / False (fail). Simple=False gives a fuller
        report."""
        result = {}
        result["passed"] = True
        result["failed_interfaces"] = []
        interfaces = self.details["interfaces"].items()
        for interface_name, interface_details in interfaces:
            if not interface_details["shutdown"]:
                if "description" not in interface_details:
                    result["passed"] = False
                    result["failed_interfaces"].append(interface_name)
        if simple:
            return result["passed"]
        else:
            return result
