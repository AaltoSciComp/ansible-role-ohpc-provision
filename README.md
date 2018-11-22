Role Name
=========

Finish OpenHPC images.  Should be run on admin node after the images
have been setup (packages, configuration etc.).

Requirements
------------

The ansible inventory should have a host group called "ohpc_images"
which is a list of chroot's for the OpenHPC/Warewulf images. Another
host group called "ohpc_compute" should contain host names/MAC of
compute nodes.

Role Variables
--------------

- ohpc_build_kernel_ver: If set, this determines which kernel version
  to create a bootstrap image for booting the nodes. If unset,
  defaults to the version the admin node is currently running.

- ohpc_ww_file_import: List of files to import to warewulf, for
  deploying to managed nodes.


Example hosts entries
---------------------

        [ohpc_images:children]
        ohpc_images_compute
        
        [ohpc_images_compute]
        /opt/ohpc/admin/images/compute
        
        [ohpc_compute:children]
        ohpc-compute-1disk
        
        [ohpc-compute-1disk]
        node1 int_ip_addr=10.10.0.1 mac_address=xx:xx:xx:xx:xx:xx ib_ip_addr=10.11.0.1 ip_last=0.1 nhc_hw_eth=eth0
        node2 int_ip_addr=10.10.0.2 mac_address=yy:yy:yy:yy:yy:yy ib_ip_addr=10.11.0.2 ip_last=0.2 nhc_hw_ib=40 nhc_hw_eth=eth0


License
-------

MIT

Author Information
------------------

https://github.com/jabl
