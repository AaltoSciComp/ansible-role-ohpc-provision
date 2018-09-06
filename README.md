Role Name
=========

Finish OpenHPC images.  Should be run on admin node after the images
have been setup (packages, configuration etc.).

Requirements
------------

The ansible inventory should have a host group called "ohpc_images"
which is a list of chroot's for the OpenHPC/Warewulf images. Another
host group called "compute" should contain host names/MAC of compute
nodes.

Role Variables
--------------

- ohpc_build_kernel_ver: If set, this determines which kernel version
  to create a bootstrap image for booting the nodes. If unset,
  defaults to the version the admin node is currently running.

- ohpc_ww_file_import: List of files to import to warewulf, for
  deploying to managed nodes.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache-2.0

Author Information
------------------

https://github.com/jabl
