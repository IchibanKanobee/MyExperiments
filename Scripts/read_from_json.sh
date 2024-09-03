#!/bin/bash

json_path="security/settings.json"
ROOT_DIR=`jq '.root_directory' $json_path`
echo $ROOT_DIR
PSW=`jq '.database_password' $json_path`
echo $PSW
