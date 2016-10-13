# -*- coding: utf-8 -*-
#
# Copyright 2016 Ricequant, Inc
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


# TODO make field readonly
# TODO use nametuple to reduce memory


class Risk(object):
    def __init__(self):
        self.volatility = .0
        self.alpha = .0
        self.beta = .0
        self.sharpe = .0
        self.sortino = .0
        self.information_rate = .0
        self.drawdown_time = .0
        self.max_drawdown = .0
        self.tracking_error = .0
        self.downside_risk = .0

    def __repr__(self):
        return "Risk({0})".format(self.__dict__)
