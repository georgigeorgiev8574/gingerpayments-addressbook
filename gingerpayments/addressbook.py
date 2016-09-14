
import re
# simple sanity check, regex from http://stackoverflow.com/a/8022584,
# i can use say https://pypi.python.org/pypi/validate_email for more thorough check
EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
# http://stackoverflow.com/a/33816411
PHONE_REGEX = re.compile(r'^\+(?=\d{5,15}$)(1|2[078]|3[0-469]|4[013-9]|5[1-8]|6[0-6]|7|8[1-469]|9[0-58]|[2-9]..)(\d+)$')


class addressbook():
    '''
    Address book class for Ginger Payments B.V. test.
    https://github.com/gingerpayments/hiring/blob/master/coding-assignments/python-address-book-assignment/python-address-book-assignment.rst
    '''
    
    def __init__(self, name):
        self.name = name  # not really needed, could be more... well... readable to have a human-readable name
        self.bookpeople = {}
        self.bookgroups = set()
    
    def addperson(self, firstname, lastname, streetaddresses, emails, phones, groups=[]):
        '''
        Only strings for first name and last name.
        I'll allow strings instead of arrays for streetaddresses, emails,
        phones and groups as it can be convenient.
        I'll also allow duplicate entries as there is no say social security
        number in our address book.
        Maybe allow adding bunch of people in one pass?
        Should I check for duplicated entries in arrays?
        '''
        
        # sanity checks
        if type(firstname) is not str:
            raise TypeError('The first name should be a string.')
        if firstname.strip() == '':  # technically this is not requred but still
            raise ValueError('The first name should not be empty.')
        
        if type(lastname) is not str:
            raise TypeError('The last name should be a string.')
        if lastname.strip() == '':  # technically this is not requred but still
            raise ValueError('The last name should not be empty.')
        
        if type(streetaddresses) is str:
            if streetaddresses.strip() == '':
                raise ValueError('The street address should not be empty.')
            streetaddresses = [streetaddresses]  # convert to array to not check for type again later
        elif type(streetaddresses) in (list, tuple):
            if len(streetaddresses) == 0:
                raise ValueError('There should be at least one address.')
            streetaddresses = list(streetaddresses)  # convert to list if tuple, i need item assignment
            for streetaddress in streetaddresses:
                if type(streetaddress) is not str:
                    raise TypeError('Every street address in the array should be a string.')
                if streetaddress.strip() == '':
                    raise ValueError('All street addresses in the array should not be empty.')
        else:
            raise TypeError('Street addresses variable should be string or array.')
        
        if type(emails) is str:
            if not EMAIL_REGEX.match(emails):
                raise ValueError('The email should have an @ and a dot.')
            emails = [emails]  # convert to array to not check for type again later
        elif type(emails) in (list, tuple):
            if len(emails) == 0:
                raise ValueError('There should be at least one email.')
            emails = list(emails)  # convert to list if tuple, i need item assignment
            for email in emails:
                if type(email) is not str:
                    raise TypeError('Every email in the array should be a string.')
                if not EMAIL_REGEX.match(email):
                    raise ValueError('All emails in the array should have an @ and a dot.')
        else:
            raise TypeError('Emails variable should be string or array.')
        
        if type(phones) is str:
            phones = phones.replace(' ','')
            if not PHONE_REGEX.match(phones):
                raise ValueError('The phone should be a valid international phone number, i.e. starts with +, has a valid country code and up to 15 digits total.')
            phones = [phones]  # convert to array to not check for type again later
        elif type(phones) in (list, tuple):
            if len(phones) == 0:
                raise ValueError('There should be at least one phone.')
            phones = list(phones)  # convert to list if tuple, i need item assignment
            for i in range(len(phones)):
                if type(phones[i]) is not str:
                    raise TypeError('Every phone in the array should be a string.')
                phones[i] = phones[i].replace(' ','')
                if not PHONE_REGEX.match(phones[i]):
                    raise ValueError('All phones in the array should be valid international phone numbers, i.e. start with +, has valid country codes and up to 15 digits each.')
        else:
            raise TypeError('Phones variable should be string or array.')
        
        if type(groups) is str:
            if type(groups) is not str:
                raise TypeError('The group name should be a string.')
            if groups.strip() == '':
                raise ValueError('The group name should not be empty.')
            if groups not in self.bookgroups:
                raise ValueError('Non-existent group: ' + groups)
            groups = [groups]  # convert to array to not check for type again later
        elif type(groups) in (list, tuple):
            #if len(groups) == 0:  # a person with no groups is allowed, right? 'can be a member', not 'should be a member'
                #raise ValueError('There should be at least one group.')
            groups = list(groups)  # convert to list if tuple, i need item assignment
            for group in groups:
                if type(group) is not str:
                    raise TypeError('Every group in the array should be a string.')
                if group.strip() == '':
                    raise ValueError('All group names in the array should not be empty.')
                if group not in self.bookgroups:
                    raise ValueError('Non-existent group in array: ' + group)
        else:
            raise TypeError('Groups variable should be string or array.')
        # end sanity checks
        
        # do the job
        id = len(self.bookpeople)  # the idea is to have easily searchable id
        self.bookpeople[id] = {'firstname': firstname,
                               'lastname': lastname,
                               'streetaddresses': streetaddresses,
                               'emails': emails,
                               'phones': phones,
                               'groups': groups}
        return id
    
    def addgroup(self, groupname):
        # sanity checks
        if type(groupname) is not str:
            raise TypeError('The group name should be a string.')
        if groupname.strip() == '':  # technically this is not requred but still
            raise ValueError('The group name should not be empty.')
        if groupname in self.bookgroups:
            raise ValueError('Group already exists')
        # end sanity checks
        
        # do the job
        self.bookgroups.add(groupname)
        return groupname
    
    def findpeoplebygroup(self, groupname):
        # sanity checks
        if type(groupname) is not str:
            raise TypeError('The group name should be a string.')
        if groupname.strip() == '':  # technically this is not requred but still
            raise ValueError('The group name should not be empty.')
        if groupname not in self.bookgroups:
            raise ValueError('Non-existant group: ' + groupname)
        # end sanity checks
        
        # do the job
        # If this is not easy enough, instead of set I can use for bookgroups a
        # dict with lists of people ids as values, but the information will be
        # redundant and potentially inconsistent.
        people = []
        for personid in self.bookpeople:
            if groupname in self.bookpeople[personid]['groups']:
                people.append(personid)
        return people
    
    def findgroups(self, personid):
        # sanity checks
        if type(personid) is not int:
            raise TypeError('The group name should be an integer.')
        if personid not in self.bookpeople:
            raise ValueError('Non-existant person id: ' + str(personid))
        # end sanity checks
        
        # do the job
        return self.bookpeople[personid]['groups']
    
    def findpeoplebynames(self, firstname=None, lastname=None):
        # sanity checks
        if firstname is None and lastname is None:
            raise ValueError('At leans one name should be not None.')
        if firstname is not None:
            if type(firstname) is not str:
                raise TypeError('The first name should be a string or None.')
            if firstname.strip() == '':  # technically this is not requred but still
                raise ValueError('The first name should not be empty.')
        if lastname is not None:
            if type(lastname) is not str:
                raise TypeError('The last name should be a string or None.')
            if lastname.strip() == '':  # technically this is not requred but still
                raise ValueError('The last name should not be empty.')
        # end sanity checks
        
        # do the job
        people = []
        for personid in self.bookpeople:
            if (firstname == self.bookpeople[personid]['firstname'] and lastname == self.bookpeople[personid]['lastname']) or \
               (firstname is None and lastname == self.bookpeople[personid]['lastname']) or \
               (firstname == self.bookpeople[personid]['firstname'] and lastname is None):  # a bit clumsy but works, i welcome suggestions :)
                people.append(personid)
        return people
    
    def findpeoplebyemail(self, emailprefix):
        # sanity checks
        if type(emailprefix) is not str:
            raise TypeError('The email should be a string.')
        if emailprefix.strip() == '':
            raise ValueError('The email prefix shoud not be empty.')
        # end sanity checks
        
        # do the job
        # This is naive, but works. Again, I can add emails dict to the class,
        # but this will be redundant and potentially inconsistent.
        # In this case I won't reinvent the wheel, but will use some library
        # say PyTrie or Biopython's trie.
        # Also, memory usage for preprocessing could be an issue.
        people = []
        for personid in self.bookpeople:
            for email in self.bookpeople[personid]['emails']:
                if email.startswith(emailprefix):
                    people.append(personid)
                    break  # save some time in case of duplicate prefixes
        return people
