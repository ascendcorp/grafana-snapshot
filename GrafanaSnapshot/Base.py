from grafana_api.grafana_face import GrafanaFace


class Base(object):
    def __init__(self, auth, host, port, protocol):
        """
        Init auth
        :param auth: API Token  (https://grafana.com/docs/http_api/auth/#create-api-token)
        :param host: Host of the API server Ex. 127.0.0.1
        :param port: Ex. 3000  (default port)
        :param protocol: http or https
         .. code-block:: python
         grafana = GenerateSnapshot(auth='', host='xx', port=3000, protocol="https")
         """
        self.api = GrafanaFace(auth=auth, host=host, port=port, protocol=protocol, url_path_prefix='', verify=False)
