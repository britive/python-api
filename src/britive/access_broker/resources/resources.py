from .labels import Labels
from .permissions import Permissions
from .types import Types


class Resources:
    def __init__(self, britive) -> None:
        self.britive = britive
        self.labels = Labels(britive)
        self.types = Types(britive)
        self.permissions = Permissions(britive)
        self.base_url = f'{self.britive.base_url}/resource-manager/resources'

    def list(self, filter_expression: str = '', search_text: str = '') -> list:
        """
        Retrieve all resources.

        :param filter_expression: Parameter to filter resources by name. Example: `name eq profile1`.
        :param search_text: Filter resources by search text.
        :return: List of resources.
        """

        params = {
            **({'filter': filter_expression} if filter_expression else {}),
            **({'searchText': search_text} if search_text else {}),
        }

        return self.britive.get(f'{self.base_url}', params=params)

    def create(self, name: str, resource_type_id: str, description: str = '') -> dict:
        """
        Create a new resource.

        :param name: Name of the resource.
        :param description: Description of the resource.
        :param resource_type_id: ID of the resource type.
        :return: Created resource.
        """

        params = {
            'name': name,
            'description': description,
            'resourceType': {'id': resource_type_id},
        }

        return self.britive.post(self.base_url, json=params)

    def get(self, resource_id: str) -> dict:
        """
        Retrieve a resource by ID.

        :param resource_id: ID of the resource.
        :return: Resource.
        """

        return self.britive.get(f'{self.base_url}/{resource_id}')

    def update(self, resource_id: str, description: str = '', resource_labels: list = None) -> dict:
        """
        Update a resource.

        :param resource_id: ID of the resource.
        :param name: Name of the resource.
        :param description: Description of the resource.
        :param resource_labels: List of Resource Labels.
        :return: Updated resource.
        """

        params = {
            'name': self.get(resource_id)['name'],
            'resourceType': {'id': self.get(resource_id)['resourceType']['id']},
            **({'description': description} if description else {}),
            **({'resourceLabels': resource_labels} if resource_labels else {}),
        }

        return self.britive.put(f'{self.base_url}/{resource_id}', json=params)

    def delete(self, resource_id: str) -> dict:
        """
        Delete a resource.

        :param resource_id: ID of the resource.
        :return: None
        """

        return self.britive.delete(f'{self.base_url}/{resource_id}')

    def add_broker_pools(self, resource_id: str, pools: list) -> list:
        """
        Add broker pools to a resource.

        :param resource_id: ID of the resource.
        :param pools: List of broker pools.
        :return: List of broker pools.
        """

        return self.britive.post(f'{self.base_url}/{resource_id}/broker-pools', json=pools)
