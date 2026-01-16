from pathlib import Path
from pyshacl import validate

def test_systemgraph_validator():
    shacl_graph = Path(__file__).parent.parent.resolve() / "docs/assets/systemgraph-validator.ttl"

    for f in sorted(list(Path(Path(__file__).parent / "data").glob("*.ttl"))):
        valid = True
        if "invalid" in f.name:
            valid = False

        v = validate(str(f), shacl_graph=str(shacl_graph))

        if v[0] == valid:
            pass
        else:
            print(f"{f}: {v[2]}")

        if not valid:
            print(f"{f}: {v[2]}")

        assert v[0] == valid