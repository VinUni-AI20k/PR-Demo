import tempfile
from pathlib import Path

from tasktrack.storage import Storage


def test_add_and_list() -> None:
    with tempfile.TemporaryDirectory() as d:
        store = Storage(Path(d) / "t.db")
        t = store.add("hello")
        assert t.id == 1
        assert [x.title for x in store.list()] == ["hello"]


def test_mark_done() -> None:
    with tempfile.TemporaryDirectory() as d:
        store = Storage(Path(d) / "t.db")
        t = store.add("hello")
        store.mark_done(t.id)
        assert store.list()[0].done is True
