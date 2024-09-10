class ResourcePermissions:
    def __init__(self, britive):
        self.britive = britive
        self.base_url = f'{self.britive.base_url}/resource-manager'

    def list(self, resource_type_id) -> list:
        """
        Retrieve all permissions for a resource type.

        :param resource_type_id: ID of the resource type.
        :return: List of permissions.
        """

        return self.britive.get(f'{self.base_url}/resource-types/{resource_type_id}/permissions')

    def create(self, resource_type_id, file : bytes = None, **kwargs) -> dict:
        """
        Create a new permission for a resource type.

        :param resource_type_id: ID of the resource type.
        :param file: File to upload.
        :param kwargs: Valid fields are...
            name
            description
            createdBy
            updatedBy
            version
            checkinURL 
            checkoutURL
            checkinFileName
            checkoutFileName
            checkinTimeLimit
            checkoutTimeLimit
            variables - List of variables
        :return: Created permission.
        """
        if not file:
            params = {
                'resourceTypeId' : resource_type_id,
                'isDraft' : False,
                **kwargs
            }
            return self.britive.post(f'{self.base_url}/permissions', json=params)
        else:
            params = {
                'resourceTypeId' : resource_type_id,
                'isDraft' : False,
                **kwargs
            }
            return self.britive.post(f'{self.base_url}/permissions', json=params, files = {'file': file})

    def update(self, permission_id, file : bytes = None, **kwargs) -> dict:     
        """
        Update a permission.

        :param permission_id: ID of the permission.
        :param file: File to upload.
        :param kwargs: Valid fields are...
            name
            description
            createdBy
            updatedBy
            version
            checkinURL 
            checkoutURL
            checkinFileName
            checkoutFileName
            checkinTimeLimit
            checkoutTimeLimit
            variables - List of variables
        :return: Updated permission.
        """
        if not file:
            return self.britive.put(f'{self.base_url}/permissions/{permission_id}', json=kwargs)
        else:
            return self.britive.put(f'{self.base_url}/permissions/{permission_id}', json=kwargs, files = {'file': file})
        
        
    
    def get(self, permission_id, version_id = None) -> dict:
        """
        Retrieve a permission by ID.

        :param permission_id: ID of the permission.
        :param version_id: ID of the version. Optional.
        :return: Permission.
        """
        if version_id:
            return self.britive.get(f'{self.base_url}/permissions/{permission_id}/{version_id}')
        else:
            return self.britive.get(f'{self.base_url}/permissions/{permission_id}')
    
    def delete(self, permission_id, version_id = None) -> dict:
        """
        Delete a permission.

        :param permission_id: ID of the permission.
        :param version_id: Version of the permission. Optional.
        :return: None
        """
        if version_id:
            return self.britive.delete(f'{self.base_url}/permissions/{permission_id}/{version_id}')
        else:
            return self.britive.delete(f'{self.base_url}/permissions/{permission_id}')
    
    def get_urls(self, permission_id) -> dict:
        """
        Retrieve URLs for a permission.

        :param permission_id: ID of the permission.
        :return: URLs.
        """
        return self.britive.get(f'{self.base_url}/permissions/get-urls/{permission_id}')