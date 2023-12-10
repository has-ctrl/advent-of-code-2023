import math

from get_day_input import get_input


data = get_input(day=8).splitlines()


def _parse_input(nodes: list[str]) -> dict[str, tuple[str, str]]:
    node_dict = {}
    for node in nodes:
        source_node, left_node, right_node = node[:3], node[7:10], node[12:15]
        node_dict[source_node] = (left_node, right_node)
    return node_dict


def one() -> int:
    """
    Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
    """
    sequence = data[0]
    nodes = _parse_input(data[2:])
    current_node, target_node = "AAA", "ZZZ"
    steps = 0
    while True:
        for direction in sequence:
            if current_node == target_node:
                return steps
            current_node = nodes[current_node][0] if direction == "L" else nodes[current_node][1]
            steps += 1


def two() -> int:
    """
    Simultaneously start on every node that ends with A.
    How many steps does it take before you're only on nodes that end with Z?
    """
    sequence = data[0]
    nodes = _parse_input(data[2:])
    start_nodes = [node for node in nodes.keys() if node[2] == "A"]
    zs = []
    for node in start_nodes:
        steps = 0
        found = False
        current_node = node
        while not found:
            for direction in sequence:
                if current_node[2] == "Z":
                    zs.append(steps)
                    found = True
                    break
                current_node = nodes[current_node][0] if direction == "L" else nodes[current_node][1]
                steps += 1
    return math.lcm(*zs)


print(f"1. {one()}")
print(f"2. {two()}")
