from grafana_api.grafana_face import GrafanaFace


class DeleteSnapshot:

    def __init__(self, auth, host, port, protocol):
        self.api = GrafanaFace(auth=auth, host=host, port=port, protocol=protocol, url_path_prefix="", verify=False)

    def delete(self, delete_key=None, key=None):

        """

        Delete snapshot with delete_key or snapshot key
        :param delete_key:
        :param key:
        :return:
        """

        if delete_key:
            print('delete_key ' + delete_key)
            return self.api.snapshots.delete_snapshot_by_delete_key(delete_key)
        elif key:
            print('key ' + key)
            return self.api.snapshots.delete_snapshot_by_key(key)
        else:
            print('NONE')
            return None
