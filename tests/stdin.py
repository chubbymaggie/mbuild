#!/usr/bin/env python
# -*- python -*-
#BEGIN_LEGAL
#
#Copyright (c) 2016 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  
#END_LEGAL

import mbuild

def dump(lines):
    if lines:
        for line in lines:
            line = line.strip()
            print "::" +  line
    else:
        print "(EMPTY)"

env = mbuild.env_t(0)
env.parse_args()

infile = file('stdin.py')
retval,output,error = mbuild.run_command('cat', stdin=infile)
print "EXIT STATUS ", str(retval)
print "OUTPUT LINES "
dump(output)
print "ERROR LINES "
dump(error)
