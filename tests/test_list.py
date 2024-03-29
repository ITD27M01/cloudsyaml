from openstack import config as cloud_config
from clouds import listing

loader = cloud_config.OpenStackConfig(config_files=['tests/clouds.yaml'])
CLOUDS = loader.get_all_clouds()
CLOUD1 = loader.get_one_cloud(cloud='cloud1')
CLOUD2 = loader.get_one_cloud(cloud='cloud2')


class Args:
    def __init__(self):
        pass

    grep = []


args = Args


def test_listing(mocker):
    mocker.patch.object(listing, 'get_clouds')
    listing.get_clouds.return_value = CLOUDS
    assert listing.list_clouds(args) == CLOUDS


def test_listing_filtered(mocker):
    mocker.patch.object(listing, 'get_clouds')
    listing.get_clouds.return_value = CLOUDS
    args.grep = ['cloud1']
    cloud_list = listing.list_clouds(args)
    assert CLOUD1 in cloud_list and CLOUD2 not in cloud_list
