#!/bin/bash

setsebool -P httpd_can_network_connect 1
systemctl daemon-reload
