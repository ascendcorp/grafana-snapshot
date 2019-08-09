# GrafanaSnapshot Package [![Build Status](https://travis-ci.com/ascendcorp/GrafanaSnapshot.svg?branch=master)](https://travis-ci.com/ascendcorp/GrafanaSnapshot)


## Install
If you want to use the API algorithms in your code, it is as simple as:

    $ pip install grafana-snapshot

You can test by creating a python file:

```python3
from GrafanaSnapshot.GenerateSnapshot import GenerateSnapshot

if __name__ == "__main__":
    grafana = GenerateSnapshot(auth='', host='xx', port=3000, protocol="https")
    result = grafana.generate(tags="tags", time_from=1563183710618, time_to=1563185212275)

    ## Delete snaphot by key
    grafana = DeleteSnapshot(auth='xxxxx', host='localhost', port='3000', protocol='http')
    result = grafana.delete(delete_key='some_delete_key', key=None)
```



## Uninstall
If you want to uninstall grafana-snapshot, it is as simple as:

    $ pip uninstall -y grafana-snapshot


## Status

| API | Status |
|---|---|
| Create Snapshot | + |
| Delete Snapshot | + |
| Get Snapshot by tags | - |
