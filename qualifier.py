"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import collections
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return f"<{self.__class__.__name__} title={repr(self.title)} "\
               f"author={repr(self.author)} "\
               f"publication_date={repr(self.publication_date.isoformat())}>"

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        """Returns a short description of the article"""
        if self.content[n_characters-1] not in [' ', '\n']:

            try:
                n_characters = max(
                    self.content.rindex(' ', 0, n_characters),
                    self.content.rindex('\n', 0, n_characters)
                    )
            except ValueError:
                if not self.content.rindex(' ', 0, n_characters):
                    n_characters = self.content.rindex('\n', 0, n_characters)
                else:
                    n_characters = self.content.rindex(' ', 0, n_characters)

            return self.content[:n_characters]

        return self.content[:n_characters].rstrip()

    def most_common_words(self, n_words: int):
        """Returns freq of most common words as a dict"""
        words = re.findall(r'[\w]+', self.content.lower())
        wordfreq = collections.Counter(words).most_common(n_words)

        return dict(wordfreq)
