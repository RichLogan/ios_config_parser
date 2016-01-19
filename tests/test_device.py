import unittest
from ios_config_parser import IOSDevice


class TestCase(unittest.TestCase):
    def test_device(self):
        config_file = open("example.cisco", 'r')
        device = IOSDevice(config_file.read())

        # Creation
        self.assertEqual(type(device), IOSDevice)
        self.assertEqual(device.host_name, "retail")

        # Interfaces
        interfaces = device.details["interfaces"]
        self.assertEqual(len(interfaces), 21)
        description_count = 0
        for interface_name, interface_details in interfaces.items():
            if "description" in interface_details:
                description_count += 1
        self.assertEqual(description_count, 2)

if __name__ == '__main__':
    unittest.main()
