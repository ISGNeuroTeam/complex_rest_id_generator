#!/bin/bash
  
sudo -u postgres psql << EOF
REASSIGN OWNED BY id_generator TO postgres;
DROP OWNED BY id_generator;
drop database id_generator_sequence;
EOF
