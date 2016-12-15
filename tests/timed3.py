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
import find
import mbuild

env = mbuild.env_t(0)
env.parse_args()

retval, output, error = mbuild.run_command_timed('./spew', seconds=2)
print "RETURN CODE ", retval
print "OUTPUT LINES ", len(output)
print "ERROR LINES ", len(error)
for l in error:
    print 'ERROR OUTPUT [{}]'.format(l.strip())
