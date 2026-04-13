#!/usr/bin/env python3
"""Standalone runner for topic_keys annotation — invoked directly."""
import sys
sys.path.insert(0, '/home/rafal/projecty/Zwiad')
from tools.topic_keys import cmd_annotate
import argparse

class Args:
    input = '/home/rafal/projecty/Zwiad/pipeline/runs/2026-04-12T21-18-15/scanner-output.json'
    output = None
    rules = '/home/rafal/projecty/Zwiad/pipeline/config/topic-key-rules.json'

sys.exit(cmd_annotate(Args()))
