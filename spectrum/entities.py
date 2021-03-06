# -*- coding: utf-8 -*-
from .member import Member


class Emoji:
    """Represents a Spectrum Emoji object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | str(x)    | Returns the emoji's name.               |
    +-----------+-----------------------------------------+

    mutability : str
        Displays the mutability of the emoji. I do not know what this means in
        context, or when they are ever mutable. I have an open prize of 3 free
        original tapirs to anyone who can solve this.
    emoji : str
        Displays the name in the form :<name>: just taken from the raw JSON. I
        do not know if I will ever do able to code and decode from Unicode.
        There is a large block of Javascript in the Javascript that runs
        Spectrum that converts between str and an object, but I do not think I
        can convert between Unicode and str.
    offset : int
        The offset of where the emoji resides within the block.
    length : int
        The length of string that the emoji takes up from the offset in the raw
        block content.
    """

    __slots__ = [
                'mutability', 'emoji', 'offset', 'length',
    ]

    def __init__(self, **kwargs):
        self.mutability = kwargs.pop('mutability')
        self.emoji = kwargs.pop('data')
        self.offset = kwargs.pop('offset')
        self.length = kwargs.pop('length')

    def __str__(self):
        return self.emoji


class Mention:
    """Represents a Spectrum mention object

    Supported Operations:

    +-----------+----------------------------------------------------+
    | Operation |                     Description                    |
    +===========+====================================================+
    | str(x)    | Returns the mention's user_id, or the member's name|
    +-----------+----------------------------------------------------+

    mutability : str
        Displays the mutability of the mention. I do not know what this means in
        context, or when they are ever mutable. I have an open prize of 3 free
        original tapirs to anyone who can solve this.
    user_id : int
        Displays the id of the user mentioned
    member : :class:`Member` or ``None``
        This attribute represents the member that the mention mentions if they
        are in the client's cache. If not it defaults to ``None``
    offset : int
        The offset of where the mention resides within the block.
    length : int
        The length of string that the mention takes up from the offset in the
        raw block content.
    """

    __slots__ = [
                'mutability', 'user_id', 'member', 'offset', 'length',
    ]

    def __init__(self, member=None, **kwargs):
        self.mutability = kwargs.pop('mutability')
        self.user_id = int(kwargs.pop('data').pop('id'))
        self.member = member
        self.offset = kwargs.pop('offset')
        self.length = kwargs.pop('length')

    def __str__(self):
        if self.member is None and not isinstance(self.member, Member):
            return self.user_id
        else:
            return self.member.name


class Link:
    """Represents a Spectrum Link object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | str(x)    | Returns the link's url.                 |
    +-----------+-----------------------------------------+

    mutability : str
        Displays the mutability of the link. I do not know what this means in
        context, or when they are ever mutable. I have an open prize of 3 free
        original tapirs to anyone who can solve this.
    url : str
        The url that the link object represents.
    offset : int
        The offset of where the link resides within the block.
    length : int
        The length of string that the link takes up from the offset in the raw
        block content.
    """

    __slots__ = [
                'mutability', 'url', 'offset', 'length',
    ]

    def __init__(self, **kwargs):
        self.mutability = kwargs.pop('mutability')
        self.url = kwargs.pop('data').pop('href')
        self.offset = kwargs.pop('offset')
        self.length = kwargs.pop('length')

    def __str__(self):
        return self.url
