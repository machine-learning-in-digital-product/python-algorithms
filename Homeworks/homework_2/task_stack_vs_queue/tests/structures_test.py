import pytest

from src.custom_queue import Queue
from src.custom_stack import Stack
from src.node import Node


# ---------- Stack tests ----------

def test_stack_push_and_top_lifo():
    s = Stack()
    s.push(Node(1))
    s.push(Node(2))
    s.push(Node(3))
    assert s.top() == 3
    s.pop()
    assert s.top() == 2
    s.pop()
    assert s.top() == 1

def test_stack_pop_until_empty_and_errors(capsys):
    s = Stack()
    assert s.pop() is None
    captured = capsys.readouterr()
    assert "Error: List is empty" in captured.out

    s.push(Node(10))
    s.push(Node(20))
    s.pop()
    s.pop()      
    assert s.is_empty()

    assert s.top() is None
    captured = capsys.readouterr()
    assert "Error: List is empty" in captured.out


# ---------- Queue tests ----------

def test_queue_enqueue_dequeue_fifo():
    q = Queue()
    q.enqueue(Node(10))
    q.enqueue(Node(20))
    q.enqueue(Node(30))

    # порядок FIFO
    assert q.front() == 10
    assert q.dequeue() == 10
    assert q.front() == 20
    assert q.dequeue() == 20
    assert q.front() == 30
    assert q.dequeue() == 30

    assert q.is_empty()

def test_queue_tail_resets_to_none_when_empty():
    q = Queue()
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    q.dequeue()
    assert not q.is_empty()
    q.dequeue()
    assert q.is_empty()
    assert q.head is None and q.tail is None

def test_queue_errors_on_empty(capsys):
    q = Queue()
    assert q.front() is None
    out = capsys.readouterr().out
    assert "Error: Queue is empty" in out

    assert q.dequeue() is None
    out = capsys.readouterr().out
    assert "Error: Queue is empty" in out
