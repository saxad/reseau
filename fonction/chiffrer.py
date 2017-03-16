#! /usr/bin/env python
# -*- coding: utf8 -*-

import hashlib

def chiffrer(mdp):
    mdp_chiffrer = hashlib.sha1(mdp).hexdigest()
    return mdp_chiffrer
