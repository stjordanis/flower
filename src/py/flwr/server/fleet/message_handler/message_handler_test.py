# Copyright 2020 Adap GmbH. All Rights Reserved.
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
# ==============================================================================
"""Fleet API message handler tests."""


from unittest.mock import MagicMock

from flwr.proto.fleet_pb2 import PullTaskInsRequest, PushTaskResRequest
from flwr.proto.node_pb2 import Node
from flwr.proto.task_pb2 import Task, TaskRes

from .message_handler import pull_task_ins, push_task_res


def test_pull_task_ins() -> None:
    """Test pull_task_ins."""
    # Prepare
    request = PullTaskInsRequest(node=Node(node_id=1, anonymous=False))
    state = MagicMock()

    # Execute
    pull_task_ins(request=request, state=state)

    # Assert
    state.store_task_ins.assert_not_called()
    state.get_task_ins.assert_called_once()
    state.store_task_res.assert_not_called()
    state.get_task_res.assert_not_called()


def test_push_task_res() -> None:
    """Test push_task_res."""
    # Prepare
    request = PushTaskResRequest(
        task_res_list=[
            TaskRes(
                task_id="",
                group_id="",
                workload_id="",
                task=Task(),
            ),
        ],
    )
    state = MagicMock()

    # Execute
    push_task_res(request=request, state=state)

    # Assert
    state.store_task_ins.assert_not_called()
    state.get_task_ins.assert_not_called()
    state.store_task_res.assert_called_once()
    state.get_task_res.assert_not_called()
