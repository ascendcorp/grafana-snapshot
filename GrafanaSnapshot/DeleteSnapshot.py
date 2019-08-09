from .Base import Base


class DeleteSnapshot(Base):

    def delete(self, delete_key=None, key=None):

        """

        Delete snapshot with delete_key or snapshot key
        :param delete_key:
        :param key:
        :return:
        """

        if delete_key:
            return self.api.snapshots.delete_snapshot_by_delete_key(delete_key)
        elif key:
            return self.api.snapshots.delete_snapshot_by_key(key)
        else:
            return None
