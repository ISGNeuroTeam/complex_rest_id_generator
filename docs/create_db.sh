#!/bin/bash
  
sudo -u postgres psql << EOF
CREATE ROLE id_generator LOGIN PASSWORD 'password';
EOF

sudo -u postgres psql << EOF
CREATE DATABASE id_generator_sequence
EOF

sudo -u postgres psql << EOF
grant all privileges on database id_generator_sequence to id_generator;
EOF


