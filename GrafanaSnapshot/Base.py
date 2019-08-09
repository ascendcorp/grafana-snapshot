from grafana_api.grafana_face import GrafanaFace


class Base(object):
    def __init__(self, auth, host, port, protocol):
        self.api = GrafanaFace(auth=auth, host=host, port=port, protocol=protocol, url_path_prefix='', verify=False)
