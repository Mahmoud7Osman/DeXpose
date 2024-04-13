# Django Server Files

This repository contains server files for hosting the Dynamic Tunnel Routing Protocol (DTRP) service online.

## Caution
These files contain plain-text passwords for performing add/clear editing operations. "Add" is used to add new addresses, while "clear" clears all addresses. This version is a pre-release, tested for stability but lacking some main operations on addresses, such as the ability to remove or edit a specific address. The plain-text password is located in `views.py` and should be changed before hosting the service online. It should never be disclosed publicly.

## Overview
This method facilitates receiving connections through tunnels like ngrok or Tor services without concerns about address changes. The DTRP service is hosted online on platforms like PythonAnywhere, enabling clients to retrieve tunnel information before attempting connections.

## How does it replace the need for Port Forwarding?
It utilizes a website to store addresses that can be changed by the owner, allowing for multiple addresses to be managed and updated. Clients retrieve these addresses through an ID Code provided to the website, eliminating the need for port forwarding and enhancing security.

## Warning
This software has the potential to initiate anonymous and illegal cyberattacks. The owner and the author of this software are not responsible for any illegal actions performed by users.
