#!/bin/bash

set -euxo pipefail

PYTHON=python3.11

$PYTHON -m premailer -f invite.html -o invite_inlined.html

rm invite.eml

cat > invite.eml <<EOF 
From: Fachschaft Elektrotechnik <fachschaft-e@ost.ch>
To:
Date: Mon Feb 24 20:00:00 CET 2025
Subject: Invitation to the Git Workshop!
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary=separate

--separate
Content-Type: text/plain; charset=utf-8

EOF

cat invite.txt >> invite.eml

cat >> invite.eml <<EOF

--separate
Content-Type: text/html; charset=utf-8

EOF

cat invite.html >> invite.eml

cat >> invite.eml <<EOF

--separate--
EOF

rm invite_inlined.html
