#!/bin/bash

#
# This is a quick build script for a GhostForce scanning node.
# usage: sudo ./build.sh
# It is poorly written....  These are the packages used in GhostForce
#

apt-get update
apt-get install python-dev build-essential python-lxml python-bs4 -qy

