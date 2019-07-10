Provisioning a new site at RHEL/Centos
======================================

## Required packages:

* nginx
* Python3.7
* virtualenv + pip
* Git
* xvfb

### Python 3.7 Installation

```console
cake@plate:~$ sudo -i && yum update && yum groupinstall -y "development tools" \
&& cd /usr/src
[cake@plate /usr/src]# wget http://python.org/ftp/python3.7.3/Python-3.7.3.tar.xz
[cake@plate /usr/src]# tar xvf Python-3.7.3.tar.xz && cd Python-3.7.3
[cake@plate Python-3.7.3]# ./configure --enable-optimizations
[cake@place Python-3.7.3]# make install
```

### Installing nginx

```console
cake@plate:$ sudo yum install nginx -y
```

### Installing virualenv

```console
cake@plate:$ sudo mkdir sites/domain.com
[cake@plate domain.com]$ pip3.7 install virualenv
```

### Installing xvfb

``console
cake@plate:$ sudo yum install -y Xvfb
```

## Nginx virtual Host config

* see nginx.template.conf 

## Systemd service

* see gunicorn.template.service

## Folder structure

├── deploy_tools
├── functional_tests
│   └── __pycache__
├── lists
│   ├── migrations
│   │   └── __pycache__
│   ├── __pycache__
│   ├── static
│   │   └── bootstrap
│   └── templates
├── static
│   ├── admin
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   └── bootstrap
│       ├── css
│       ├── fonts
│       └── js
├── superlist
│   └── __pycache__
└── virtualenv
    ├── bin
    │   └── __pycache__
    ├── include
    ├── lib
    │   └── python3.7
    └── lib64 -> lib
