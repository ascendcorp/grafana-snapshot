import unittest

import requests_mock
from GrafanaSnapshot.GenerateSnapshot import GenerateSnapshot


class TestGrafanaAPI(unittest.TestCase):

    @requests_mock.Mocker()
    def test_generate(self, m):

        m.get(
            "http://localhost:3000/api/search?tag=test_tag",
            json=[
                {
                    "id": 163,
                    "uid": "cIBgcSjkk",
                    "title": "Folder",
                    "url": "/dashboards/f/000000163/folder",
                    "type": "dash-folder",
                    "tags": [],
                    "isStarred": 'false',
                    "uri": "db/folder"
                }
            ]
        )
        m.get(
            "http://localhost:3000/api/dashboards/uid/cIBgcSjkk",
            json={
                "dashboard": {
                    "id": 1,
                    "uid": "cIBgcSjkk",
                    "title": "Production Overview",
                    "tags": ["templated"],
                    "timezone": "browser",
                    "schemaVersion": 16,
                    "version": 0,
                    "time": {
                        "from": "now-15m",
                        "to": "now"
                    }
                },
                "meta": {
                    "isStarred": 'false',
                    "url": "/d/cIBgcSjkk/production-overview",
                    "slug": "production-overview"
                }
            }
        )
        m.post(
            "http://localhost:3000/api/snapshots",
            json={
                "deleteKey": "XXXXXXX",
                "deleteUrl": "myurl/api/snapshots.py-delete/XXXXXXX",
                "key": "YYYYYYY",
                "url": "myurl/dashboard/snapshot/YYYYYYY"
            },
        )

        grafana = GenerateSnapshot(auth="xxxxx", port=3000, host="localhost", protocol="http")
        results = grafana.generate(tags="test_tag", time_from=1563183710618, time_to=1563185212275)
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
