#!/bin/bash
  
sudo -u postgres psql << EOF
CREATE ROLE id_generator LOGIN PASSWORD 'password';
EOF

sudo -u postgres psql << EOF
CREATE DATABASE id_generator;
EOF

sudo -u postgres psql << EOF
grant all privileges on database id_generator to id_generator;
EOF


