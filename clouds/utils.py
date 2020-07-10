def to_dict(connection):
    dict_connection = dict()
    dict_connection['name'] = connection.name
    dict_connection['auth'] = connection.auth
    return dict_connection


def to_list(connection):
    list_connection = list()
    cloud_dict = dict()
    config_dict = {
        'auth': connection.auth,
        'region_name': connection.get_region_name(),
        'identity_api_verion': connection.get_api_version('identity')
    }
    config_dict['auth']['password'] = str("******")
    cloud_dict[connection.name] = config_dict
    list_connection.append(cloud_dict)
    return list_connection
