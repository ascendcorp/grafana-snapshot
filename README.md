# GrafanaSnapshotLibrary Package [![Build Status](https://travis-ci.com/ohmrefresh/GrafanaSnapshotLibrary.svg?branch=master)](https://travis-ci.com/ohmrefresh/GrafanaSnapshotLibrary)

# Current status in development


# grafana_api = GrafanaFace(auth='',
#                           host='xx', port=3000, protocol="https", verify=False)

#
# dashboards_info = grafana_api.search.search_dashboards(tag='tags')
# print(dashboards_info)
# dashboards = {}
# for dashboard_info in dashboards_info:
#     uid = dashboard_info["uid"]
#     dashboards[dashboard_info['uri']] = grafana_api.dashboard.get_dashboard(uid);
#
# snapshot_list = []
# for uri, dashboard in dashboards.items():
#     dashboard = dashboard["dashboard"] if "dashboard" in dashboard else dashboard
#     if time_from:
#         dashboard["time"]["from"] = time_str_from_unix_ms(time_from)
#     if time_to:
#         dashboard["time"]["to"] = time_str_from_unix_ms(time_to)
#     snapshot = grafana_api.snapshots.create_new_snapshot(dashboard, name=uri.replace("db/", ""),expires=300)
#     print(snapshot)
 