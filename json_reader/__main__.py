import sys
import json
from json_reader.decoder import JSONDecoder, iter_loads
from json_reader.decoder_node_py import NodePyCompatibleScanner


def main():
    decoder = JSONDecoder(scanner_cls=NodePyCompatibleScanner)
    for data, left in iter_loads(sys.stdin.read(), decoder=decoder):
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
