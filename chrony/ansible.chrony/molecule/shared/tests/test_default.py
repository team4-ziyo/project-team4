import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chrony_installed(host):
    chrony = host.package("chrony")
    assert chrony.is_installed


def test_env_file(host):
    distribution = host.system_info.distribution

    if distribution == 'centos':
        filename = '/etc/sysconfig/chronyd'
    elif distribution == 'ubuntu':
        filename = '/etc/default/chrony'

    f = host.file(filename)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config_file(host):
    distribution = host.system_info.distribution

    if distribution == 'centos':
        filename = '/etc/chrony.conf'
    elif distribution == 'ubuntu':
        filename = '/etc/chrony/chrony.conf'

    f = host.file(filename)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config_file_content(host):
    distribution = host.system_info.distribution

    if distribution == 'centos':
        filename = '/etc/chrony.conf'
    elif distribution == 'ubuntu':
        filename = '/etc/chrony/chrony.conf'

    f = host.file(filename)

    assert f.contains('0.pool.ntp.org')


def test_chrony_running_and_enabled(host):
    distribution = host.system_info.distribution

    if distribution == 'centos':
        serviceName = 'chronyd'
    elif distribution == 'ubuntu':
        serviceName = 'chrony'

    chrony = host.service(serviceName)

    assert chrony.is_running
    assert chrony.is_enabled
