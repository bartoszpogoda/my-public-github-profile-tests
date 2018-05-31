import unittest
from selenium import webdriver
from collections import Counter
from datetime import datetime, timedelta


class MyPublicGithubProfileTests(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to my github page
        self.driver.get('https://github.com/bartoszpogoda')

    # Checks if my first and last name are set correctly
    def test_my_name(self):
        name_container = self.driver.find_element_by_css_selector('.vcard-fullname')
        self.assertTrue('Bartosz Pogoda' in name_container.text, 'Hey! Did you change your name recently?')

    # Checks if I am popular enough
    def test_more_than_5_followers(self):
        number_of_followers = int(self.driver.find_element_by_css_selector('[title="Followers"] span.Counter').text)
        self.assertGreater(number_of_followers, 5, 'You\'re not popular enough!')

    # Checks if Java is still my favorite language
    def test_java_dominance(self):
        # Navigate to repositories page
        self.driver.find_element_by_partial_link_text('Repositories').click()

        # Find most frequently used language
        languages = self.driver.find_elements_by_css_selector('span[itemprop="programmingLanguage"]')
        languages = map(lambda x: x.text, languages)
        counted_languages = Counter(languages)

        most_common = counted_languages.most_common(1)

        # Assert it is Java
        self.assertEqual('Java', most_common[0][0], 'Seems like you should program more in Java.')

    # Checks if I've performed at more than 5 commits in the last week
    def test_commits_last_week(self):
        last_week_dates = map(lambda date: date.strftime("%Y-%m-%d"),
                              (map(lambda diff: datetime.today() - timedelta(days=diff), range(0, 7))))

        def get_commits_for_date(date):
            return int(self.driver.find_element_by_css_selector\
                ('svg.js-calendar-graph-svg rect.day[data-date="'
                 + date + '"').get_attribute('data-count'))

        commit_counts = list(map(get_commits_for_date, last_week_dates))

        self.assertGreater(sum(commit_counts), 5, 'Commit more to committing!')

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
