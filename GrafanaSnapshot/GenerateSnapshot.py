from grafana_api.grafana_face import GrafanaFace
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GenerateSnapshot:
    api = None

    def __init__(self, auth, host, port, protocol):
        self.api = GrafanaFace(auth=auth, host=host, port=port, protocol=protocol, verify=False)

    def generate(self, tags, time_from, time_to, expires=300):

        """
        Generate Grafana snapshot with expires
        :param tags:
        :param time_from:
        :param time_to:
        :param expires:
        :return:
        """

        dashboards_info = self.api.search.search_dashboards(tag=tags)
        dashboards = {}
        for dashboard_info in dashboards_info:
            uid = dashboard_info["uid"]
            dashboards[dashboard_info['uri']] = self.api.dashboard.get_dashboard(uid);

        snapshot_list = []
        for uri, dashboard in dashboards.items():
            dashboard = dashboard["dashboard"] if "dashboard" in dashboard else dashboard
            if time_from:
                dashboard["time"]["from"] = self.__time_str_from_unix_ms(time_from)
            if time_to:
                dashboard["time"]["to"] = self.__time_str_from_unix_ms(time_to)

            snapshot_name = "{}_{}_{}".format(uri.replace("db/", ""), dashboard["time"]["from"],
                                              dashboard["time"]["to"])

            snapshot = self.api.snapshots.create_new_snapshot(dashboard, name=snapshot_name, expires=expires)
            snapshot_list.append(snapshot)

        return snapshot_list

    @staticmethod
    def __time_str_from_unix_ms(unix_ms):
        return datetime.datetime.utcfromtimestamp(int(unix_ms / 1000)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
