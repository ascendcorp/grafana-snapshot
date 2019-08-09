import unittest

import requests_mock
from GrafanaSnapshot.DeleteSnapshot import DeleteSnapshot


class TestDeleteSnapshot(unittest.TestCase):

    @requests_mock.Mocker()
    def test_delete_snapshot_with_delete_key(self, m):
        m.get(
            'http://localhost:3000/api/snapshots-delete/some_delete_key',
            json="{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        )

        grafana = DeleteSnapshot(auth='xxxxx', host='localhost', port='3000', protocol='http')
        result = grafana.delete(delete_key='some_delete_key', key=None)

        expected = "{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        self.assertEqual(result, expected)

    @requests_mock.Mocker()
    def test_delete_snapshot_with_key(self, m):
        m.delete(
            'http://localhost:3000/api/snapshots/some_key',
            json="{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        )

        grafana = DeleteSnapshot(auth='xxxxx', host='localhost', port='3000', protocol='http')
        result = grafana.delete(delete_key=None, key='some_key')

        expected = "{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        self.assertEqual(result, expected)

    @requests_mock.Mocker()
    def test_delete_snapshot_with_both(self, m):
        m.get(
            'http://localhost:3000/api/snapshots-delete/some_delete_key',
            json="{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        )

        grafana = DeleteSnapshot(auth='xxxxx', host='localhost', port='3000', protocol='http')
        result = grafana.delete(delete_key='some_delete_key', key='some_key')

        expected = "{'message': \"Snapshot deleted. It might take an hour before it\'s cleared from any CDN caches.\"}"
        self.assertEqual(result, expected)

    def test_delete_snapshot_without_key_and_delete_key(self):
        grafana = DeleteSnapshot(auth='xxxxx', host='localhost', port='3000', protocol='http')

        self.assertIsNone(grafana.delete())
