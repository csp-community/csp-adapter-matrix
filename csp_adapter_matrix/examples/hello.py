"""Reply to any Matrix message that says hello."""

import os

import csp
from csp import ts

from csp_adapter_matrix import MatrixAdapter, MatrixConfig, MatrixMessage


@csp.node
def reply_to_hello(msg: ts[MatrixMessage]) -> ts[MatrixMessage]:
    if "hello" in msg.content.lower():
        return MatrixMessage(channel=msg.channel, content=f"hello, {msg.author_name}")


def graph(adapter: MatrixAdapter):
    messages = csp.unroll(adapter.subscribe())
    csp.print("messages", messages)
    adapter.publish(reply_to_hello(messages))


if __name__ == "__main__":
    config = MatrixConfig(
        homeserver=os.environ["MATRIX_HOMESERVER"],
        user_id=os.environ["MATRIX_USER_ID"],
        access_token=os.environ["MATRIX_ACCESS_TOKEN"],
        device_id=os.environ["MATRIX_DEVICE_ID"],
    )
    csp.run(graph, MatrixAdapter(config), realtime=True)
