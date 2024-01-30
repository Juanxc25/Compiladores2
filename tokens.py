from enum import Enum
from dataclasses import dataclass
class TokenType(Enum):
    FOR = 1
    DO =2
    WHILE = 3
    IF = 4
    LPAREN = 6
    RPAREN =7
    ERROR = 0 
    

@dataclass
class Token:
    token_type : TokenType
    lexeme:str
    
            