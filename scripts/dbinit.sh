#!/bin/bash
# insta485db

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Sanity check command line options
usage() {
  echo "Usage: $0 (create|destroy|reset)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

case "$1" in
"create")
    echo sqlite3 database/exp.sqlite3 < database/schema.sql
    sqlite3 database/exp.sqlite3 < database/schema.sql
    echo sqlite3 database/exp.sqlite3 < database/data.sql
    sqlite3 database/exp.sqlite3 < database/data.sql
    ;;


  "destroy")
    echo rm -rf database/exp.sqlite3 #var/uploads
    rm -rf database/exp.sqlite3 #var/uploads
    ;;

  "reset")
    echo rm -rf database/exp.sqlite3 #var/uploads
    rm -rf database/exp.sqlite3 #var/uploads
    echo mkdir -p var/uploads
    mkdir -p var/uploads
    echo sqlite3 var/insta485.sqlite3 < sql/schema.sql
    sqlite3 var/insta485.sqlite3 < sql/schema.sql
    echo sqlite3 var/insta485.sqlite3 < sql/data.sql
    sqlite3 var/insta485.sqlite3 < sql/data.sql
    echo cp sql/uploads/* var/uploads/
    cp sql/uploads/* var/uploads/
    ;;

  *)
    usage
    exit 1
    ;;
esac