* Created Vagrantfile with the basic Vagrant box configuration: type of OS, port forwarding, playbook file location, adjustment of the basic repositories, since 'mirrorlist' doesn't support Centos 8 anymore.
* Created Ansible playbook file with the rest of the configuration and installation instructions: added Prometheus repository, OS packages upgrade and installation, starting/enabling services and conf adjustment
* File vault_pass contains Ansible vault password for Grafana admin 
* Firewall daemon is running and opens the ports "22", "80", "3000", "9090", "9100"
* SELinux is in enforcing mode
* Grafana imports config file, datasource and dashboard settings from from /files/grafana.ini | grafana-dashboard.yaml | grafana-datasource.yaml | grafana-metrics.json
* Created app-bottle.py web page running on Python module bottle, that counts visits. Created app-bottle.service for the script that is started after boot.
* Edited /usr/lib/systemd/system/node_exporter.service to send metrics from systemd
------------------------------------------------
When box is up and running:
* http://192.168.56.1:8080/ (IP address depends on your settings)
*   /app -> loads Python bottle micro web-framework that counts visits
*   /health -> currently it works only as redirect to Prometheus 
*   /grafana -> works as reverse proxy and exposes default Grafana web interface with the login prompt
*   /dashboard -> works as redirect to dashboard, however login is still needed
