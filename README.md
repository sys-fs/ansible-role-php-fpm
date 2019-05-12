sys-fs.php-fpm
==============

This role installs and configures php-fpm from the sury.org repo on Ubuntu and
Debian.

Requirements
------------

This role requires at least Ansible 2.5.

Role Variables
--------------

	php_fpm_packages:
	  - php7.3
	  ...
	  - php7.3-zip

List of PHP packages to install.

	php_fpm_pools:
	  - name: www
	    type: unix
        pm: dynamic
        php_admin_values:
          - name: memory_limit
            value: '128M'

List of pools to create. There are many optional variables than can be defined
within a pool. The following table details the pool variables:

Name | Default | Description
---- | ------- | -----------
name | www     | The name of the pool. Also affects the name of the socket when type is unix.

type | '' | The type of socket to listen on. Can be either 'tcp' or 'unix'. Must be specified.
listen | 127.0.0.1:9000 | Address and port to listen on when type is tcp.
listen_allowed_clients | '' | Addresses allowed to talk to FPM when type is tcp. If omitted defaults to allowing all addresses.
pm | '' | The pm to use. Can be one of 'static', 'dynamic', or 'ondemand'. Must be specified.
pm_max_children | 20 | Total number of child processes to create with static, or the max number of child processes to create with dynamic or ondemand.
pm_start_servers | 5 | Only useful with the dynamic pm. Number of child processes to create on startup.
pm_min_spare_servers | 5 | Only useful with the dynamic pm. Desired minimumnumber of child processes.
pm_max_spare_servers | 5 | Only useful with the dynamic pm. Desired maximumnumber of child processes.
pm_process_idle_timeout | 10s | Only useful with the ondemand pm. Time until an inactive child process is killed.
pm_max_requests | 500 | The number of requests that child processes should execute before respawning. Can be set to 0 for no limit.
php_admin_flags | [] | Local overrides of php.ini values. Boolean (on/off) values only. Cannot be overridden by ini_set
php_flags | [] | Local overrides of php.ini values. Boolean ('on' and 'off') values only. Can be overridden by ini_set
php_admin_values | [] | Local overrides of php.ini values. Values other than booleans ('on' and 'off') only. Cannot be overridden by ini_set
php_values | [] | Local overrides of php.ini values. Values other than booleans ('on' and 'off') only. Can be overridden by ini_set

Example Playbook
----------------

    - hosts: php
	  vars:
	    - php_fpm_pools:
           - name: dev
	         type: unix
             pm: static
             pm_max_children: 100
             php_admin_values:
               - name: memory_limit
                 value: '512M'
               - name: 'opcache.enable'
                 value: 0
      roles:
        - sys-fs.php-fpm

License
-------

MIT
