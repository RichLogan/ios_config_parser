

# IOS Config Parser ![](https://api.travis-ci.org/RichLogan/ios_config_parser.svg?branch=master) [![Stories in Ready](https://badge.waffle.io/RichLogan/ios_config_parser.png?label=ready&title=Ready)](https://waffle.io/RichLogan/ios_config_parser)


- Python module to parse IOS `sh run` output in order to work with IOS devices better.
- Provides auditing functionality.
- Designed to be used with Fabric for SSH
- Below is an example of auditing a remote router's interface descriptions:

```python
import json
from fabric.api import *
from fabric.network import disconnect_all
from fabric.context_managers import hide
from ios_config_parser import IOSDevice

# Connection Information
env.host_string = <host_name>
env.user = <username>
env.password = <password>

# Audit Interfaces
with hide('running', 'stdout', 'stderr', 'status'):
    config_file = run("sh run")
    device = IOSDevice(config_file)
    print json.dumps(device.audit_interfaces(simple=False))
    disconnect_all()
```

And the output:

```json
{
    "passed": false,
    "failed_interfaces": [
        "Loopback0"
    ]
}
```
