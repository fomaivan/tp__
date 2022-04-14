import os
import shutil
import tempfile

from src.tree_utils_02.node import FileNode
from src.tree_utils_02.size_node import FileSizeNode
from src.tree_utils_02.size_tree import SizeTree
from src.tree_utils_02.tree import Tree
from tree_utils_02.size_tree import *
from tree_utils_02.tree import *

def test_update_node():
    tree_size = SizeTree()
    with tempfile.TemporaryDirectory() as first:
        os.chdir(first)
        os.mkdir('second')
        txt = open('file.txt', 'w+')
        file = FileSizeNode('file.txt', False, [], 0)
        second = FileSizeNode('second', True, [], 4096)
        node = FileSizeNode(os.path.basename(first), True, [file, second], 1)
        assert 4097 == tree_size.update_filenode(node).size


def test_constructor_dir():
    tree_size = SizeTree()
    with tempfile.TemporaryDirectory() as tmp:
        size_node = FileSizeNode(os.path.basename(tmp), True, [], 4096)
        assert size_node == tree_size.construct_filenode(tmp, True)


def test_constructor_file():
    tree_size = SizeTree()
    with tempfile.NamedTemporaryFile() as tmp:
        size_node = FileSizeNode(os.path.basename(tmp.name), False, [], 0)
        assert size_node == tree_size.construct_filenode(tmp.name, False)
