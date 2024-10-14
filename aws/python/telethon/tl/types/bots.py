"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeBotPreviewMedia, TypeUser



class BotInfo(TLObject):
    CONSTRUCTOR_ID = 0xe8a775b0
    SUBCLASS_OF_ID = 0xca7b2235

    def __init__(self, name: str, about: str, description: str):
        """
        Constructor for bots.BotInfo: Instance of BotInfo.
        """
        self.name = name
        self.about = about
        self.description = description

    def to_dict(self):
        return {
            '_': 'BotInfo',
            'name': self.name,
            'about': self.about,
            'description': self.description
        }

    def _bytes(self):
        return b''.join((
            b'\xb0u\xa7\xe8',
            self.serialize_bytes(self.name),
            self.serialize_bytes(self.about),
            self.serialize_bytes(self.description),
        ))

    @classmethod
    def from_reader(cls, reader):
        _name = reader.tgread_string()
        _about = reader.tgread_string()
        _description = reader.tgread_string()
        return cls(name=_name, about=_about, description=_description)


class PopularAppBots(TLObject):
    CONSTRUCTOR_ID = 0x1991b13b
    SUBCLASS_OF_ID = 0x7b64be7d

    def __init__(self, users: List['TypeUser'], next_offset: Optional[str]=None):
        """
        Constructor for bots.PopularAppBots: Instance of PopularAppBots.
        """
        self.users = users
        self.next_offset = next_offset

    def to_dict(self):
        return {
            '_': 'PopularAppBots',
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users],
            'next_offset': self.next_offset
        }

    def _bytes(self):
        return b''.join((
            b';\xb1\x91\x19',
            struct.pack('<I', (0 if self.next_offset is None or self.next_offset is False else 1)),
            b'' if self.next_offset is None or self.next_offset is False else (self.serialize_bytes(self.next_offset)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _next_offset = reader.tgread_string()
        else:
            _next_offset = None
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(users=_users, next_offset=_next_offset)


class PreviewInfo(TLObject):
    CONSTRUCTOR_ID = 0xca71d64
    SUBCLASS_OF_ID = 0xf0c27f35

    def __init__(self, media: List['TypeBotPreviewMedia'], lang_codes: List[str]):
        """
        Constructor for bots.PreviewInfo: Instance of PreviewInfo.
        """
        self.media = media
        self.lang_codes = lang_codes

    def to_dict(self):
        return {
            '_': 'PreviewInfo',
            'media': [] if self.media is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.media],
            'lang_codes': [] if self.lang_codes is None else self.lang_codes[:]
        }

    def _bytes(self):
        return b''.join((
            b'd\x1d\xa7\x0c',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.media)),b''.join(x._bytes() for x in self.media),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.lang_codes)),b''.join(self.serialize_bytes(x) for x in self.lang_codes),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _media = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _media.append(_x)

        reader.read_int()
        _lang_codes = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_string()
            _lang_codes.append(_x)

        return cls(media=_media, lang_codes=_lang_codes)

