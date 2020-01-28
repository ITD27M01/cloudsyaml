# Library and CLI for manage the clouds.yaml

## List configured clouds
    clouds list
    +--------------------+
    | name               |
    +--------------------+
    | admin              |
    | octavia            |
    | octavia-testos     |

## Get info about one cloud
    clouds show admin
    admin:
      auth:
        auth_url: https://cloud.nexign.com:5000
        password: '******'
        project_domain_name: Default
        project_name: admin
        user_domain_name: Default
        username: admin
      identity_api_verion: '3'
      region_name: SPB

## List configuration files used by SDK
    clouds files
    +-------------+--------------------------------------------------+
    | name        | path                                             |
    +-------------+--------------------------------------------------+
    | clouds.yaml | /Users/igor.tiunov/.config/openstack/clouds.yaml |
    +-------------+--------------------------------------------------+
