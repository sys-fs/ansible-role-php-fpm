import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    pkg = host.package('php7.3')
    assert pkg.is_installed


def test_service(host):
    service = host.service('php7.3-fpm')

    assert service.is_running
    assert service.is_enabled
