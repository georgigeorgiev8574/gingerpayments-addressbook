import unittest
from addressbook import addressbook

class TestGroupErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addgroup('')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addgroup(1)
    def test_list(self):
        with self.assertRaises(TypeError):
            self.abook.addgroup(['groupname'])
    def test_tuple(self):
        with self.assertRaises(TypeError):
            self.abook.addgroup(('groupname',))
    def test_alreadyexisting(self):
        testname = 'groupname'
        self.abook.addgroup(testname)
        with self.assertRaises(ValueError):
            self.abook.addgroup(testname)
    def tearDown(self):
        del self.abook

class TestGroupCorrect(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_addgroup(self):
        testname = 'groupname'
        self.assertEqual(self.abook.addgroup(testname), testname)
    def tearDown(self):
        del self.abook

class TestNotEnoughParameters(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_noparameters(self):
        with self.assertRaises(TypeError):
            self.abook.addperson()
    def test_notenoughparameters(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('d','-')
    def tearDown(self):
        del self.abook

class TestFirstnameErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('','smith','zip, city, street #','john@example.com','+359 88 888 8888')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson(1,'smith','zip, city, street #','john@example.com','+359 88 888 8888')
    def test_list(self):
        with self.assertRaises(TypeError):
            self.abook.addperson(['john', 'james'],'smith','zip, city, street #','john@example.com','+359 88 888 8888')
    def test_tuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson(('john', 'james'),'smith','zip, city, street #','john@example.com','+359 88 888 8888')
    def tearDown(self):
        del self.abook

class TestLastnameErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','','zip, city, street #','john@example.com','+359 88 888 8888')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john',1,'zip, city, street #','john@example.com','+359 88 888 8888')
    def test_list(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john',['smith','jones'],'zip, city, street #','john@example.com','+359 88 888 8888')
    def test_tuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john',('smith','jones'),'zip, city, street #','john@example.com','+359 88 888 8888')
    def tearDown(self):
        del self.abook

class TestStreetaddressErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','','john@example.com','+359 88 888 8888')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith',1,'john@example.com','+359 88 888 8888')
    def test_emptyinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith',['zip, city, street #',''],'john@example.com','+359 88 888 8888')
    def test_intinlist(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith',['zip, city, street #',1],'john@example.com','+359 88 888 8888')
    def test_emptyintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith',('zip, city, street #',''),'john@example.com','+359 88 888 8888')
    def test_intintuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith',('zip, city, street #',1),'john@example.com','+359 88 888 8888')
    def tearDown(self):
        del self.abook

class TestEmailErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','','+359 88 888 8888')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #',1,'+359 88 888 8888')
    def test_nodot(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@examplecom','+359 88 888 8888')
    def test_noat(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','johnexample.com','+359 88 888 8888')
    def test_emptyinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',['john@example.com',''],'+359 88 888 8888')
    def test_intinlist(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #',['john@example.com',1],'+359 88 888 8888')
    def test_nodotinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',['john@example.com','john@examplecom'],'+359 88 888 8888')
    def test_noatinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',['john@example.com','johnexample.com'],'+359 88 888 8888')
    def test_emptyintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',('john@example.com',''),'+359 88 888 8888')
    def test_intintuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #',('john@example.com',1),'+359 88 888 8888')
    def test_nodotintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',('john@example.com','john@examplecom'),'+359 88 888 8888')
    def test_noatintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #',('john@example.com','johnexample.com'),'+359 88 888 8888')
    def tearDown(self):
        del self.abook

class TestPhoneErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',359888888888)
    def test_toomanydigits(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888 8888')
    def test_noplus(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','359 88 888 8888')
    def test_badsymbol1(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','359 88+888 8888')
    def test_badsymbol2(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88z888 8888')
    def test_emptyinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888',''])
    def test_intinlist(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888',359888888888])
    def test_toomanydigitsinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888','+359 88 888 8888 8888'])
    def test_noplusinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888','359 88 888 8888'])
    def test_badsymbol1inlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888','359 88+888 8888'])
    def test_badsymbol2inlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',['+359 88 888 8888','+359 88z888 8888'])
    def test_emptyintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888',''))
    def test_intintuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888',359888888888))
    def test_toomanydigitsintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888','+359 88 888 8888 8888'))
    def test_noplusintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888','359 88 888 8888'))
    def test_badsymbol1intuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888','359 88+888 8888'))
    def test_badsymbol2intuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com',('+359 88 888 8888','+359 88z888 8888'))
    def tearDown(self):
        del self.abook

class TestPersonGroupErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addgroup('group1')
    def test_nonexistent(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888','non-existent group')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888','')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',1)
    def test_nonexistentinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',['group1','non-existent group'])
    def test_emptyinlist(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',['group1',''])
    def test_intinlist(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',['group1',1])
    def test_nonexistentintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',('group1','non-existent group'))
    def test_emptyintuple(self):
        with self.assertRaises(ValueError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',('group1',''))
    def test_intintuple(self):
        with self.assertRaises(TypeError):
            self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888',('group1',1))
    def tearDown(self):
        del self.abook

class TestPersonCorrect(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.firstid = 0
        self.secondid = 1
        self.abook.addgroup('group1')
        self.abook.addgroup('group2')
    def test_nogroups(self):
        self.assertEqual(self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888'), self.firstid)
    def test_strings(self):
        self.assertEqual(self.abook.addperson('john','smith','zip, city, street #','john@example.com','+359 88 888 8888','group1'), self.firstid)
    def test_lists(self):
        self.assertEqual(self.abook.addperson('john','smith',['zip, city, street #', 'zip2, city2, street2 #2'],
                                              ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2']), self.firstid)
    def test_tuples(self):
        self.assertEqual(self.abook.addperson('john','smith',('zip, city, street #', 'zip2, city2, street2 #2'),
                                              ('john@example.com','john2@example.com'),('+359 88 888 8888','+359 89 999 9999'),('group1','group2')), self.firstid)
    def test_multiple(self):
        self.assertEqual(self.abook.addperson('john','smith',['zip, city, street #', 'zip2, city2, street2 #2'],
                                              ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2']), self.firstid)
        self.assertEqual(self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777'), self.secondid)
    def tearDown(self):
        del self.abook

class TestFindPeopleByGroupErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebygroup('')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.findpeoplebygroup(1)
    def test_nonexistant(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebygroup('non-existant group')
    def tearDown(self):
        del self.abook

class TestFindPeopleByGroup(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addgroup('group1')
        self.abook.addgroup('group2')
        self.abook.addgroup('group3')
        self.abook.addgroup('group4')
        self.abook.addperson('john','smith',['zip, city, street #', 'zip6, city6, street6 #6'],
                             ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2'])
        self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777')
        self.abook.addperson('carter','brown','zip3, city3, street3 #3','brown@example.com',
                             ['+359 88 888 6666','+359 89 999 5555'],['group1','group3'])
        self.abook.addperson('michelangelo','buonarroti','zip4, city4, street4 #4',['mike@example.com','turtle@example.com'],
                             '+359 88 888 4444','group1')
        self.abook.addperson('uncle','charlie','malibu, on the beach','charlie@example.com','+359 88 888 3333','group4')
    def test_findone(self):
        self.assertEqual(self.abook.findpeoplebygroup('group2'), [0])
        self.assertEqual(self.abook.findpeoplebygroup('group3'), [2])
        self.assertEqual(self.abook.findpeoplebygroup('group4'), [4])
    def test_findmultiple(self):
        self.assertEqual(self.abook.findpeoplebygroup('group1'), [0,2,3])
    def tearDown(self):
        del self.abook

class TestFindGroupsErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777')
    def test_string(self):
        with self.assertRaises(TypeError):
            self.abook.findgroups('0')
    def test_nonexistant(self):
        with self.assertRaises(ValueError):
            self.abook.findgroups(1)
    def tearDown(self):
        del self.abook

class TestFindGroups(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addgroup('group1')
        self.abook.addgroup('group2')
        self.abook.addgroup('group3')
        self.abook.addperson('john','smith',['zip, city, street #', 'zip6, city6, street6 #6'],
                             ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2'])
        self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777', 'group3')
    def test_findone(self):
        self.assertEqual(self.abook.findgroups(1), ['group3'])
    def test_findmultiple(self):
        self.assertEqual(self.abook.findgroups(0), ['group1','group2'])
    def tearDown(self):
        del self.abook

class TestFindPeopleByNamesErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777')
    def test_firstnameempty(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebynames('', 'jones')
    def test_firstnameint(self):
        with self.assertRaises(TypeError):
            self.abook.findpeoplebynames(1, 'jones')
    def test_lastnameempty(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebynames('james','')
    def test_lastnameint(self):
        with self.assertRaises(TypeError):
            self.abook.findpeoplebynames('james',1)
    def test_bothnone(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebynames(None, None)
    def tearDown(self):
        del self.abook

class TestFindPeopleByNames(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addgroup('group1')
        self.abook.addgroup('group2')
        self.abook.addgroup('group3')
        self.abook.addgroup('group4')
        self.abook.addperson('john','smith',['zip, city, street #', 'zip6, city6, street6 #6'],
                             ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2'])
        self.abook.addperson('carter','smith','zip3, city3, street3 #3','brown@example.com',
                             ['+359 88 888 6666','+359 89 999 5555'],['group1','group3'])
        self.abook.addperson('michelangelo','buonarroti','zip4, city4, street4 #4',['mike@example.com','turtle@example.com'],
                             '+359 88 888 4444','group1')
        self.abook.addperson('uncle','charlie','malibu, on the beach','charlie@example.com','+359 88 888 3333','group4')
    def test_findbyfirstname(self):
        self.assertEqual(self.abook.findpeoplebynames('michelangelo',None), [2])
    def test_findbylastname(self):
        self.assertEqual(self.abook.findpeoplebynames(None,'smith'), [0,1])
    def test_findbybothnames(self):
        self.assertEqual(self.abook.findpeoplebynames('john','smith'), [0])
        self.assertEqual(self.abook.findpeoplebynames('uncle','charlie'), [3])
    def tearDown(self):
        del self.abook

class TestFindPeopleByEmailErrors(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
    def test_empty(self):
        with self.assertRaises(ValueError):
            self.abook.findpeoplebyemail('')
    def test_int(self):
        with self.assertRaises(TypeError):
            self.abook.findpeoplebyemail(1)
    def tearDown(self):
        del self.abook

class TestFindPeopleByEmail(unittest.TestCase):
    def setUp(self):
        self.abook = addressbook('book name')
        self.abook.addgroup('group1')
        self.abook.addgroup('group2')
        self.abook.addgroup('group3')
        self.abook.addgroup('group4')
        self.abook.addperson('john','smith',['zip, city, street #', 'zip6, city6, street6 #6'],
                             ['john@example.com','john2@example.com'],['+359 88 888 8888','+359 89 999 9999'],['group1','group2'])
        self.abook.addperson('james','jones','zip2, city2, street2 #2','james@example.com','+359 87 777 7777')
        self.abook.addperson('carter','brown','zip3, city3, street3 #3','brown@example.com',
                             ['+359 88 888 6666','+359 89 999 5555'],['group1','group3'])
        self.abook.addperson('michelangelo','buonarroti','zip4, city4, street4 #4',['mike@example.com','turtle@example.com'],
                             '+359 88 888 4444','group1')
        self.abook.addperson('uncle','charlie','malibu, on the beach','charlie@example.com','+359 88 888 3333','group4')
    def test_findbywholeemail(self):
        self.assertEqual(self.abook.findpeoplebyemail('turtle@example.com'), [3])
        self.assertEqual(self.abook.findpeoplebyemail('charlie@example.com'), [4])
    def test_findbypartialemail(self):
        self.assertEqual(self.abook.findpeoplebyemail('j'), [0,1])
    def tearDown(self):
        del self.abook

if __name__ == '__main__':
    unittest.main()
