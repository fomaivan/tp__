//
// Created by akhtyamovpavel on 5/1/20.
//


#pragma once

#include <gtest/gtest.h>
#include <boost/filesystem.hpp>
#include <Tree.h>
#include <string>
#include <iostream>
#include <fstream>


using namespace boost::filesystem;

class TreeTestCase : public ::testing::Test {
public:
    path p;
    path p2;
    std::ofstream testFile1;
    std::ofstream testFile2;

    
    TreeTestCase() {
        this->p = current_path();
        this->p += "/my_tmp";
        create_directory(p);
        path p1 = p;
        p1 += "/dir1";
        create_directory(p1);
        p2 = p;
        p2 += "/dir2";
        create_directory(p2);
        path p3 = p2;
        p3 += "/dirInsideDir";
        create_directory(p3);
        testFile1 = std::ofstream("my_tmp/testFileLongNameToBeFound.txt");
        testFile2 = std::ofstream("my_tmp/dir1/testFileXDXDXDXDXDXD.txt");
    }
    
    ~TreeTestCase() {
        testFile1.close();
        testFile2.close();
        remove_all(this->p);
    }
};

TEST_F(TreeTestCase, PathDoesntExistsTest) {
    ASSERT_THROW(GetTree("blablablabla", true), std::invalid_argument);
}

TEST_F(TreeTestCase, PathIsntDirectoryTest) {
    ASSERT_THROW(GetTree(p.string() + "/testFileLongNameToBeFound.txt", true), std::invalid_argument);
}

TEST_F(TreeTestCase, NotOnlyDirsTest) {
    ASSERT_NO_THROW(GetTree(p.string(), false));
}

TEST_F(TreeTestCase, DirsOnlyTest) {
    ASSERT_NO_THROW(GetTree(p.string(), true));
}

TEST_F(TreeTestCase, EqualityTest) {
    ASSERT_TRUE(GetTree(p.string(), true) == GetTree(p.string(), true));
    ASSERT_FALSE(GetTree(p.string(), true) == GetTree(p2.string(), true));
}
