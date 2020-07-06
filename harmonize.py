#!/usr/bin/env python3
#coding: utf-8

import sys

# field indexes
ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) >= 1 and fields[ID].isdigit():
        # TODO harmonize the tag, store the harmonized tag into UPOS
        fields[UPOS] = fields[XPOS]
        if fields[XPOS][0] == 'V':
            fields[UPOS] = 'VERB'
        if fields[XPOS][0] == 'J':
            fields[UPOS] = 'ADJ'
        if fields[XPOS][0] == 'N':
            fields[UPOS] = 'NOUN'   
        if fields[XPOS][0] == 'R':
            fields[UPOS] = 'ADV'
        if fields[XPOS][0] == 'J':
            fields[UPOS] = 'ADJ'
        if fields[XPOS] == 'UH':
            fields[UPOS] = 'INTJ'
        if fields[XPOS] == 'IN':
            fields[UPOS] = 'ADP'
        if fields[XPOS] == 'DT':
            fields[UPOS] = 'DET'
        if fields[XPOS] == 'CD':
            fields[UPOS] = 'NUM'
        if fields[XPOS] == 'CC':
            fields[UPOS] = 'CCONJ'
        # output
        print('\t'.join(fields))
    else:
        # pass thru
        print(line.strip())


