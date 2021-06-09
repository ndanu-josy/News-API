import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('KTN','KTN News','The good, the bad, the ugly','ktnnews.com','general','Kenya','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'KTN')
        self.assertEquals(self.new_source.name,'kTN News')
        self.assertEquals(self.new_source.description,'The good, the bad, the ugly')
        self.assertEquals(self.new_source.url,'ktnnews.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'Kenya')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('KTN','Josphine Ndanu','Technology','A deep dive into technology and how Kenyans take the matter','technology.com','tech.jpg','2021-06-08T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'KTN')
        self.assertEquals(self.new_article.author,'Josphine Ndanu')
        self.assertEquals(self.new_article.title,'Technology')
        self.assertEquals(self.new_article.description,'A deep dive into technology and how Kenyans take the matter')
        self.assertEquals(self.new_article.url,'technology.com')
        self.assertEquals(self.new_article.image,'tech.jpg')
        self.assertEquals(self.new_article.date,'2021-06-08T07:57:16Z')
