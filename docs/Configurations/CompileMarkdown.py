#!/usr/bin/env python3
"""
Compile markdown describing the 2019 Padua Training examples
based on identifying the presentation to exercise list automatically.
"""

from collections import OrderedDict
import glob
import os
import pdb
import re
import string

class Lecture:
    def __init__(self, pdf_path, txt_path):
        self.pdf_path = pdf_path
        self.txt_path = txt_path
        self.exercises = {}

    def add(self, config, args):
        if config is not None:
            self.exercises[config] = "%s" % args

    def __repr__(self):
        s = []
        s.append(self.pdf_path)
        if len(self.exercises) > 0:
            for (config, args) in self.exercises.items():
                s.append("\t%s %s" % (config, args))
        else:
            s.append("\tHas no exercises defined.")
        return '\n'.join(s)

std_cmd_pat = re.compile('./Main.sh -l RealTimeLoader -f (.*.cfg)(.*)')

def parse_cmdline(cmd):
    """Parse a standard Main.sh invocation"""
    parts = {}
    s = std_cmd_pat
    m = s.match(cmd)
    (config, args) = (None, None)
    if m: 
        (config, args) = [p.strip() for p in m.groups()] 
        if args == "-m" : args += " StateMachine:START" 
    return (config, args)

def analyse_lecture(pdf_path, txt_path):
    lecture = Lecture(pdf_path, txt_path)
    with open(txt_path, 'r') as fh:
        lines = fh.readlines()
        for cmd in lines:
            (config, post_args) = parse_cmdline(cmd)
            lecture.add(config, post_args)
    return lecture

def analyse_all():
    config_sources = glob.glob("./*.txt.config")
    exercise_sources = [f for f in config_sources if os.stat(f).st_size > 0]
    lectures = OrderedDict()
    for e in exercise_sources:
        lecture = analyse_lecture(e,e)
        lectures[e] = lecture
    return lectures

def lecture_number_as_float(txt_path):
    parts = txt_path[2:].split("_")
    return float(parts[0])

def main():
    with open("LectureExercises.md", "w") as fh:
        fh.write("# Lecture Exercises\n\n")
        fh.write("```\n")
        lectures = analyse_all()
        config_txts = list(lectures.keys())
        config_txts.sort(key = lecture_number_as_float)
        for c in config_txts:
            fh.writelines("%s\n" % lectures[c]) 
            #print(lectures[c])
        fh.write("\n```")


if __name__ == '__main__':
    main()
