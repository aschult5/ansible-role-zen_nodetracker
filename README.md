# Ansible Role: zen\_nodetracker (Horizen)

[![Build Status](https://travis-ci.com/aschult5/ansible-role-zen_nodetracker.svg?branch=master)](https://travis-ci.com/aschult5/ansible-role-zen_nodetracker)

Installs and runs Horizen's nodetracker in a container on Debian/Ubuntu servers.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see [defaults/main.yml](defaults/main.yml)):

    nodetracker_ver: latest

The version of nodetracker to install. Refer to [zen-nodetracker tags on Docker Hub](https://hub.docker.com/r/aschultz5/zen-nodetracker/tags) for valid version strings.

    nodetracker_type: secure

Valid options are 'secure' and 'super'.

    nodetracker_dir: /mnt/nodetracker

Where to store nodetracker files.

    nodetracker_svc_name: zentracker
    nodetracker_svc_enabled: yes

Configuration of systemd service controlling nodetracker.

    nodetracker_docker_ctr_name: zentracker

The name of the docker container running nodetracker.

## Dependencies

  - aschult5.zend

## Example Playbook

```yaml
- hosts: nodetracker
  roles:
    - role: aschult5.zen_nodetracker
      become: yes
```

## See Also
[aschult5.zend](https://github.com/aschult5/ansible-role-zend)
[aschult5.horizen](https://github.com/aschult5/ansible-collection-horizen)

## License

MIT

## Author Information

This role was created in 2019 by Andrew Schultz for use with [Nodeler](https://www.nodeler.com)
