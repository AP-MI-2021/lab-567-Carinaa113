from Tests.testCRUD import testAdaugaCarte,testStergeCarte
from Tests.testDomain import testCarte
from Test.testFunctionalitate import testaplicareDiscount,testmodificareGen,testpretMin,testordonarePret,testnumarTitluri


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testpretMin()
    testnumarTitluri()
    testaplicareDiscount()
    testmodificareGen()
