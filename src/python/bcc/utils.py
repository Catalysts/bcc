# Copyright 2016 Catalysts GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def get_online_cpus():
    online_cpus = []
    with open('/sys/devices/system/cpu/online', 'r') as f:
        sysfs_online_cpus = f.read()
        for cpu_range in sysfs_online_cpus.split(','):
            rangeop = cpu_range.find('-')
            if rangeop == -1:
                online_cpus.append(int(cpu_range))
            else:
                start = int(cpu_range[:rangeop])
                end = int(cpu_range[rangeop+1:])
                online_cpus.extend(range(start, end+1))
    return online_cpus
