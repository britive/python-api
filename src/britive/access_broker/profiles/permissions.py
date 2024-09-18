class Permissions:
    def __init__(self, britive):
        self.britive = britive
        self.base_url = f'{self.britive.base_url}/resource-manager/profiles'
    def add_permissions(self, profile_id, permission_id, version, resource_type_id, variables=[]):
        """
        Add permissions to a resource profile.
        :param profile_id: ID of the profile.
        :param permission_id: ID of the permission.
        :param version: Version of the permission.
        :param resource_type_id: ID of the resource type.
        :param variables: List of variables.
        :return: Updated profile.
        """
        params = {
            'permissionId': permission_id,
            'version': version,
            'resourceTypeId': resource_type_id,
            'variables': variables
        }
        return self.britive.post(f'{self.base_url}/{profile_id}/permissions', json=params)

    def list_permissions(self, profile_id):
        """
        Retrieve all permissions for a resource profile.
        :param profile_id: ID of the profile.
        :return: List of permissions.
        """
        return self.britive.get(f'{self.base_url}/{profile_id}/permissions')
    
    def list_available_permissions(self, profile_id):
        """
        Used to retrieve permissions available to the resource profile.
        :param profile_id: ID of the profile.
        :return: List of permissions.
        """

        return self.britive.get(f'{self.base_url}/{profile_id}/available-permissions')
    
    #not tested
    def update_permission_variables(self, profile_id, permission_id, variables=[]):
        """
        Update permission variables for a resource profile.
        :param profile_id: ID of the profile.
        :param permission_id: ID of the permission.
        :param variables: List of variables.
        :return: Updated profile.
        """
        params = {
            'variables': variables
        }
        return self.britive.patch(f'{self.base_url}/{profile_id}/permissions/{permission_id}', json=params)
    
    def delete_permission(self, profile_id, permission_id):
        """
        Delete a permission from a resource profile.
        :param profile_id: ID of the profile.
        :param permission_id: ID of the permission.
        :return: None
        """
        return self.britive.delete(f'{self.base_url}/{profile_id}/permissions/{permission_id}')
    