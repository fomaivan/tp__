import os
import shutil
import tempfile

import pytest
from tree_utils_02.size_tree import *
from tree_utils_02.tree import *

from src.tree_utils_02.node import FileNode
from src.tree_utils_02.tree import Tree


def test_constructor():
    tree = Tree()
    assert FileNode('example.txt', False, []) == tree.construct_filenode('../example.txt', False)


def test_update():
    tree = Tree()
    a = 6
    assert tree.update_filenode(a) == 6


def test_filter_file():
    tree = Tree()
    node = FileNode('example.txt', False, [])
    assert None == tree.filter_empty_nodes(node)


def test_filter_dir():
    tree = Tree()
    with tempfile.TemporaryDirectory() as first:
        os.chdir(first)
        os.mkdir('second')
        file = FileNode('file.txt', False, [])
        second = FileNode('second', True, [])
        node = FileNode(os.path.basename(first), True, [file, second])
        tree.filter_empty_nodes(node)
        assert False == os.path.exists('second')


def test_get_with_wrong_path():
    with pytest.raises(AttributeError):
        tree = Tree()
        tree.get('', True)


def test_get_file():
    tmp = tempfile.NamedTemporaryFile()
    tree = Tree()
    assert FileNode(os.path.basename(tmp.name), False, []) == tree.get(tmp.name, False)
    tmp.close()


def test_get_file_with_error():
    with pytest.raises(AttributeError):
        tmp = tempfile.NamedTemporaryFile()
        tree = Tree()
        tree.get(tmp.name, True)
        tmp.close()


def test_get_file_recursively():
    tmp = tempfile.NamedTemporaryFile()
    tree = Tree()
    assert None == tree.get(tmp.name, True, True)
    tmp.close()


def test_get_dir():
    tree = Tree()
    with tempfile.TemporaryDirectory() as first:
        os.chdir(first)
        os.mkdir('second')
        txt = open('file.txt', 'w+')
        file = FileNode('file.txt', False, [])
        second = FileNode('second', True, [])
        assert FileNode(os.path.basename(first), True, [file, second]) == tree.get(first, False)


