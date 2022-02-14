from Tests.testDomain import testCarte
from Tests.testCRUD import testAdaugaCarte, testStergeCarte, testmodificaCarte
from Tests.testFunctionalitate import testpretMin, testnumarTitluri, testmodificareGen, testaplicareDiscount, \
    testordonarePret
from Tests.testUndoRedo import testUndoRedo


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testmodificaCarte()
    testpretMin()
    testnumarTitluri()
    testaplicareDiscount()
    testmodificareGen()
    testordonarePret()
    testUndoRedo()
