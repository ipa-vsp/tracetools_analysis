# Copyright 2019 Robert Bosch GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for profile data model."""

import pandas as pd

from . import DataModel


class ProfileDataModel(DataModel):
    """Container to model pre-processed profiling data for analysis."""

    def __init__(self) -> None:
        """Constructor."""
        super().__init__()
        self.times = pd.DataFrame(columns=[
            'tid',
            'depth',
            'function_name',
            'start_timestamp',
            'duration',
        ])

    def add_duration(
        self,
        tid: int,
        depth: int,
        function_name: str,
        start_timestamp: int,
        duration: int,
    ) -> None:
        data = {
            'tid': tid,
            'depth': depth,
            'function_name': function_name,
            'start_timestamp': start_timestamp,
            'duration': duration,
        }
        self.times = self.times.append(data, ignore_index=True)

    def print_model(self) -> None:
        """Debug method to print every contained df."""
        print('====================PROFILE DATA MODEL====================')
        tail = 20
        print(f'Times (tail={tail}):\n{self.times.tail(tail).to_string()}')
        print('==========================================================')
