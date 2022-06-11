def _siftdown_nodes(arr: list, start_index: int, index: int):
    item = arr[index]

    while index > start_index:
        parent_index = (index - 1) >> 1
        parent = arr[parent_index]

        if item[1] >= parent[1]:
            break

        arr[index] = parent
        index = parent_index

    arr[index] = item


def _siftup_nodes(arr: list, start_index: int):
    arr_len = len(arr)
    index = start_index
    item = arr[start_index]
    child_index = 2 * start_index + 1

    while child_index < arr_len:
        right_index = child_index + 1

        if right_index < arr_len and not arr[child_index][1] < arr[right_index][1]:
            child_index = right_index

        arr[index] = arr[child_index]
        index = child_index
        child_index = 2 * index + 1

    arr[index] = item
    _siftdown_nodes(arr, start_index, index)


def _heapify_nodes(arr: list):
    for i in range(len(arr) // 2 - 1, -1, -1):
        _siftup_nodes(arr, i)


def create_char_occurrences(text: str):
    occurrences = {}
    for c in text:
        occurrences[c] = occurrences.get(c, 0) + 1

    return occurrences


def _create_nodes(char_occurrences: dict):
    queue = []
    for c, n in char_occurrences.items():
        queue.append([c, n])
    _heapify_nodes(queue)

    nodes = {}
    while len(queue) > 1:
        x = queue.pop(0)
        y = queue.pop(0)

        k = x[0] + y[0]
        n = x[1] + y[1]

        nodes[k] = [x[0], y[0]]

        queue.append([k, n])
        _heapify_nodes(queue)

    return nodes


def create_codes(text: str):
    occurrences = create_char_occurrences(text)
    nodes = _create_nodes(occurrences)

    codes = {}
    for c in occurrences.keys():
        for children in nodes.values():
            if c in children[0]:
                codes[c] = "0" + codes.get(c, "")
            elif c in children[1]:
                codes[c] = "1" + codes.get(c, "")

    return codes


def encode(text: str, codes: dict):
    compressed = ""
    for c in text:
        compressed += codes[c]

    return compressed


def decode(encoded_text: str, codes: dict):
    encoded_text_copy = encoded_text
    text = ""

    while len(encoded_text_copy) > 0:
        for c, code in codes.items():
            code_len = len(code)
            if code == encoded_text_copy[:code_len]:
                text += c
                encoded_text_copy = encoded_text_copy[code_len:]
                break

    return text
