# chrony

Role to install and configure chrony - Network Time Protocol client & server

## Requirements

- Ansible >= 2.7

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - bionic
  - xenial
```

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| chrony__package_state | Whether to install the package or not | string | `present` | True |
| chrony__allow_clients | List of NTP clients, that are allowed to access to 'chronyd' | list | `None` | True |
| chrony__daemon_options | List of daemon start options | string | `-4` | True |
| chrony__ntp_servers | List of NTP servers Options are hard-coded inside a templates | list | `['0.pool.ntp.org', '1.pool.ntp.org', '2.pool.ntp.org', '3.pool.ntp.org']` | True |
| chrony__ntp_servers_custom | List of NTP servers with possibility of defining custom options. `chrony__ntp_servers` was left in template + defaults for backward compatibility. Use that variable if you want to define/not define custom options for each server. If either `chrony__ntp_servers` or `chrony__ntp_servers_custom` are not used, default template according to your OS will be load | list | `[]` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name | Description | Type | Default |
| -----| ----------- | :--: | :-----: |
| chrony__package_name | Package name to be installed. | string | `chrony` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

### centos variables

| Name | Description | Type | Default |
| -----| :---------: | :--: | ------- |
| chrony__daemon_environment_file | Environment file path. | string | `/etc/sysconfig/chronyd` |
| chrony__service_name | Service name. | string | `chronyd` |
| chrony__config_path | Path to chrony configuration files. | string | `/etc` |

**All static centos variables are described in [vars/centos.yml](vars/centos.yml)**

### ubuntu variables

| Name | Description | Type | Default |
| -----| :---------: | :--: | ------- |
| chrony__daemon_environment_file | Environment file path. | string | `/etc/default/chrony` |
| chrony__service_name | Service name. | string | `chrony` |
| chrony__config_path | Path to chrony configuration files. | string | `/etc/chrony` |

**All static ubuntu variables are described in [vars/ubuntu.yml](vars/ubuntu.yml)**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:

      - role: zerodowntime.chrony
        chrony__daemon_options: '-4'
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
