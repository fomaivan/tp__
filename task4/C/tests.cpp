#include <gtest/gtest.h>
#include "main.h"

TEST(Test1, TestClass) {
    ClassLib x;
    x.Set(6);
    ASSERT_EQ(x.Get(), 6);
}
TEST(Test2, TestClass) {
    ASSERT_EQ(3 + 1, 4);
}
