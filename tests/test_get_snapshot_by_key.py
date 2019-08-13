import unittest
import requests_mock
from GrafanaSnapshot.snapshot_face import SnapshotFace


class TestGetSnapshotByKey(unittest.TestCase):

    @requests_mock.Mocker()
    def test_get_snapshot_by_key(self, m):
        m.get(
            'http://localhost:3000/api/dashboard/snapshots',
            json=[
                {
                    "id":8,
                    "name":"some_key",
                    "key":"YYYYYYY",
                    "orgId":1,
                    "userId":1,
                    "external":'false',
                    "externalUrl":"",
                    "expires":"2200-13-32T25:23:23+02:00",
                    "created":"2200-13-32T28:24:23+02:00",
                    "updated":"2200-13-32T28:24:23+02:00"
                }
            ]
        )

        grafana = SnapshotFace(auth='xxxxx', host='localhost', port='3000', protocol='http')
        results = grafana.snapshots.get_snapshot_by_key(key='some_key', host='localhost')

        self.assertEqual(len(results), 1)

    @requests_mock.Mocker()
    def test_get_snapshot_by_key_not_found(self, m):
        m.get(
            'http://localhost:3000/api/dashboard/snapshots',
            json=[
                {
                    "id":8,
                    "name":"some_key",
                    "key":"YYYYYYY",
                    "orgId":1,
                    "userId":1,
                    "external":'false',
                    "externalUrl":"",
                    "expires":"2200-13-32T25:23:23+02:00",
                    "created":"2200-13-32T28:24:23+02:00",
                    "updated":"2200-13-32T28:24:23+02:00"
                }
            ]
        )

        grafana = SnapshotFace(auth='xxxxx', host='localhost', port='3000', protocol='http')
        results = grafana.snapshots.get_snapshot_by_key(key='not_found', host='localhost')

        self.assertEqual(len(results), 0)
