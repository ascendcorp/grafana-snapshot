# GrafanaSnapshotLibrary Package [![Build Status](https://travis-ci.com/ohmrefresh/GrafanaSnapshot.svg?branch=master)](https://travis-ci.com/ohmrefresh/GrafanaSnapshot)

# Current status in development

## Install
If you want to use the API algorithms in your code, it is as simple as:

    $ pip3 install grafana-snapshot

You can test by creating a python file:

```python3
from GrafanaSnapshot.GenerateSnapshot import GenerateSnapshot

if __name__ == "__main__":
    grafana = GenerateSnapshot(auth='', host='xx', port=3000, protocol="https")
    grafana.generate(tags="tags", time_from="1563183710618", time_to="1563185212275")

```

## Uninstall
If you want to uninstall grafana-snapshot, it is as simple as:

    $ pip3 uninstall -y grafana-snapshot
