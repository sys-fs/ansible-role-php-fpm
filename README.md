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
        pm: dynamic
        php_admin_values:
          - name: memory_limit
            value: '128M'

List of pools to create. There are many optional variables than can be defined
within a pool. Please see the [pool template](templates/pool.conf.j2) for more
information on variables that can be set for customising pools.

Example Playbook
----------------

    - hosts: php
	  vars:
	    - php_fpm_pools:
           - name: dev
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
