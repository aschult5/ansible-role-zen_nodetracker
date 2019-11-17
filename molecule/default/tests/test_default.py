import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_tracker_is_installed(host):
    ctr_name = os.environ['NODETRACKER_DOCKER_CTR_NAME']
    nodetracker = host.docker(ctr_name)
    assert nodetracker


def test_tracker_running(host):
    svc_name = os.environ['NODETRACKER_SVC_NAME']
    nodetracker = host.service(svc_name)
    assert nodetracker.is_enabled
    assert nodetracker.is_running
